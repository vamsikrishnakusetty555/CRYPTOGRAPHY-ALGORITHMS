# RSA Algorithm
def private_key(e,phi):
    i=1
    while True:
        if (e * i) % phi == 1:
            return i
        i += 1
def encrypt():
    global alphabets
    print("Private key : ",private_key(e,phi))
    msg=input("Enter Message : ")
    msg=msg.lower()
    msg=msg.replace(" ","")
    cipher=[]
    for i in msg:
        c=(alphabets.index(i)**e)%n
        cipher.append(c)
    print("Encrypted Text is ", end="")
    print(*cipher)

def decrypt():
    global n
    msg=list(map(int,input("Enter Encrypted text : ").split()))
    plain=[]
    plain_text=""
    d=int(input("Enter Private Key : "))
    for i in msg:
        p=(i**d)%n
        plain.append(p)
    for i in plain:
        plain_text+=alphabets[i]
    return plain_text

alphabets="abcdefghijklmnopqrstuvwxyz"
while 1:
    print("***RSA Algorithm***\n1.Encryption\n2.Decryption\n3.Exit")
    choice=int(input("Enter(1/2/3): "))
    if choice==1:
        p, q = map(int, input("Enter Two Large Prime Numbers : ").split())
        n = p * q
        phi = (p - 1) * (q - 1)
        print("n : ",n)
        print("Totient function  : ",phi)
        while True:
            e = int(input("Enter a valid Public Key : "))
            co_prime = 0
            if e < phi :
                for i in range(2, phi):
                    if phi % i == 0 and e % i == 0:
                        co_prime += 1
                if co_prime == 0:
                    break
                else:
                    print("Invalid Public Key!!")
            elif e>=phi or e<=1:
                print("Invalid Public Key!! Range should be (1 < e < Totient function)")
        encrypt()
    elif choice==2:
        print(decrypt())
    elif choice==3:
        exit()
    else:
        print("Invalid Option!!")
