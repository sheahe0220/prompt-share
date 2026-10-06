"""
Why: publisher sites (Wiley, Elsevier, IWA) block scripted downloads, so full-text HTML is
     fetched in the Playwright browser and POSTed here to be saved into raw/.
Rerun: C:\\Users\\SGJEONG99\\anaconda3\\envs\\pyswmm\\python.exe -X utf8 s03_receiver.py   (runs until killed)
POST /save?name=<file> with the body -> raw/<file>
"""
import os, re
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")
os.makedirs(RAW, exist_ok=True)

class H(BaseHTTPRequestHandler):
    def do_POST(self):
        q = parse_qs(urlparse(self.path).query)
        name = re.sub(r"[^A-Za-z0-9_.-]", "_", q.get("name", ["x"])[0])
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n)
        with open(os.path.join(RAW, name), "wb") as f:
            f.write(body)
        print("saved", name, len(body), flush=True)
        self.send_response(200); self.end_headers(); self.wfile.write(b"ok")

HTTPServer(("127.0.0.1", 8765), H).serve_forever()
