#Hill Cipher 

def detinv(a,m):
    for i in range(m):
        if (a*i)%m==1:
            return i

def det(k):
    d=(k[0][0]*k[1][1])-(k[0][1]*k[1][0])
    if d<0:
        d=d+26
        if d<0:
            return "Invalid Key!"
        else:
            return d
    elif d>26:
        return "Invalid Key!"
    elif d==0:
        return "Invalid Key >> Det = 0"
    else:
        return d

def adj(k):
    k_adj=[[0,0],[0,0]]
    k_adj[0][0]=k[1][1]
    k_adj[1][1]=k[0][0]
    k_adj[0][1]=-1*k[0][1]+26
    k_adj[1][0]=-1*k[1][0]+26
    return k_adj

def inverse(adj_k,Det):
    k_inv=[[0,0],[0,0]]
    k_inv[0][0]=(adj_k[0][0]*Det)%26
    k_inv[0][1]=(adj_k[0][1]*Det)%26
    k_inv[1][0]=(adj_k[1][0]*Det)%26
    k_inv[1][1]=(adj_k[1][1]*Det)%26
    return k_inv

def encryption(word,k):
    global alphabets
    p=[alphabets.index(i)for i in word]
    cipher=""
    cipher+=alphabets[(k[0][0]*p[0]+k[0][1]*p[1])%26]
    cipher+=alphabets[(k[1][0]*p[0]+k[1][1]*p[1])%26]
    return cipher.upper()

def decryption(word,k):
    global alphabets
    c = [alphabets.index(i) for i in word]
    plain = ""
    plain += alphabets[(k[0][0] * c[0] + k[0][1] * c[1]) % 26]
    plain += alphabets[(k[1][0] * c[0] + k[1][1] * c[1]) % 26]
    return plain


def key_matrix(k):
    key_matrix = []
    for i in range(0, len(k), 2):
        temp1 = k[i:i + 2]
        temp2 = []
        for j in temp1:
            temp2.append(alphabets.index(j))
        key_matrix.append(temp2)
    return key_matrix

def msg_split(msg):
    if len(msg) % 2 != 0: msg += "x"
    plaintext = [msg[i:i + 2] for i in range(0, len(msg), 2)]
    return plaintext

alphabets="abcdefghijklmnopqrstuvwxyz"

#main
while 1:
    print("\n***Hill Cipher***\n1.Encryption\n2.Decryption\n3.Exit")
    choice=int(input("Enter Operation(1/2/3) : "))
    if choice == 3:
        exit()

    key = input("Enter Key : ")
    key = key.lower()
    #k = key[0] + key[2] + key[1] + key[3]

    # Initializing Key Matrix
    key_mat = key_matrix(key)

    # Validating key
    if isinstance(det(key_mat),int):
        if choice==1:
            msg = input("Enter Message : ")
            msg = msg.replace(" ", "")
            msg=msg.lower()
            # Dividing Plain Text
            text = msg_split(msg)
            # Encryption

            cipher = [encryption(i, key_mat) for i in text]
            print("Encrypted Text : ")
            for i in cipher: print(i, end="")



        elif choice==2:
            msg = input("Enter Encrypted Message : ")
            msg = msg.replace(" ", "")
            msg=msg.lower()
            # Dividing Cipher Text
            text = msg_split(msg)
            # Decryption
            Det=det(key_mat)
            Det_inv=detinv(Det,26)

            adj_k=adj(key_mat)

            inv_k=inverse(adj_k,Det_inv)

            plain = [decryption(i, inv_k) for i in text]
            print("Decrypted Text : ")
            if plain[-1][1]=="x":
                s=""
                for i in plain:s+=i
                s=s.replace(s[-1],"")
                print(s)
            else:
                for i in plain:print(i,end="")

        else:
            print("Invalid Option")
    else:
        print(det(key_mat))
