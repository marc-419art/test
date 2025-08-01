def trouver_points_articulation(graphe):
    """
    Détecte les points d'articulation dans un graphe non orienté.

    Args:
        graphe (dict): Le graphe représenté comme un dictionnaire d'adjacence.
                       Ex: { 'A': ['B', 'D'], 'B': ['A', 'C', 'E'], ... }

    Returns:
        set: Un ensemble contenant les sommets qui sont des points d'articulation.
    """
    # Variables pour suivre l'état du parcours DFS et les propriétés des nœuds
    visite = set()          # Pour savoir quels nœuds ont déjà été visités
    temps_decouverte = {}   # 'disc[u]' : Moment où le nœud 'u' a été découvert
    plus_bas_ancetre = {}   # 'low[u]' : Le plus petit temps de découverte atteignable depuis 'u'
    parent = {}             # 'parent[u]' : Le parent de 'u' dans l'arbre DFS
    points_articulation = set() # L'ensemble où nous stockerons les points d'articulation trouvés
    temps_global = 0        # Un compteur de temps qui s'incrémente à chaque nouvelle découverte

    # --- Fonction DFS récursive ---
    def dfs_recursif(u):
        nonlocal temps_global # Permet de modifier la variable 'temps_global' définie en dehors de cette fonction

        # Marque le nœud 'u' comme visité
        visite.add(u)
        # Enregistre le temps de découverte et initialise le plus bas ancêtre atteignable
        temps_decouverte[u] = temps_global
        plus_bas_ancetre[u] = temps_global
        temps_global += 1

        compteur_enfants_dfs = 0 # Compte les enfants dans l'arbre DFS (utile pour la racine)

        # Parcours tous les voisins 'v' du nœud actuel 'u'
        for v in graphe.get(u, []):
            # Si 'v' est le parent de 'u' dans l'arbre DFS, on l'ignore
            if v == parent.get(u):
                continue

            # Si 'v' a déjà été visité (c'est une arête de retour)
            if v in visite:
                # Met à jour 'plus_bas_ancetre[u]' avec le temps de découverte de 'v'
                # (car 'u' peut atteindre 'v' qui est un ancêtre)
                plus_bas_ancetre[u] = min(plus_bas_ancetre[u], temps_decouverte[v])
            else:
                # Si 'v' n'a pas été visité (c'est une arête d'arbre)
                parent[v] = u # Définit 'u' comme parent de 'v'
                compteur_enfants_dfs += 1 # Incrémente le compteur d'enfants pour 'u'
                
                dfs_recursif(v) # Appel récursif pour explorer le sous-arbre de 'v'

                # Après le retour de l'appel récursif pour 'v' :
                # Met à jour 'plus_bas_ancetre[u]' avec le 'plus_bas_ancetre' de 'v'
                # (car 'u' peut atteindre tout ce que 'v' peut atteindre)
                plus_bas_ancetre[u] = min(plus_bas_ancetre[u], plus_bas_ancetre[v])

                # --- Condition de détection du point d'articulation ---
                # Si 'u' n'est PAS la racine de l'arbre DFS
                # ET si le sous-arbre de 'v' ne peut pas atteindre un ancêtre de 'u'
                # (ou 'u' lui-même) autrement qu'en passant par 'u'
                if parent.get(u) is not None and plus_bas_ancetre[v] >= temps_decouverte[u]:
                    points_articulation.add(u)
        
        # --- Cas spécial pour la racine de l'arbre DFS ---
        # Si 'u' est la racine de l'arbre DFS (n'a pas de parent)
        # ET si elle a plus d'un enfant dans l'arbre DFS
        if parent.get(u) is None and compteur_enfants_dfs > 1:
            points_articulation.add(u)

    # --- Boucle principale pour lancer le DFS sur toutes les composantes connexes ---
    for noeud_depart in graphe:
        if noeud_depart not in visite:
            parent[noeud_depart] = None # La racine n'a pas de parent
            dfs_recursif(noeud_depart)
            
    return points_articulation

# --- Partie pour interagir avec l'utilisateur ---
if __name__ == "__main__":
    print("--- Programme de Recherche de Points d'Articulation ---")
    print("Veuillez entrer les arêtes de votre graphe. Chaque arête relie deux sommets.")
    print("Utilisez des lettres ou des chiffres pour nommer vos sommets (ex: A B, 1 2).")
    print("Tapez 'FIN' ou 'DONE' quand vous avez terminé d'entrer les arêtes.")

    graphe_utilisateur = {} # Le graphe sera construit ici

    while True:
        entree_arete = input("Entrez une arête (ex: N1 N2) ou 'FIN' : ").strip().upper()

        if entree_arete in ('FIN', 'DONE'):
            break

        parties = entree_arete.split()
        if len(parties) != 2:
            print("Erreur : Entrée invalide. Veuillez entrer deux sommets séparés par un espace.")
            continue

        sommet1, sommet2 = parties[0], parties[1]

        # Ajoute l'arête dans les deux sens pour un graphe non orienté
        if sommet1 not in graphe_utilisateur:
            graphe_utilisateur[sommet1] = []
        graphe_utilisateur[sommet1].append(sommet2)

        if sommet2 not in graphe_utilisateur:
            graphe_utilisateur[sommet2] = []
        graphe_utilisateur[sommet2].append(sommet1)
    
    # Éliminer les doublons dans les listes d'adjacence au cas où l'utilisateur entre plusieurs fois la même arête
    for sommet in graphe_utilisateur:
        graphe_utilisateur[sommet] = list(set(graphe_utilisateur[sommet]))

    print("\n--- Graphe Saisi ---")
    if not graphe_utilisateur:
        print("Le graphe est vide.")
    else:
        # Affichage du graphe pour vérification
        for sommet, voisins in sorted(graphe_utilisateur.items()):
            print(f"{sommet}: {', '.join(sorted(voisins))}") # Trie aussi les voisins pour un affichage constant

    # Recherche et affichage des points d'articulation
    if not graphe_utilisateur:
        print("\nAucun point d'articulation dans un graphe vide.")
    else:
        resultats_points_articulation = trouver_points_articulation(graphe_utilisateur)

        print("\n--- Résultats des Points d'Articulation ---")
        if resultats_points_articulation:
            print("Les points d'articulation trouvés sont :")
            # Affichage trié pour une meilleure lisibilité
            for ap in sorted(list(resultats_points_articulation)):
                print(f"- {ap}")
            print("\nLa suppression de l'un de ces sommets déconnecterait des parties du graphe.")
        else:
            print("Ce graphe ne contient aucun point d'articulation. Il est 'biconnexe' (plus robuste).")