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
            for _, project in self.projects():
                doap = doapit(project)
                if doap:
                    self.doap_graph += doap
        return self.doap_graph

    def projects(self) -> list[URIRef]:
        """Get all projects.
        Yields a tuple of a project's subject IRI and optionally the respective URL of the project on an online platform (like GitHub)."""
        for row in self.graph.query(queries.list_projects()):
            yield row.project, row.platform_project

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
        for project, platform_project in self.projects():
            self.rename_resource(self.doap_graph, platform_project, project)
        return self.graph + self.doap_graph

    def store_to_dir(self, readme: Path, output_dir: Path):
        if not self.parser:
            self.parser = ListParser(readme, self.base_iri)

        call_and_write(self.parser.parse, output_dir / "any.ttl")
        call_and_write(self.parser.get_readme_graph, output_dir / "readme.ttl")
        call_and_write(self.fetch_doap, output_dir / "doap.ttl")
        call_and_write(self.get_awesome_graph, output_dir / "awesome.ttl")

    def rename_resource(self, graph: Graph, resource_from: URIRef, resource_to: URIRef):
        """Move all triples from a subject `resource_from` to a new subject `resource_to`.
        This will merge all triples ?s_from ?p ?o with ?s_to ?p ?o to ?s_to ?p ?o .

        This method will alter the provided graph."""

        for resource_from, p, o in graph.triples((resource_from, None, None)):
            graph.add((resource_to, p, o))
            graph.remove((resource_from, p, o))

        return graph
