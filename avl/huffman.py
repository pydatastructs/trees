# -*- Mode: Python -*-

from . import avl

def analyze_file (filename):
    data = open(filename).read()
    f = {}
    for ch in data:
        if f.has_key (ch):
            f[ch] = f[ch] + 1
        else:
            f[ch] = 1
    f = f.items()
    f = map (lambda x: (x[1],x[0]), f)
    return f

def huffman_tree (f):
    t = avl.newavl (f)
    while len(t) > 1:
        w1,c1 = n1 = t[0]
        w2,c2 = n2 = t[1]
        t.remove(n1)
        t.remove(n2)
        t.insert (((w1+w2),(c1,c2)))
    return t[0]

def walk (r, t, s=''):
    if type(t) is type(''):
        r.append ((s, t))
    else:
        walk (r, t[0], s+'0')
        walk (r, t[1], s+'1')

def huffman_code (t):
    r = []
    walk (r, t[1])
    r = map (lambda x: (len(x[0]), x), r)
    r.sort()
    return map (lambda x: x[1], r)

if __name__ == '__main__':
    import sys
    code = huffman_code (huffman_tree (analyze_file (sys.argv[1])))
    for s, ch in code:
        print '%08s %s' % (repr(ch),s)
