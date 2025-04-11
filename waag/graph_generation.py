from rdflib import Graph, URIRef
from gitdoap import doapit
from pathlib import Path
from .list_parser import ListParser
from . import queries


def call_and_write(callable, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    graph = callable()
    with open(path, mode="wb") as file:
        print(f"Write out to: {path}", end="...")
        graph.serialize(destination=file, format="turtle")
        print("done")


class GraphGeneration:
    def __init__(self, graph: Graph = None, base_iri: URIRef = None):
        self.base_iri = base_iri
        self.graph = graph
        if self.graph is None:
            self.graph = Graph()
        self.parser = None
        self.doap_graph = None

    def fetch_doap(self):
        if not self.doap_graph:
            self.doap_graph = Graph()
            for project in self.projects():
                doap = doapit(project)
                if doap:
                    self.doap_graph += doap
        return self.doap_graph

    def projects(self) -> list[URIRef]:
        """Get all projects IRIs"""
        for row in self.graph.query(queries.list_projects()):
            yield row.project

    def write_to_graph(self, graph_path: Path):
        with open(graph_path, mode="wb") as file:
            print(f"Write out to: {graph_path}", end="...")
            self.graph.serialize(destination=file, format="turtle")
            print("done")

    def init_from_readme(self, readme: Path):
        if not self.parser:
            self.parser = ListParser(readme, self.base_iri)
        self.parser.parse()
        self.graph += self.parser.get_readme_graph()

    def init_from_dir(self, output_dir: Path):
        readme = output_dir / "readme.ttl"
        doap = output_dir / "doap.ttl"
        if readme.exists():
            self.graph = Graph()
            self.graph.parse(readme)
        if doap.exists():
            self.doap_graph = Graph()
            self.doap_graph.parse(doap)

    def get_awesome_graph(self):
        return self.graph + self.doap_graph

    def store_to_dir(self, readme: Path, output_dir: Path):
        if not self.parser:
            self.parser = ListParser(readme, self.base_iri)

        call_and_write(self.parser.parse, output_dir / "any.ttl")
        call_and_write(self.parser.get_readme_graph, output_dir / "readme.ttl")
        call_and_write(self.fetch_doap, output_dir / "doap.ttl")
        call_and_write(self.get_awesome_graph, output_dir / "awesome.ttl")
