from collections import defaultdict

def find_articulation_points(graph):
    """
    Trouve les points d'articulation dans un graphe non orienté en utilisant l'algorithme DFS.

    Args:
        graph (dict): Un dictionnaire représentant le graphe.
                      Les clés sont les sommets et les valeurs sont des listes d'adjacence.
                      Ex: {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}

    Returns:
        set: Un ensemble de points d'articulation dans le graphe.
    """

    # Initialisation des variables globales pour le DFS
    time = 0  # Compteur de temps pour disc et low
    disc = {}  # Temps de découverte de chaque sommet
    low = {}   # Plus petite valeur de temps de découverte atteignable
    parent = {} # Parent de chaque sommet dans l'arbre DFS
    is_articulation = set() # Ensemble des points d'articulation trouvés

    # Pour suivre les sommets visités pendant le DFS
    # Nous pourrions utiliser disc[u] == -1 comme indicateur, mais un set est plus explicite.
    visited = set()

    # Fonction DFS récursive
    def dfs(u):
        nonlocal time # Permet de modifier la variable 'time' de la portée extérieure
        visited.add(u)
        disc[u] = time
        low[u] = time
        time += 1
        children_count = 0 # Nombre d'enfants dans l'arbre DFS pour le sommet 'u'

        # Parcourt tous les voisins de 'u'
        for v in graph.get(u, []): # .get(u, []) gère les sommets sans arêtes
            if v == parent.get(u): # Si 'v' est le parent de 'u', on l'ignore
                continue

            if v in visited: # 'v' a déjà été visité, c'est une arête de retour
                low[u] = min(low[u], disc[v])
            else: # 'v' n'a pas été visité, c'est une arête d'arbre
                parent[v] = u # Définit 'u' comme parent de 'v'
                children_count += 1
                dfs(v) # Appel récursif pour 'v'

                # Après le retour de l'appel récursif, met à jour low[u]
                # 'u' peut potentiellement atteindre un ancêtre plus haut via 'v'
                low[u] = min(low[u], low[v])

                # Vérifie la condition du point d'articulation
                # Cas 1: 'u' est la racine de l'arbre DFS et a au moins deux enfants
                # La racine du DFS n'a pas de parent initial (parent[u] n'est pas défini ou est None/sentinelle)
                if parent.get(u) is None and children_count > 1:
                    is_articulation.add(u)
                # Cas 2: 'u' n'est pas la racine et low[v] >= disc[u]
                # Cela signifie que tout chemin de 'v' ou de son sous-arbre vers un ancêtre
                # doit passer par 'u' ou un de ses ancêtres, mais pas plus haut que 'u'
                elif parent.get(u) is not None and low[v] >= disc[u]:
                    is_articulation.add(u)

    # Itère sur tous les sommets pour s'assurer que tous les composants connexes sont parcourus
    for vertex in graph:
        if vertex not in visited:
            # Pour le premier sommet de chaque composante connexe, il n'y a pas de parent
            # On passe None comme parent initial pour la racine du DFS.
            parent[vertex] = None # Ou tout autre valeur pour indiquer que c'est une racine
            dfs(vertex)

    return is_articulation

# --- Exemples d'utilisation ---

print("--- Exemple 1: Chaîne simple ---")
# Graphe: 0-1-2-3-4
graph1 = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
}
# Points d'articulation attendus: {1, 2, 3}
print(f"Graphe 1: {graph1}")
print(f"Points d'articulation: {find_articulation_points(graph1)}")
# ---
# Explication: Si on retire 1, 0 est isolé de 2-3-4.
# Si on retire 2, 0-1 est isolé de 3-4.
# Si on retire 3, 0-1-2 est isolé de 4.


print("\n--- Exemple 2: Graphe avec un cycle et une branche ---")
# Graphe:
#   0 -- 1
#   |  / |
#   2 -- 3
#        |
#        4
graph2 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
}
# Points d'articulation attendus: {3}
print(f"Graphe 2: {graph2}")
print(f"Points d'articulation: {find_articulation_points(graph2)}")
# ---
# Explication: Seul 3 est un point d'articulation. Si on retire 3, le cycle 0-1-2 est déconnecté de 4.
# Les sommets 0, 1, 2 ne sont pas des points d'articulation car ils font partie d'un cycle.
# La suppression de l'un d'eux ne déconnecte pas le graphe.

print("\n--- Exemple 3: Graphe simple en forme de V ---")
# Graphe:
#   0 -- 1
#   |
#   2
graph3 = {
    0: [1, 2],
    1: [0],
    2: [0]
}
# Points d'articulation attendus: {0}
print(f"Graphe 3: {graph3}")
print(f"Points d'articulation: {find_articulation_points(graph3)}")
# ---
# Explication: Si on retire 0, 1 et 2 sont déconnectés l'un de l'autre.

print("\n--- Exemple 4: Graphe complètement connexe (aucun point d'articulation) ---")
# Graphe: 0-1-2-0 (triangle)
graph4 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
# Points d'articulation attendus: set() (vide)
print(f"Graphe 4: {graph4}")
print(f"Points d'articulation: {find_articulation_points(graph4)}")
# ---
# Explication: C'est un cycle. La suppression de n'importe quel sommet ne déconnecte pas le graphe.

print("\n--- Exemple 5: Graphe déconnecté (plusieurs composantes) ---")
# Graphe: 0-1 et 2-3
graph5 = {
    0: [1],
    1: [0],
    2: [3],
    3: [2]
}
# Points d'articulation attendus: set() (vide)
print(f"Graphe 5: {graph5}")
print(f"Points d'articulation: {find_articulation_points(graph5)}")
# ---
# Explication: Le graphe est déjà déconnecté. Les sommets 0, 1, 2, 3 ne sont pas des points d'articulation
# car leur suppression ne fait qu'isoler une partie d'une composante déjà existante, sans créer de nouvelle déconnexion.

print("\n--- Exemple 6: Graphe en forme d'étoile ---")
# Graphe:
#   1 -- 0 -- 2
#        |
#        3
graph6 = {
    0: [1, 2, 3],
    1: [0],
    2: [0],
    3: [0]
}
# Points d'articulation attendus: {0}
print(f"Graphe 6: {graph6}")
print(f"Points d'articulation: {find_articulation_points(graph6)}")
# ---
# Explication: Le sommet central 0 est un point d'articulation. Si on le supprime,
# les sommets 1, 2 et 3 deviennent isolés les uns des autres.