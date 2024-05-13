from rdflib import Graph, URIRef


class GraphGeneration:
    def __init__(self, graph: Graph = None, base_iri: URIRef = None):
        self.graph = graph
        if self.graph is None:
            self.graph = Graph()

    def category(self, elem):
        print(header.identifier)
        self.graph.add()

    def entry(self, elem, category = None):
        print(header.identifier)
        self.graph.add()
