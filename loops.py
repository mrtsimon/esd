def multiplie(a, b):
    rsst = 0

    for i in range(b):
        rst += a

    return resultat

# Exemple d'utilisation de la fonction multiplie
x = int(input("Saisissez une première valeur: "))
y = int(input("Saisissez une seconde valeur: "))
produit = multiplie(x, y)
print("Le résultat de la multiplication est :", x, "*", y, "=", produit)




# puissance

def puissance(base, exposant):
    rst2 = 1

    for _ in range(exposant):
        rst2 *= base

    return rst2

base = int(input("Entrez la base "))
exposant = int(input("Entrez l'exposant "))
rst2 = puissance(base, exposant)
print("Le résultat est :", base, "^", exposant, "=", resultat)
