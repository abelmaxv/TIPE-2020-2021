import random

def expo_rap(m,e,n):
    """Algorithme d'expodentitaion rapide m^e [n]"""
    p = 1
    while e>0:
        if e%2 == 1:
            p = (p*m)%n
        m=(m*m)%n
        e=e//2
    return p



def euclide_etendu(a,b):
    """renvoit le pgcd de a et b ainsi que les coefficients
     de la relation de Bézout correspondante"""   
    r,u,v,r2,u2,v2 = a,1,0,b,0,1
    while r2 != 0: 
        q = r//r2
        r, u ,v,r2,u2,v2 = r2,u2,v2,(r-q*r2),(u-q*u2),(v-q*v2)
    return (r,u,v)

def creer_clefs(p,q):
    """Renvoie une clef publique et une clef privée à partire des 
    nombres premiers p et q"""
    n = p*q
    phi = (p-1)*(q-1)
    e = phi
    r,d = euclide_etendu(e, phi)[0:2]
    while r !=1:
        e = random.randint(2, phi)
        r,d = euclide_etendu(e, phi)[0:2]   
    return (e,n) , (d%phi,n)

def chiffrement (m,e,n):
    """Chiffrement d'un message m avec une clef (e,n)"""
    return expo_rap(m,e,n)

def dechiffrement(c,d,n):
    """Dechiffrement d'un message c avec la clef privée (d,n)"""
    return expo_rap(c,d,n)

def int_to_string(n):
    """Conversion d'un entier en une chaine de caractère pour l'exemple"""
    s = ""
    while n!= 0:
        r = n%100
        n= n//100
        if r == 0: r = "0"
        elif r == 1 : r = "1"
        elif r ==2 : r = "2"
        elif r ==3 : r = "3"
        elif r ==4 : r = "4"
        elif r ==5 : r = "5"
        elif r ==6 : r = "6"
        elif r ==7 : r = "7"
        elif r ==8 : r = "8"
        elif r ==9 : r = "9"
        elif r ==10 : r = "A"
        elif r ==11 : r = "B"
        elif r ==12 : r = "C"
        elif r ==13 : r = "D"
        elif r ==14 : r = "E"
        elif r ==15 : r = "F"
        elif r ==16 : r = "G"
        elif r ==17 : r = "H"
        elif r ==18 : r = "I"
        elif r ==19 : r = "J"
        elif r ==20 : r = "K"
        elif r ==21 : r = "L"
        elif r ==22 : r = "M"
        elif r ==23 : r = "N"
        elif r ==24 : r = "O"
        elif r ==25 : r = "P"
        elif r ==26 : r = "Q"
        elif r ==27 : r = "R"
        elif r ==28 : r = "S"
        elif r ==29 : r = "T"
        elif r ==30 : r = "U"
        elif r ==31 : r = "V"
        elif r ==32 : r = "W"
        elif r ==33 : r = "X"
        elif r ==35 : r = "Y"
        elif r == 36 : r = "Z"
        elif r ==37 : r = " "

        s= r+s
    return s

# p = 2147483647
# q = 2305843009213693951
# pub = (1577853571334153130409925987, 4951760154835678088235319297)
# priv = (96685962259908502466291123, 4951760154835678088235319297)
# entier chiffré : 2374117310055482034146695634


    
