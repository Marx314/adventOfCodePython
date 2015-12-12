import networkx as nx
from networkx import shortest_path_length
from src.InputFetcher import InputFetcher


class Day9:

    def __init__(self):
        pass

    def calc(self, instructions):
        print instructions
        return
        graph = nx.Graph()
        for instruction in instructions:
            result = instruction.split(' ')
            graph.add_node(result[0])
            graph.add_node(result[2])
            graph.add_edge(result[0], result[2], weight=int(result[4]))
            graph.add_edge(result[2], result[0], weight=int(result[4]))

        #paths = shortest_path_length(graph, weight="weight")
        #print paths
        paths = nx.johnson(graph, weight='weight')
        #paths = nx.johnson(graph, weight='weight')
        print paths

        length = 100000000
        for source, path in paths.iteritems():
            print "city : {0} length {1}".format(source, 0)
            print path


        return length

    @staticmethod
    def run():
        data = InputFetcher.fetch_input(9).split('\n')
        day = Day9()
        print data
        print day.calc(data)



Day9.run()
