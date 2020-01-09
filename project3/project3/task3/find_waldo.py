#!/usr/bin/python
import json, sys, hashlib
from fractions import gcd


def usage():
    print """Usage:
    python find_waldo.py student_id (i.e., qchenxiong3)"""
    sys.exit(1)

#TODO -- n1 and n2 share p or q?
def is_waldo(n1, n2):
    result = False

    q=0
    p=0

    if gcd(n1, n2) != 1:
        result = True

    return result

#TODO -- get private key of n1
def get_private_key(n1, n2, e):
    d = 0

    #your code starts here
    if gcd(n1, n2) != 1:
        p1 = gcd(n1, n2)
        q1 = n1 / p1

    totientN = (p1 - 1) * (q1 - 1)

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

    d = modinv(e, totientN)

    #your code ends here

    return d

def main():
    if len(sys.argv) != 2:
        usage()

    all_keys = None
    with open("keys.json", 'r') as f:
        all_keys = json.load(f)

    name = hashlib.sha224(sys.argv[1].strip()).hexdigest()
    if name not in all_keys:
        print sys.argv[1], "not in keylist"
        usage()

    pub_key = all_keys[name]
    n1 = int(pub_key['N'], 16)
    e = int(pub_key['e'], 16)
    d = 0
    waldo = "dolores"

    print "your public key: (", hex(n1).rstrip("L"), ",", hex(e).rstrip("L"), ")"

    for classmate in all_keys:
        if classmate == name:
            continue
        n2 = int(all_keys[classmate]['N'], 16)

        if is_waldo(n1, n2):
            waldo = classmate
            d = get_private_key(n1, n2, e)
            break
    
    print "your private key: ", hex(d).rstrip("L")
    print "your waldo: ", waldo


if __name__ == "__main__":
    main()
