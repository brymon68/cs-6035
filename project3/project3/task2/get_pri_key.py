#!/usr/bin/python
import json, sys, hashlib
import math

def usage():
    print """Usage:
        python get_pri_key.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)

# TODO -- get n's factors
# reminder: you can cheat ;-), as long as you can get p and q
def get_factors(n):

    p = 0
    q = 0

    for i in range(int(math.sqrt(n)), int(math.sqrt(n)-300000), -1):
        newvalue = n % i
        if newvalue ==0:
            p = i
            break
    q = n / p
    # your code ends here
    return (p, q)

# TODO: write code to get d from p, q and e
def get_key(p, q, e):
    d = 0

    ogn=(p*q)
    n=(p-1)*(q-1)

    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    d = modinv(e, n)

    return d

def main():
    if len(sys.argv) != 2:
        usage()

    n = 0
    e = 0

    all_keys = None
    with open("task2-keys.json", 'r') as f:
        all_keys = json.load(f)
    
    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()
    
    pub_key = all_keys[name]
    n = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)

    print "your public key: (", hex(n).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    (p, q) = get_factors(n)
    d = get_key(p, q, e)
    print "your private key:", hex(d).rstrip("L")

if __name__ == "__main__":
    main()
