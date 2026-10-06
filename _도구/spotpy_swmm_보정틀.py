r"""SPOTPY 로 SWMM 파라미터를 보정하는 틀. 33_루프.md 의 캘리브레이션을 정식 최적화기로 돌린다.

무엇을 왜 만들었나
  루프 방식은 에이전트가 다음 파라미터를 손으로 고른다. 파라미터 공간이 넓으면
  느리고 한쪽으로 쏠린다. SPOTPY 는 LHS · SCE-UA · DDS 같은 정식 탐색기로 뒤지고,
  시도마다 파라미터와 지표를 CSV 에 남긴다. 판정(KGE 문턱)은 여전히 밖에서 한다.

  파라미터 바꾸기는 swmmio 로 한다. 정본 모형(2021E10, CONTROLS · CUSTOM 포함)에서
  읽고 되써도 34 절이 그대로이고 모의 결과가 원본과 같음을 확인했다(2026-09-20).

역할 분담
  탐색        SPOTPY               어느 값을 시도할지
  모의        pyswmm               돌린다
  고치기      swmmio               .inp 에 값을 넣는다
  판정        이 파일의 kge()      33_루프.md 의 verify.py 와 같은 식
  범위 · 금지  사람                 PARAMS 를 정하고 건드리지 말 것을 뺀다

쌍둥이 시험 (--쌍둥이)
  원본 모형의 유출을 관측값으로 삼고 불투수율 배수를 흩뜨린 뒤 정답 1.0 근처를
  되찾는지 본다. 틀이 제대로 이어졌는지 확인하는 용도다. 실제 보정 전에 한 번 돌린다.

실행
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _도구\spotpy_swmm_보정틀.py ^
      --inp <정본.inp> --obs <관측.csv> --node OUT1 --alg lhs --reps 30
  C:\Users\SGJEONG99\anaconda3\envs\pyswmm\python.exe -X utf8 _도구\spotpy_swmm_보정틀.py ^
      --inp <정본.inp> --쌍둥이 --reps 8

  관측 CSV 는 두 열이다:  시각(YYYY-MM-DD HH:MM) , 값(모형과 같은 단위)

주의
  작업 사본은 C:\swmm_work\YYYYMMDD_HHMM_spotpy\ 에 둔다. 한글 경로는 SWMM 이 못 읽는다.
  원본 .inp 는 읽기만 한다.
  보정용과 검증용 사상을 섞지 마라. 이 틀은 한 사상만 본다. 검증은 다른 사상에서 한다.
"""
import argparse
import datetime
import os
import shutil
import sys
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)

# ---------------------------------------------------------------- 보정할 파라미터
# (이름, 하한, 상한, 적용 함수)  적용 함수는 swmmio 모형을 받아 값을 넣는다.
# 배수로 다루면 소유역마다 다른 값을 한 번에 흔들 수 있다.


def _배수(section, col):
    def f(model, x):
        df = getattr(model.inp, section)
        c = [k for k in df.columns if k.lower() == col.lower()][0]
        df[c] = (df[c].astype(float) * x).clip(upper=100.0 if "perc" in col.lower() else None)
        setattr(model.inp, section, df)
    return f


# 상한에 걸리는 파라미터는 식별이 안 된다. 2021E10 은 소유역 262 개 중 52 개(20%)가
# 이미 불투수율 100 이고 중앙값이 93.7 이다. 배수를 1.0 위로 올리면 상당수가 100 에서
# 잘려 결과가 평평해진다. 쌍둥이 시험에서 배수 1.02 와 1.09 가 둘 다 KGE 1.0000 이었다.
# 불투수율을 올리는 쪽으로 맞춰야 한다면 100 에 붙은 소유역을 빼고 흔든다.
PARAMS = [
    ("imperv_scale", 0.70, 1.10, _배수("subcatchments", "PercImperv")),
    # ("width_scale", 0.5, 2.0, _배수("subcatchments", "Width")),
    # ("n_imperv_scale", 0.7, 1.5, _배수("subareas", "N-Imperv")),
]
# 건드리지 말 것은 여기에 올리지 않는다. 예: 실측 토지피복에서 온 값


# ---------------------------------------------------------------- 지표
def kge(obs, sim):
    """Gupta 2009. 33_루프.md 의 verify.py 와 같은 식이다."""
    obs = np.asarray(obs, dtype=float)
    sim = np.asarray(sim, dtype=float)
    m = np.isfinite(obs) & np.isfinite(sim)
    obs, sim = obs[m], sim[m]
    if len(obs) < 3 or obs.std() == 0 or sim.std() == 0:
        return float("nan")
    r = np.corrcoef(obs, sim)[0, 1]
    return 1.0 - float(np.sqrt((r - 1) ** 2 + (sim.std() / obs.std() - 1) ** 2
                               + (sim.mean() / obs.mean() - 1) ** 2))


# ---------------------------------------------------------------- 모의
def 모의(inp, node):
    """inp 를 돌려 node 의 total_inflow 시계열을 돌려준다. 보고 간격으로 뽑는다."""
    from pyswmm import Simulation, Nodes
    vals, times = [], []
    with Simulation(inp) as sim:
        sim.step_advance(60)                  # 1 분마다 멈춰 값을 읽는다
        n = Nodes(sim)[node]
        for _ in sim:
            times.append(sim.current_time)
            vals.append(n.total_inflow)
    return pd.Series(vals, index=pd.to_datetime(times))


