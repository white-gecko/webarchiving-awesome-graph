import pysparql_anything as sa
from pathlib import Path
from . import queries
from tempfile import NamedTemporaryFile
from os import remove


class ListParser:
    """The list parser reads an Awesome List in Markdown format with SparqlAnything and runs a set of SPARQL queries to extract a graph from it."""

    def __init__(self, file_path, base_iri):
        """Initialize the ListParser with a file path and base IRI.

        Args:
            file_path (str): Path to the markdown file
            base_iri (str): Base IRI for the generated resources
        """
        self.temp_file = None
        self.file_path = self.clean_list_file(Path(file_path))
        self.base_iri = base_iri
        self.engine = sa.SparqlAnything()

        self.any_graph = None
        self.everything = None
        self.awesome_concepts = None
        self.awesome_concept_taxonomy = None
        self.awesome_concept_descriptions = None
        self.awesome_items = None

    def __del__(self):
        """Clean up temporary files when the object is destroyed."""
        if self.temp_file:
            try:
                self.temp_file.close()
                remove(self.temp_file.name)
            except Exception:
                pass

    def clean_list_file(self, file_path: Path):
        """Filter out linter comments from the file.

        The list file (file_path) might contain lines with HTML comments for the linter (`<!--lint -->`).
        These lines need to be removed from the file, to maintain a syntax that can be interpreted correctly by SPARQL Anything.

        Args:
            file_path (Path): Path to the input file

        Returns:
            Path: Path to a temporary file with filtered content
        """
        # Read the content of the file
        with open(file_path, "r") as f:
            lines = f.readlines()

        # Filter out lines containing <!--lint -->
        filtered_lines = [
            line for line in lines if not line.strip().startswith("<!--lint")
        ]

        # Create a temporary file and write the filtered content
        self.temp_file = NamedTemporaryFile(suffix=".md", mode="w+", delete=False)
        self.temp_file.writelines(filtered_lines)
        self.temp_file.flush()
        self.temp_file.seek(0)

        return Path(self.temp_file.name)

    def parse(self):
        """Parse the markdown file into an RDF graph.

        Uses SPARQL Anything to construct an RDF graph from the markdown file.

        Returns:
            Graph: The parsed RDF graph
        """
        if not self.any_graph:
            self.any_graph = self.engine.construct(
                query=queries.spo(self.file_path.resolve())
            )
        return self.any_graph

    def get_readme_graph(self):
        """Get the complete README graph with concepts and projects.

        Combines concept taxonomy and project information into a single graph.

        Returns:
            Graph: The complete README graph
        """
        if not self.everything:
            self.everything = self.get_concepts() + self.get_projects()
            self.everything.update(queries.merge_blank_categories())
            self.everything.update(queries.identify_tools(self.base_iri))
        return self.everything

    def get_concept_taxonomy(self):
        """Extract concept taxonomy from the markdown file.

        Retrieves hierarchical relationships between concepts in the awesome list.

        Returns:
            Graph: The concept taxonomy graph
        """
        if not self.awesome_concept_taxonomy:
            self.awesome_concept_taxonomy = self.engine.construct(
                query=queries.concept_taxonomy(self.file_path.resolve(), self.base_iri)
            )
        return self.awesome_concept_taxonomy

    def get_concept_descriptions(self):
        """Extract concept descriptions from the markdown file.

        Retrieves textual descriptions for each concept in the awesome list.

        Returns:
            Graph: The concept descriptions graph
        """
        if not self.awesome_concept_descriptions:
            self.awesome_concept_descriptions = self.engine.construct(
                query=queries.concept_description(
                    self.file_path.resolve(), self.base_iri
                )
            )
        return self.awesome_concept_descriptions

    def get_concepts(self):
        """Get all concepts from the markdown file.

        Combines concept taxonomy and descriptions into a single concept graph.

        Returns:
            Graph: The combined concepts graph
        """
        if not self.awesome_concepts:
            self.awesome_concepts = (
                self.get_concept_taxonomy() + self.get_concept_descriptions()
            )
        return self.awesome_concepts

    def get_projects(self):
        """Extract project information from the markdown file.

        Retrieves project details including labels, descriptions, and categories.

        Returns:
            Graph: The projects graph
        """
        if not self.awesome_items:
            self.awesome_items = self.engine.construct(
                query=queries.awesome_items(self.file_path.resolve(), self.base_iri)
            )
        return self.awesome_items
