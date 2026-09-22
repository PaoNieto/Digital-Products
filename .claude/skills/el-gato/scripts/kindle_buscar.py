# Amazon Kindle search -> titles, rating, number of ratings, price
# usage: python az.py "query" [domain: com|com.mx|es]  (default com)
import re, sys, subprocess, urllib.parse, html as H
q = sys.argv[1]
dom = sys.argv[2] if len(sys.argv) > 2 else 'com'
url = f'https://www.amazon.{dom}/s?k=' + urllib.parse.quote(q) + '&i=digital-text'
s = subprocess.run(['curl', '-sL', '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36', '-H', 'Accept-Language: es-ES,es;q=0.9', url], capture_output=True).stdout.decode('utf-8', 'ignore')
blocks = s.split('data-component-type="s-search-result"')[1:]
print(f'Q="{q}" amazon.{dom} results={len(blocks)}  {url}')
for b in blocks[:20]:
    t = re.search(r'<h2[^>]*aria-label="([^"]+)"', b) or re.search(r'<h2[^>]*>.*?<span[^>]*>([^<]+)</span>', b, re.S)
    r = re.search(r'([0-9][.,][0-9]) de 5 estrellas|([0-9][.,][0-9]) out of 5 stars', b)
    n = re.search(r'aria-label="([0-9.,]+) (calificaciones|ratings|valoraciones)', b) or re.search(r'>\(([0-9.,KkMm]+)\)<', b)
    p = re.search(r'<span class="a-offscreen">([^<]+)</span>', b)
    asin = re.search(r'data-asin="([A-Z0-9]{10})"', 'data-asin="' + b[:400]) or re.search(r'/dp/([A-Z0-9]{10})', b)
    bs = ' [BEST SELLER]' if ('Best Seller' in b or 'Más vendido' in b or 'M&aacute;s vendido' in b) else ''
    print('-', H.unescape(t.group(1) if t else '?')[:95], '|', (r.group(0) if r else 'sin estrellas'), '|', (n.group(1) + ' calif.' if n else '0 calif. visibles'), '|', (p.group(1) if p else 'precio no visible'), bs, '|', f'https://www.amazon.{dom}/dp/' + asin.group(1) if asin else '')
