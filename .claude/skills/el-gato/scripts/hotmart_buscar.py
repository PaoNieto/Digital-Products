# Hotmart marketplace search -> products with reviews/date
import re, json, sys, subprocess, urllib.parse
q = sys.argv[1]
allang = len(sys.argv) > 2 and sys.argv[2] == 'all'
url = 'https://hotmart.com/es/marketplace/productos?q=' + urllib.parse.quote(q)
html = subprocess.run(['curl', '-sL', '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36', url], capture_output=True).stdout.decode('utf-8', 'ignore')
m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
if not m:
    print('NO DATA'); sys.exit()
d = json.loads(m.group(1))
res = d['props']['pageProps'].get('resultsData', {}).get('requestData', {}).get('results', [])
print(f'Q="{q}" results={len(res)}')
for r in res:
    if not allang and r.get('language') != 'ES':
        continue
    loc = 'es' if r.get('language') == 'ES' else 'pt-br'
    base = 'productos' if loc == 'es' else 'produtos'
    u = f"https://hotmart.com/{loc}/marketplace/{base}/{r['slug']}/{r['producerReferenceCode']}"
    print(f"- {r['title'][:70]} | {str(r.get('ownerName',''))[:30]} | {r.get('language')} | rev={r.get('totalReviews')} rat={round(r.get('rating') or 0,1)} | desde {str(r.get('ingressDate'))[:10]} | fmt={r.get('format')} | {u}")
