from collections import defaultdict
from top import find_articulation_points

# Fonction pour créer un graphe selon le choix utilisateur

def creer_graphe_par_choix(choix):
    """Retourne un graphe prédéfini selon le choix de l'utilisateur."""
    match choix:
        case '1':
            # Chaîne simple : 0-1-2-3-4
            return {
                0: [1],
                1: [0, 2],
                2: [1, 3],
                3: [2, 4],
                4: [3]
            }
        case '2':
            # Graphe avec un cycle et une branche
            return {
                0: [1, 2],
                1: [0, 2, 3],
                2: [0, 1, 3],
                3: [1, 2, 4],
                4: [3]
            }
        case '3':
            # Graphe simple en forme de V
            return {
                0: [1, 2],
                1: [0],
                2: [0]
            }
        case '4':
            # Graphe complètement connexe (triangle)
            return {
                0: [1, 2],
                1: [0, 2],
                2: [0, 1]
            }
        case '5':
            # Graphe déconnecté (deux composantes)
            return {
                0: [1],
                1: [0],
                2: [3],
                3: [2]
            }
        case '6':
            # Graphe en forme d'étoile
            return {
                0: [1, 2, 3],
                1: [0],
                2: [0],
                3: [0]
            }
        case '7':
            # Saisie manuelle
            print("Entrez votre graphe sous forme de dictionnaire , ex: {0: [1], 1: [0,2], 2: [1]}")
            user_input = input("Votre graphe : ")
            try:
                graphe = eval(user_input)
                if isinstance(graphe, dict):
                    return graphe
                else:
                    print("Format invalide.")
                    return None
            except Exception as e:
                print(f"Erreur de saisie : {e}")
                return None
        case _:
            return None

# --- Utilisation interactive ---
if __name__ == '__main__':
    
    print("Choisissez un modèle de graphe parmi les options suivantes :")
    print("1. Chaîne simple")
    print("2. Graphe avec un cycle et une branche")
    print("3. Graphe simple en forme de V")
    print("4. Graphe connexe (triangle)")
    print("5. Graphe déconnecté")
    print("6. Graphe en forme d'étoile")
    choix = input("Entrez votre choix (1-6) : ")

    while choix not in ["1", "2", "3", "4", "5", "6"]:
        choix = input("Choix invalide. Entrez une des valeurs [1,2,3,4,5,6] : ")
    graphe = creer_graphe_par_choix(choix)
    print(f"Graphe choisi : {graphe}")

    #gestion des erreurs (pour eviter les fautes de frappe)
    try:
        if choix not in ["1", "2", "3", "4", "5", "6",]:
            raise ValueError("Choix invalide, veuillez entrer une valeur de 1 à 6.")
    except ValueError as e:
        print(e)

    # Exemple d'utilisation de la fonction importée de top.py
    points = find_articulation_points(graphe)
    print(f"Points d'articulation : {points}")