# Python program to find articulation points using a naive DFS approach (geekforgeeks.org)

def dfs(node, adj, visited):
    
    # Standard DFS to mark all reachable nodes
    visited[node] = True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited)

def constructadj(V, edges):
    
    # Builds adjacency list from edge list
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def get_components(V, adj, removed):
    visited = [False] * V
    visited[removed] = True
    components = []
    for i in range(V):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                comp.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            components.append(comp)
    return components

def articulationPoints(V, edges):
    # Finds articulation points using naive DFS approach
    adj = constructadj(V, edges)
    res = []

    # Try removing each node one by one
    for i in range(V):
        visited = [False] * V
        visited[i] = True 
        
        # count DFS calls from i's neighbors
        comp = 0  
        for it in adj[i]:
            if comp > 1:
                break 
            if not visited[it]:
                
                # explore connected part
                dfs(it, adj, visited)  
                comp += 1

        # if more than one component forms, it's an articulation point
        if comp > 1:
            res.append(i)

    if not res:
        print("Articulation points: [-1]")
        return [-1]
    
    print("Articulation points:", res)
    for ap in res:
        comps = get_components(V, adj, ap)
        print(f"Removing {ap} separates the graph into:")
        for c in comps:
            print("  ", c)

    return res

if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 4], [2, 3], [2, 4], [3, 4]]

    ans = articulationPoints(V, edges)
    for it in ans:
        print(it, end=" ")