def calculer_imc(taille, poids):
    """Calcule la valeur de l'IMC à partir de la taille et du poids"""
    return poids / (taille ** 2)

def classer_imc(imc):
    """Détermine la classe d'IMC à partir de la valeur de l'IMC"""
    if imc < 18.5:
        classe = "Maigreur"
    elif imc < 25:
        classe = "IMC normal"
    elif imc < 30:
        classe = "Surpoids"
    else:
        classe = "Obésité"
    return classe

def tri_selection(liste):
    """Trie la liste en utilisant l'algorithme de tri par sélection"""
    for i in range(len(liste)):
        min_index = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

def tri_bulle(liste):
    """Trie la liste en utilisant l'algorithme de tri par bulle"""
    for i in range(len(liste)):
        for j in range(len(liste) - i - 1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# Exemple d'utilisation
taille = float(input("Entrez votre taille (en mètres): "))
poids = float(input("Entrez votre poids (en kilogrammes): "))
imc = calculer_imc(taille, poids)
print("IMC:", imc)
classe = classer_imc(imc)
print("Classe d'IMC:", classe)

liste = list(map(int, input("Entrez une liste d'entiers, séparés par des espaces: ").split()))
print("Liste originale:", liste)
liste_triee_selection = tri_selection(liste)
print("Liste triée par sélection:", liste_triee_selection)
liste_triee_bulle = tri_bulle(liste)
print("Liste triée par bulle:", liste_triee_bulle)