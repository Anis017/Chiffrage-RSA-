#RSA Signature Implementation
#Realisation de la fonction qui realise la Devision Eclidienne
def euclid(m, n):
    if n == 0:
        return m
    else:
        r = m % n    #m modulo (le reste de la devision) avec n
        return euclid(n, r)
    
    

#calcul du PGCD
def exteuclid(a, b):
    r1 = a
    r2 = b
    s1 = int(1)
    s2 = int(0)
    t1 = int(0)
    t2 = int(1)

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if t1 < 0:
        t1 = t1 % a

    return (r1, t1)



#Le protocole RSA
p = 7  #P nombre Premier Privees propre au Recepteur
q = 117  #q nombre premier Privees propre au recepteur
n = p * q   #Calcul De n qui est rendu publique et recuperee par l'emetter
Pn = (p - 1) * (q - 1)  #Calcul de Pn par le recepteur



#Calculer La clef "e" publique par le Recepteur
#On verifie si cette cle est premier avec pn
key = []
for i in range(2, Pn):
    gcd = euclid(Pn, i)
#verifer si pgcd (e,pn) egale a 1
    #Afin que la Cle e ne soit pas un facteur de Pn
    # On verifie si cette cle est premier avec pn
    if gcd == 1:
        key.append(i) #???





#Calcul De la cle Privee d
e = int(313)    #C'est le cle "e" qui verifie La condition De Pgcd egale A 1 avec le pn
r, d = exteuclid(Pn, e)
if r == 1:
    d = int(d)






#AFFICHAGE
    print("decryption key is: ", d)
else:
    print("Multiplicative inverse for\the given encryption key does not \exist. Choose a different encrytion key ")






#Chiffrement et dechiffrement Par le Recepteur et L'emetter
    M = 41   #Le Message que on veut envoyer
    S = (M ** d) % n   #Chiffrement par l'emetter /signature numérique en utilisant S = M ^ d mod n
    M1 = (S ** e) % n  #Dechiffrement par le recepteur



#AFFICHAGE  DU RESULTAT DU CHIFFREMENT ET DECHIFFREMENT DU RECEPTEUR ET DE L'EMETTEUR
    if M == M1:
        print("As M = M1, Accept the\
    message sent by the receiver ")
    else:
        print("As M not equal to M1,\
    Do not accept the message \
            sent by the receiver   ")
        #The Message is received By the receiver
