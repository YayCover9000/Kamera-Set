#!/usr/bin/env python3
"""Liest jobs/suchen.txt, ruft Seite 1 je Suche von vinted.de ab und gibt Titel, Zustand, Preis, Link aus."""
import html, os, re, subprocess, sys, tempfile, time, urllib.parse

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
BASE = "https://www.vinted.de"
JAR = os.path.join(tempfile.gettempdir(), "vinted_jar")
HERE = os.path.dirname(os.path.abspath(__file__))


def get(url):
    r = subprocess.run(["curl", "-sS", "-c", JAR, "-b", JAR, "-A", UA, "-m", "40", "-w", "\n%{http_code}", url],
                       capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    return code, body


def fetch(url):
    for wait in (0, 6, 15, 30):  # Vinted (DataDome) blockt bei schnellen Abfragen zeitweise mit 403
        time.sleep(wait)
        code, body = get(url)
        if code == "200":
            return body
    return None


def main():
    for line in open(os.path.join(HERE, "suchen.txt"), encoding="utf-8"):
        if not line.strip() or line.startswith("#"):
            continue
        q, cat, flt = [p.strip() for p in (line.split("|") + ["", ""])[:3]]
        url = f"{BASE}/catalog?order=newest_first&catalog[]={cat or 3061}&search_text={urllib.parse.quote_plus(q)}"
        print(f"## {q}")
        time.sleep(8)  # Abstand zwischen Suchen, sonst blockt Vinted (DataDome)
        h = fetch(url)
        if h is None:
            print("FEHLER: Seite nicht abrufbar (403)")
            continue
        seen = set()
        for m in re.finditer(r'<img src="[^"]*" alt="([^"]*)"[^>]*data-testid="product-item-id-(\d+)--image--img"', h):
            alt, i = html.unescape(m.group(1)), m.group(2)
            if i in seen or len(seen) >= 20:
                continue
            seen.add(i)
            if flt and not re.search(flt, alt, re.I):
                continue
            lm = re.search(r'href="(/items/%s-[^"?]*)' % i, h)
            print(f"{alt} | {BASE}{lm.group(1) if lm else '/items/' + i}")
        print(f"({len(seen)} Treffer geladen)")


if __name__ == "__main__":
    sys.exit(main())
