# Exercice 1 : Manipulation de Listes

liste_de_nombres = [5, 1, 9, 3]
liste_de_nombres.append(7)
liste_de_nombres.append(4)
liste_de_nombres.sort()
print(liste_de_nombres)

# Exercice 2 : Gestion d'un Dictionnaire

personne = {
    "nom": "Dupont",
    "âge": 35,
    "adresse": "12 rue de la Paix, Paris"
}

print(personne)

# Exercice 3 : Opérations sur les Ensembles

ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

print("Union :", ensemble1.union(ensemble2))
print("Intersection :", ensemble1.intersection(ensemble2))
