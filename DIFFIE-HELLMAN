# Diffie-Hellman
def primitive_root(p,g):
    lst=[]
    ran_ge=[i for i in range(1,p)]
    for i in range(p):
        root=(g**i)%p
        lst.append(root)
    if sorted(list(set(lst)))!=ran_ge:
        return 0
    else:
        return 1

def compute_public_key(xa,xb,p,g):
    return (g**xa)%p,(g**xb)%p
def shared_key(xa,xb,ya,yb,p):
    return (yb**xa)%p,(ya**xb)%p



p=int(input("Enter a prime number (p) : "))
while True:
    g=int(input("Enter a primitive root (g<p) : "))
    if primitive_root(p,g) ==1:
        break
    else:
        print(g, " is not a valid primitive root")
xa=int(input("Enter Private key of A (xa<p) : "))
xb=int(input("Enter Private key of B (xb<p): "))
ya,yb=compute_public_key(xa,xb,p,g)
print("A's Public key (ya): ",ya)
print("B's Public key (yb): ",yb)
ka,kb=shared_key(xa,xb,ya,yb,p)
if(ka==kb):
    print("Shared Secret key : ",ka)
