# Encrypted by kiansantang (hard)
# Time Encrypted: 2025-10-13 22:03:08

import base64, marshal, zlib, bz2, hashlib

_vpWMMAfVqW = [encoded hex payload]
_bPKNpbtKz = [9, 30, 28, 24, 17, 13, 7, 23, 20, 0, 27, 33, 26, 12, 5, 18, 1, 11, 10, 2, 14, 16, 8, 31, 4, 15, 29, 34, 21, 19, 32, 22, 3, 6, 25]

_ngwkMSbfs = [
    '408fffb3dc9b1f996ab30ec',
    '3f20e52ea4',
    'e39f362',
    'b1d048bc629e0cdf5',
    'f',
    'e20',
    '031',
]
_BcoVPeCS = [3, 2, 6, 1, 5, 4, 0]

def _QtqtBTMxKo(x):
    s = 0
    for ch in x:
        s = ((s << 5) - s) ^ (ord(ch) & 0xFF)
    return s & 0xFFFF

def _NqNlGHnkP(lst, order):
    out = []
    inv = [0] * len(order)
    for j, pj in enumerate(order):
        inv[pj] = j
    for i in range(len(inv)):
        out.append(lst[inv[i]])
    return ''.join(out)


def _ijpPJMDHXl(hexs):
    b = bytearray()
    for i in range(0, len(hexs), 256):
        b.extend(bytes.fromhex(hexs[i:i+256]))
    return bytes(b)


def _LnBKcPKXUhUL():
    hexs = _NqNlGHnkP(_vpWMMAfVqW, _bPKNpbtKz)
    keyh = _NqNlGHnkP(_ngwkMSbfs, _BcoVPeCS)
    D = _ijpPJMDHXl(hexs)
    K = _ijpPJMDHXl(keyh)
    if len(D) < 4:
        raise SystemExit('Corrupt payload')
    tail = D[-4:]; payload = D[:-4]
    if hashlib.sha256(payload).digest()[:4] != tail:
        raise SystemExit('Integrity failure')
    CH = 17
    L = len(payload); mv = payload
    parts = [mv[i:i+CH] for i in range(0, L, CH)]
    il = b''.join(p[::-1] for p in parts)
    n = len(il); n0 = (n+2)//3; n1 = (n+1)//3
    rev = bytearray(n)
    rev[::3] = il[:n0]
    rev[1::3] = il[n0:n0+n1]
    rev[2::3] = il[n0+n1:]
    X = bytes(rev)[::-1]
    KS = _kstream(len(X), K)
    b85 = bytes(a^b for a,b in zip(X, KS))
    c2 = base64.b85decode(b85)
    c1 = bz2.decompress(c2)
    raw = zlib.decompress(c1)
    co = marshal.loads(raw)
    globals()['__name__']='__main__'
    exec(co, globals())


def _kstream(n, seed):
    out = bytearray(); cur = seed
    while len(out) < n:
        cur = hashlib.sha256(cur).digest(); out.extend(cur)
    return bytes(out[:n])


if __name__ == '__main__':
    try:
        _LnBKcPKXUhUL()
    except Exception as e:
        import traceback; traceback.print_exc(); print('Runner v3 failed:', e)