class Setup:
    def __init__(self, inp, obs, node, work):
        import spotpy
        import swmmio
        self.swmmio = swmmio
        self.base = inp
        self.obs = obs
        self.node = node
        self.work = work
        self.n = 0
        self.params = [spotpy.parameter.Uniform(n, low=lo, high=hi)
                       for n, lo, hi, _ in PARAMS]

    def parameters(self):
        import spotpy
        return spotpy.parameter.generate(self.params)

    def simulation(self, x):
        self.n += 1
        p = os.path.join(self.work, "run_%03d.inp" % self.n)
        m = self.swmmio.Model(self.base)
        for (name, _, _, f), v in zip(PARAMS, x):
            f(m, float(v))
        m.inp.save(p)
        s = 모의(p, self.node)
        s = s.reindex(self.obs.index, method="nearest", tolerance=pd.Timedelta("30s"))
        print("[%03d] %s  KGE=%.4f" % (self.n, " ".join("%s=%.4f" % (a[0], b)
              for a, b in zip(PARAMS, x)), kge(self.obs.values, s.values)), flush=True)
        for ext in (".out", ".rpt"):               # 용량이 커서 지운다. inp 는 남긴다
            q = p[:-4] + ext
            if os.path.exists(q):
                os.remove(q)
        return s.values.tolist()

    def evaluation(self):
        return self.obs.values.tolist()

    def objectivefunction(self, simulation, evaluation, params=None):
        return kge(evaluation, simulation)       # 클수록 좋다


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inp", required=True)
    ap.add_argument("--obs")
    ap.add_argument("--node", default="OUT1")
    ap.add_argument("--alg", default="lhs", choices=["lhs", "mc", "sceua", "dds"])
    ap.add_argument("--reps", type=int, default=30)
    ap.add_argument("--쌍둥이", action="store_true")
    ap.add_argument("--강행", action="store_true",
                    help="매끄러움 점검에서 멈춰도 보정을 진행한다")
    a = ap.parse_args()

    import spotpy

    assert os.path.exists(a.inp), "inp 가 없다: %s" % a.inp
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    work = r"C:\swmm_work\%s_spotpy" % stamp
    assert not os.path.exists(work), "작업 폴더가 이미 있다: %s" % work
    os.makedirs(work)
    base = os.path.join(work, "base.inp")
    shutil.copy2(a.inp, base)                   # 원본은 읽기만 한다
    print("작업 폴더", work)

    if a.쌍둥이:
        obs = 모의(base, a.node)
        obs = obs[obs.index >= obs.index[0] + pd.Timedelta("1h")]   # 초기 구간 제외
        print("쌍둥이: 원본 모의를 관측으로 쓴다. 정답은 모든 배수 = 1.0")
    else:
        assert a.obs, "--obs 가 필요하다"
        d = pd.read_csv(a.obs)
        obs = pd.Series(d.iloc[:, 1].astype(float).values,
                        index=pd.to_datetime(d.iloc[:, 0]))
    assert len(obs) > 10, "관측 자료가 너무 적다: %d" % len(obs)

    # 보정 전 매끄러움 점검. 파라미터를 0.1% 만 흔들어 응답이 끊기는지 본다.
    # 펌프 · 스위치로 움직이는 지점은 조금만 바뀌어도 가동 횟수가 달라져 계단처럼
    # 튄다. 실측: 2021E10 OUT1 에서 배수 0.999 의 KGE 가 -0.07, 평균비 1.333.
    # 이런 지점은 어떤 최적화기로도 못 맞춘다. 연속으로 응답하는 지점을 골라야 한다.
    if not a.강행:
        import swmmio
        s0 = 모의(base, a.node)
        p1 = os.path.join(work, "smooth_check.inp")
        m = swmmio.Model(base)
        for _, _, _, f in PARAMS:
            f(m, 0.999)
        m.inp.save(p1)
        s1 = 모의(p1, a.node).reindex(s0.index, method="nearest")
        k = kge(s0.values, s1.values)
        print("[매끄러움] %s  배수 1.0 대 0.999  KGE %.4f  (0.95 이상이어야 한다)"
              % (a.node, k))
        if not (k >= 0.95):
            print("[멈춤] 응답이 끊겨 있다. 펌프 · 수문 · 월류 같은 스위치 뒤의 지점이다.")
            print("       유입 수직구 앞 관로의 유량이나 연속 관측되는 수위를 고른다.")
            print("       그래도 이 지점으로 하려면 --강행")
            return 1

    setup = Setup(base, obs, a.node, work)
    db = os.path.join(work, "trials")
    alg = {"lhs": spotpy.algorithms.lhs, "mc": spotpy.algorithms.mc,
           "sceua": spotpy.algorithms.sceua, "dds": spotpy.algorithms.dds}[a.alg]
    sampler = alg(setup, dbname=db, dbformat="csv", save_sim=False)
    if a.alg == "sceua":
        sampler.sample(a.reps, ngs=max(2, len(PARAMS) + 1))
    else:
        sampler.sample(a.reps)

    res = pd.read_csv(db + ".csv")
    assert len(res) > 0, "시도 결과가 비었다"
    best = res.loc[res["like1"].idxmax()]
    print("\n[결과] 시도 %d 회" % len(res))
    for n, _, _, _ in PARAMS:
        print("  %-14s %.4f" % (n, best["par" + n]))
    print("  KGE            %.4f" % best["like1"])
    print("  기록           %s.csv" % db)
    if a.쌍둥이:
        err = max(abs(best["par" + n] - 1.0) for n, _, _, _ in PARAMS)
        print("  쌍둥이 판정    정답 1.0 과의 차이 %.4f" % err)
    return 0


if __name__ == "__main__":
    sys.exit(main())
