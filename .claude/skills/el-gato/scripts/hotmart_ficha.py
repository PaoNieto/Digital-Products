# Hotmart product: marketplace profile + checkout price
import re, json, sys, subprocess
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'


def get(u):
    return subprocess.run(['curl', '-sL', '-A', UA, u], capture_output=True).stdout.decode('utf-8', 'ignore')


for url in sys.argv[1:]:
    print('=' * 20, url)
    html = get(url)
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        print('NO PROFILE DATA'); continue
    prof = json.loads(m.group(1))['props']['pageProps'].get('profile', {}) or {}
    p = prof.get('product', {}) or {}
    cr = prof.get('customerReview') or {}
    ds = p.get('dataSheet') or {}
    print('NAME:', p.get('name'), '| PRODUCER:', (p.get('hotmarter') or {}).get('name'), '| badgesProductor:', (p.get('hotmarter') or {}).get('activeBadges'))
    print('CREATED:', str(prof.get('createdAt'))[:10], '| ALUMNOS(totalUsers):', prof.get('totalUsers'), '| REVIEWS:', cr.get('totalReviews'), 'rating', cr.get('rating'), '| GARANTIA:', ds.get('warranty'), '| PAIS:', p.get('targetCountry'), '| FORMATO:', p.get('format'))
    print('COPY:', (p.get('copy') or '').replace('\n', ' ')[:450])
    print('VENTAJAS:', (p.get('advantages') or '').replace('\n', ' ')[:350])
    code = p.get('producerReferenceCode'); off = p.get('offer')
    c = get(f'https://pay.hotmart.com/{code}?off={off}') if code else ''
    m2 = re.search(r'id="__NUXT_DATA__"[^>]*>(.*?)</script>', c, re.S)
    if not m2:
        print('CHECKOUT: no data'); continue
    arr = json.loads(m2.group(1))

    def res(x, depth=0):
        if not isinstance(x, int) or isinstance(x, bool):
            return x
        if depth > 6:
            return '..'
        v = arr[x]
        if isinstance(v, dict):
            return {k: res(y, depth + 1) for k, y in v.items()}
        if isinstance(v, list):
            if v and v[0] in ('Reactive', 'ShallowReactive', 'Ref', 'ShallowRef', 'EmptyRef'):
                return res(v[1], depth + 1) if len(v) > 1 else None
            return [res(y, depth + 1) for y in v][:8]
        return v

    out = {}
    for v in arr:
        if isinstance(v, dict):
            if 'baseValue' in v:
                out['base'] = (res(v['baseValue']), res(v.get('baseCurrency')), res(v.get('convertedValue')), res(v.get('convertedCurrency')))
            if 'paymentPlans' in v:
                out['plans'] = res(v['paymentPlans'])
            if 'warrantyDays' in v:
                out['warranty'] = res(v['warrantyDays'])
    fa = [res(v['fullAmount']) for v in arr if isinstance(v, dict) and 'fullAmount' in v]
    print('CHECKOUT base(valor,moneda,convertido,moneda):', out.get('base'), '| 1 pago:', fa[0] if fa else None, '| planes:', json.dumps(out.get('plans'), ensure_ascii=False)[:200], '| garantia:', out.get('warranty'))
    names = set()
    for v in arr:
        if isinstance(v, dict) and 'name' in v and ('ucode' in v or 'productId' in v or 'offer' in v):
            n = res(v['name'])
            if isinstance(n, str):
                names.add(n)
    print('PRODUCTOS EN CHECKOUT:', list(names)[:8])
