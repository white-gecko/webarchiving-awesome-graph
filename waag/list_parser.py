import pysparql_anything as sa
from pathlib import Path
from . import queries


class AwesomeEntry:
    def __init__(self):
        self.url
        self.title
        self.description
        self.comment
        self.attributes = {}


class ListParser:
    def __init__(self, file, base_iri):
        self.file_path = Path(file)
        self.base_iri = base_iri
        self.engine = sa.SparqlAnything()

        self.any_graph = None
        self.everything = None
        self.awesome_concepts = None
        self.awesome_concept_taxonomy = None
        self.awesome_concept_descriptions = None
        self.awesome_items = None

    def parse(self):
        if not self.any_graph:
            self.any_graph = self.engine.construct(
                query=queries.spo(self.file_path.resolve())
            )
        return self.any_graph

    def get_awesome_graph(self):
        if not self.everything:
            self.everything = (
                self.get_concepts() + self.get_projects()
            )
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
