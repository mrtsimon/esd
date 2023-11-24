# Convertisseur Température
temp = float(input("Veuillez entrer une température : "))
unit = str(input("Veuillez entrer une unité : "))

def convertir_temp(temp, unit):
    if unit == "C":
        return (temp * 9/5) + 32
    elif unit == "F":
        return (temp - 32) * 5/9
    else:
        print("Unité invalide.")
        return None

resultat = convertir_temp(temp, unit)
print(resultat)