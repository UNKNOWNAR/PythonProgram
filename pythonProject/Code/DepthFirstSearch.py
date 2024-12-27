class DepthFirstSearch:
    def DFS(self,graph, visited, i):
        # Mark the current node as visited
        visited[i] = True
        # Traverse all adjacent nodes
        for j in range(len(graph[i])):  # Iterate over columns (adjacent nodes)
            if graph[i][j] == 1 and not visited.get(j, False):
                visited = self.DFS(graph, visited, j)
        return visited
if __name__=="__main__":
    graph = [
        [0, 1, 0, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0]
    ]
    visited = {}  # Initially, no nodes are visited
    start_node = 0  # Start DFS from node 0
    graphSearch = DepthFirstSearch()
    visited = graphSearch.DFS(graph,visited,start_node)
    print(visited)