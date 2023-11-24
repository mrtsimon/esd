import json
import os

# Charger les contacts depuis un fichier s'ils existent
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}

while True:
    action = input("Voulez-vous ajouter, supprimer, rechercher, ou quitter? ")
    
    if action == "ajouter":
        nom = input("Entrez le nom du contact: ")
        numero = input("Entrez le numéro de téléphone du contact: ")
        contacts[nom] = numero
        contacts.append(nom)
    elif action == "supprimer":
        nom = input("Entrez le nom du contact à supprimer: ")
        if nom in contacts:
            del contacts[nom]
        else:
            print("Ce contact n'existe pas.")
    elif action == "rechercher" or "r":
        nom = input("Entrez le nom du contact à rechercher: ")
        # Recherche en ignorant la casse
        nom = nom.lower()
        found_contacts = [contact for contact in contacts.keys() if contact.lower() == nom]
        if found_contacts:
            for contact in found_contacts:
                print("Le numéro de téléphone de", contact, "est", contacts[contact])
        else:
            print("Ce contact n'existe pas.")
    elif action == "quitter":

        if os.path.exists("contacts.json"):
            # Charger les contacts depuis le fichier existant
            with open("contacts.json", "r") as file:
                existing_contacts = json.load(file)
            
            # Mettre à jour les contacts existants avec les nouveaux contacts
            existing_contacts.update(contacts)
            contacts = existing_contacts

        # Sauvegarder les contacts dans un fichier
        with open("contacts.json", "w") as file:
            json.dump(contacts, file)
    else:
        print("Action invalide.")

