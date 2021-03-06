import sys

def read_dataset():
    return [list(map(int, line.strip().split())) for line in sys.stdin.readlines()]
    
class Graph():
    def __init__(self, edge_list):
        self.edge_list = edge_list
        self.num_nodes = edge_list[0][0]
        self.graph_impl = {}
        self.__build_graph()
    
    def get_degree_array(self):
        return [len(self.graph_impl[x + 1]) for x in range(self.num_nodes)]
        
    def __build_graph(self):
        for node in range(self.num_nodes):
            self.graph_impl[node + 1] = []
        for x, y in self.edge_list[1:]:
            self.graph_impl[x].append(y)
            self.graph_impl[y].append(x)
        
def main():
    edge_list = read_dataset()
    graph = Graph(edge_list)
    print(' '.join(map(str, graph.get_degree_array())))
    
if __name__ == '__main__':
    sys.exit(main())
