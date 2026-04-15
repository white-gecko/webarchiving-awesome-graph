import pysparql_anything as sa
from pathlib import Path
from . import queries
from tempfile import TemporaryFile


class ListParser:
    """The list parser reads an Awesome List in Markdown format with SparqlAnything and runs a set of SPARQL queries to extract a graph from it."""

    def __init__(self, file_path, base_iri):
        self.file_path = Path(file_path)
        self.base_iri = base_iri
        self.engine = sa.SparqlAnything()

        self.any_graph = None
        self.everything = None
        self.awesome_concepts = None
        self.awesome_concept_taxonomy = None
        self.awesome_concept_descriptions = None
        self.awesome_items = None
        self.temp_file = None

    def __del__(self):
        if hasattr(self, 'temp_file'):
            try:
                self.temp_file.close()
            except Exception:
                pass

    def clean_list_file(self, file_path: Path):
        """Filter out linter comments from the file.
        The list file (file_path) might contain lines with HTML comments for the linter (`<!--lint -->`).
        These lines need to be removed from the file, to maintain a sytax that cen be interpretet correctly by SPARQL Anything.

        This method takes a file path as input, filters its content and remove `<!--lint -->` lines and writes the output to a TemporaryFile that is then returned.
        """
        # Read the content of the file
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Filter out lines containing <!--lint -->
        filtered_lines = [line for line in lines if not line.strip().startswith('<!--lint')]

        # Create a temporary file and write the filtered content
        self.temp_file = TemporaryFile(mode='w')
        self.temp_file.writelines(filtered_lines)
        self.temp_file.flush()
        self.temp_file.seek(0)

        return self.temp_file


    def parse(self):
        if not self.any_graph:
            self.any_graph = self.engine.construct(
                query=queries.spo(self.file_path.resolve())
            )
        return self.any_graph

    def get_readme_graph(self):
        if not self.everything:
            self.everything = self.get_concepts() + self.get_projects()
            self.everything.update(queries.merge_blank_categories())
            self.everything.update(queries.identify_tools(self.base_iri))
        return self.everything

    def get_concept_taxonomy(self):
        if not self.awesome_concept_taxonomy:
            self.awesome_concept_taxonomy = self.engine.construct(
                query=queries.concept_taxonomy(self.file_path.resolve(), self.base_iri)
            )
        return self.awesome_concept_taxonomy

    def get_concept_descriptions(self):
        if not self.awesome_concept_descriptions:
            self.awesome_concept_descriptions = self.engine.construct(
                query=queries.concept_description(
                    self.file_path.resolve(), self.base_iri
                )
            )
        return self.awesome_concept_descriptions

    def get_concepts(self):
        if not self.awesome_concepts:
            self.awesome_concepts = (
                self.get_concept_taxonomy() + self.get_concept_descriptions()
            )
        return self.awesome_concepts

    def get_projects(self):
        if not self.awesome_items:
            self.awesome_items = self.engine.construct(
                query=queries.awesome_items(self.file_path.resolve(), self.base_iri)
            )
        return self.awesome_items
