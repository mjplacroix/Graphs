class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)



def earliest_ancestor(ancestors, starting_node):
    ## using the graph class
    graph = Graph()

    ## build a dictionary of all the connections
    for connection in ancestors:
        graph.add_vertex(connection[1])

    for connection in ancestors:
        graph.add_edge(connection[1], connection[0])

    print("----------------------------------------------------")
    print(graph.vertices)
    ## search dictionary/graph for all possible paths to earliest ancestor

    ## empty set to store the paths (set of lists)
    paths = []
    visited_paths = []

    visited_paths.append([starting_node])
    ## if starting node is stored as a key
    while len(visited_paths) > 0:
        current_path = visited_paths.pop(0)
        current_node = current_path[-1]
        print(current_node)
        if current_node in graph.vertices:
            for parent in graph.vertices[current_node]:
                ## append each value to copy of starting node as a new_path
                new_path = []
                new_path.append(current_path)
                ## append each new_path to the paths set() & end of list
                new_path.append(parent)
                paths.append(new_path)
                visited_paths.append(new_path)
                # current_node = visited_paths.pop(0)[-1]
            

    print(paths)
    if len(paths) == 0:
        return -1
    longest = max([len(i) for i in paths])
    plist = [] 
    for path in paths:
        if len(path) == longest:
            plist.append(path)
    
    oldest = []
    for path in plist:
        oldest.append(path[-1])
    
    return max(oldest)







    ## reset each as a current_node and traverse accordingly
    ## search each new value - key/value pair

    
    ## if current path not in set
    ## add to set
    ## get max length list
    ## if more than one
        ## compare parents - take smaller one
    ## return parent
