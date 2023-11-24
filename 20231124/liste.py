def tri_selection(liste):
    """Trie la liste en utilisant l'algorithme de tri par sélection"""
    for i in range(len(liste)):
        min_index = i
        for j in range(i+1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

import random

# Génère une liste de 10 entiers aléatoires
liste = random.sample(range(100), 10)
print("Liste initiale: ", liste)

# Trie la liste en utilisant le tri par bulle
liste_triee_bulle = tri_bulle(liste.copy())
print("Liste triée par bulle: ", liste_triee_bulle)

# Trie la liste en utilisant le tri par sélection
liste_triee_selection = tri_selection(liste.copy())
print("Liste triée par sélection: ", liste_triee_selection)