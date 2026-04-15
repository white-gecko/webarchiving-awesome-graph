from rdflib import Graph, URIRef
from gitdoap import doapit
from pathlib import Path
from .list_parser import ListParser
from . import queries


def call_and_write(callable, path, prefixes=None):
    """Serialize and write a graph to a file.

    This helper function takes a callable that returns a graph and writes it to a specified path.

    Args:
        callable: A function that returns an RDF graph
        path (Path): The file path where the graph should be serialized
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    graph = callable()
    with open(path, mode="wb") as file:
        print(f"Write out to: {path}", end="...")
        graph.serialize(destination=file, format="turtle", namespaces=prefixes)
        print("done")


class GraphGeneration:
    def __init__(self, graph: Graph = None, base_iri: URIRef = None):
        """Initialize the GraphGeneration object with optional graph and base IRI.

        Args:
            graph (Graph, optional): An RDF graph to initialize with.
            base_iri (URIRef, optional): The base IRI used for resolving relative IRIs.
        """
        self.base_iri = base_iri
        self.graph = graph
        if self.graph is None:
            self.graph = Graph()
        self.parser = None
        self.doap_graph = None
        self.prefixes = None


    def fetch_doap(self):
        """Fetch DOAP information for all projects.

        If the DOAP graph has not been fetched yet, this method retrieves DOAP data
        for each project using the `doapit` library and stores it in `self.doap_graph`.

        Returns:
            Graph: The DOAP graph containing information about projects.
        """
        if not self.doap_graph:
            self.doap_graph = Graph()
            for _, project in self.projects():
                doap = doapit(project)
                if doap:
                    self.doap_graph += doap
        return self.doap_graph

    def projects(self) -> list[URIRef]:
        """Get all projects from the graph.

        Queries the graph for project information and yields tuples of project IRIs
        and their associated platform project URLs (e.g. on GitHub).

        Yields:
            tuple[URIRef, URIRef]: A tuple containing the project IRI and its platform project URL.
        """
        for row in self.graph.query(queries.list_projects()):
            yield row.project, row.platform_project

    def write_to_graph(self, graph_path: Path):
        """Serialize and write the internal graph to a file.

        Args:
            graph_path (Path): The file path where the graph should be serialized.
        """
        with open(graph_path, mode="wb") as file:
            print(f"Write out to: {graph_path}", end="...")
            self.graph.serialize(destination=file, format="turtle")
            print("done")

    def init_from_readme(self, readme: Path):
        """Initialize the graph from a README file.

        Parses the README file and adds the resulting graph to the internal graph.

        Args:
            readme (Path): Path to the README file to parse.
        """
        if not self.parser:
            self.parser = ListParser(readme, self.base_iri)
        self.parser.parse()
        self.graph += self.parser.get_readme_graph()

    def init_from_dir(self, output_dir: Path):
        """Initialize the graph from previously saved files in a directory.

        Loads the README and DOAP graphs from disk if they exist.

        Args:
            output_dir (Path): Directory containing serialized graph files.
        """
        readme = output_dir / "readme.ttl"
        doap = output_dir / "doap.ttl"
        prefixes = output_dir / "prefixes.ttl"
        if readme.exists():
            self.graph = Graph()
            self.graph.parse(readme)
        if doap.exists():
            self.doap_graph = Graph()
            self.doap_graph.parse(doap)
        if prefixes.exists():
            self.prefixes_graph = Graph()
            self.prefixes_graph.parse(prefixes)
            self.prefixes = list(self.prefixes_graph.namespaces())

    def get_awesome_graph(self):
        """Merge the main graph with the DOAP graph.

        Renames resources in the DOAP graph to match those in the main graph,
        then combines both graphs into one.

        Returns:
            Graph: The merged graph combining the main and DOAP information.
        """
        for project, platform_project in self.projects():
            self.rename_resource(self.doap_graph, platform_project, project)
        return self.graph + self.doap_graph

    def store_to_dir(self, readme: Path, output_dir: Path):
        """Store all graphs to the specified directory.

        Parses the README, fetches DOAP data, and serializes all graphs to files.

        Args:
            readme (Path): Path to the README file to parse.
            output_dir (Path): Directory where the graphs will be stored.
        """
        if not self.parser:
            self.parser = ListParser(readme, self.base_iri)

        call_and_write(self.parser.parse, output_dir / "any.ttl", self.prefixes)
        call_and_write(self.parser.get_readme_graph, output_dir / "readme.ttl", self.prefixes)
        call_and_write(self.fetch_doap, output_dir / "doap.ttl", self.prefixes)
        call_and_write(self.get_awesome_graph, output_dir / "awesome.ttl", self.prefixes)

    def rename_resource(self, graph: Graph, resource_from: URIRef, resource_to: URIRef):
        """Rename a resource in a graph by moving all triples from one subject to another.

        This method moves all triples where the subject is `resource_from` to use
        `resource_to` as the subject instead. It modifies the graph in-place.
        This will merge all triples ?s_from ?p ?o and ?s_to ?p ?o.

        Args:
            graph (Graph): The RDF graph to modify.
            resource_from (URIRef): The original subject IRI.
            resource_to (URIRef): The new subject IRI.

        Returns:
            Graph: The modified graph with renamed resources.
        """
        for resource_from, p, o in graph.triples((resource_from, None, None)):
            graph.add((resource_to, p, o))
            graph.remove((resource_from, p, o))

        return graph
