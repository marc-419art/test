 # pour le cas de l'utilisateur qui veut proposer un graphe 
case '7':
            # Saisie manuelle
            print("Entrez votre graphe sous forme de dictionnaire Python, ex: {0: [1], 1: [0,2], 2: [1]}")
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

# a mettre apres la selection du choix 
while choix not in [str(i) for i in range(1, 8)]:
        choix = input("Choix invalide. Entrez une des valeurs [1,2,3,4,5,6,7] : ")
    graphe = creer_graphe_par_choix(choix)
    if graphe:
        print(f\"Graphe choisi : {graphe}\")
        points = find_articulation_points(graphe)
        print(f\"Points d'articulation : {points}\")
    else:
        print(\"Aucun graphe valide fourni.\")


  # a ajouter direct dans la match case
# le fichier principale avec les fonctions pour initialiser le projet 
 # c'est le fichier top. Et le fichier input sert a demarer le projet (no graphique mode!!!)


 