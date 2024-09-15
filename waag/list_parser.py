import pysparql_anything as sa
from undent import undent
from pathlib import Path

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

    def parse(self):
        graph = self.engine.construct(
        	query=undent(f"""
                construct {{
                    ?s ?p ?o
                }} where {{
                    service <x-sparql-anything:file://{self.file_path.resolve()}> {{
                        ?s ?p ?o
                    }}
                }}
                """)
        )
        self.any_graph = graph
        print(graph.serialize(format='turtle'))

    def get_awesome_graph(self):
        pass

    def get_concept_taxonomy(self):
        if not self.awesome_concept_taxonomy:
            self.awesome_concept_taxonomy = self.engine.construct(query=undent(f"""
                prefix fx: <http://sparql.xyz/facade-x/ns/>
                prefix xyz: <http://sparql.xyz/facade-x/data/>
                prefix dct: <http://purl.org/dc/terms/>
                prefix skos: <http://www.w3.org/2004/02/skos/core#>
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                prefix xsd: <http://www.w3.org/2001/XMLSchema#>

                construct {{
                    ?concept_iri a skos:Concept ;
                        rdfs:label ?label ;
                        skos:narrower ?sub_concept_iri .

                    ?sub_concept_iri a skos:Concept ;
                        rdfs:label ?sub_label ;
                        skos:broader ?concept_iri .
                }} where {{
                    service <x-sparql-anything:file://{self.file_path.resolve()}> {{
                        ?root ?li_contents ?contents .
                        ?contents a xyz:Heading ;
                            xyz:level 2 ;
                            rdf:_1 "Contents" .
                        ?root ?li_contents_list ?contents_list .
                        ?contents_list a xyz:BulletList ;
                            ?li_concept ?concept_node .

                        filter(fx:next(?li_contents) = ?li_contents_list) .

                        ?concept_node rdf:_1 [ a xyz:Paragraph ;
                            rdf:_1 [ a xyz:Link ;
                                xyz:destination ?destination ;
                                rdf:_1 ?label
                            ]
                        ] .

                        bind(iri(concat("{self.base_iri}", ?destination)) as ?concept_iri)

                        optional {{
                            ?concept_node rdf:_2 [ a xyz:BulletList ;
                                ?li [
                                    rdf:_1 [ a xyz:Paragraph ;
                                        rdf:_1 [ a xyz:Link ;
                                            xyz:destination ?sub_destination ;
                                            rdf:_1 ?sub_label
                                        ]
                                    ]
                                ]
                            ] .

                            bind(iri(concat("{self.base_iri}", ?sub_destination)) as ?sub_concept_iri)
                        }}

                    }}
                }}
                """))
        return self.awesome_concept_taxonomy

    def get_concept_descriptions(self):
        if not self.awesome_concept_descriptions:
            self.awesome_concept_descriptions = self.engine.construct(query=undent(f"""
                prefix fx: <http://sparql.xyz/facade-x/ns/>
                prefix xyz: <http://sparql.xyz/facade-x/data/>
                prefix dct: <http://purl.org/dc/terms/>
                prefix skos: <http://www.w3.org/2004/02/skos/core#>
                prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                prefix xsd: <http://www.w3.org/2001/XMLSchema#>

                construct {{
                    ?concept_iri a skos:Concept ;
                        rdfs:label ?label ;
                        dct:description ?description .

                    ?sub_concept_iri a skos:Concept ;
                        rdfs:label ?sub_label ;
                        dct:description ?sub_description .
                }} where {{
                    service <x-sparql-anything:file://{self.file_path.resolve()}> {{
                        ?root ?li_contents ?contents .
                        ?contents a xyz:Heading ;
                            xyz:level 2 ;
                            rdf:_1 "Contents" .
                        ?root ?li_contents_list ?contents_list .
                        ?contents_list a xyz:BulletList ;
                            ?li_concept [
                                rdf:_2?/fx:anySlot?/rdf:_1 [ a xyz:Paragraph ;
                                    rdf:_1 [ a xyz:Link ;
                                        xyz:destination ?destination ;
                                        rdf:_1 ?label
                                    ]
                                ]
                            ] .

                        filter(fx:next(?li_contents) = ?li_contents_list) .

                        ?root ?concept_membership [ a xyz:Heading ;
                            rdf:_1 ?label
                        ] .

                        optional {{
                            ?root ?next_membership [
                                a xyz:Paragraph ;
                                rdf:_1 ?description
                            ] .
                            filter (fx:next(?concept_membership) = ?next_membership)
                        }}

                        bind(iri(concat("{self.base_iri}", ?destination)) as ?concept_iri)
                    }}
                }}
                """))
        return self.awesome_concept_descriptions

    def get_concepts(self):
        if not self.awesome_concepts:
            self.awesome_concepts = self.get_concept_taxonomy() + self.get_concept_descriptions()
        print(self.awesome_concepts.serialize(format='turtle'))
        return self.awesome_concepts

    def get_projects(self):
        self.awesome_items = self.engine.construct(query=undent(f"""
            prefix fx: <http://sparql.xyz/facade-x/ns/>
            prefix xyz: <http://sparql.xyz/facade-x/data/>
            prefix dct: <http://purl.org/dc/terms/>
            prefix skos: <http://www.w3.org/2004/02/skos/core#>
            prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            prefix xsd: <http://www.w3.org/2001/XMLSchema#>
            prefix sioc: <http://rdfs.org/sioc/ns#>

            construct {{
                ?destination a sioc:Item ;
                    rdfs:label ?label ;
                    dct:description ?description .

            }} where {{
                service <x-sparql-anything:file://{self.file_path.resolve()}> {{
                    ?sibling_projects_list a xyz:BulletList ;
                        fx:anySlot [ a xyz:ListItem ;
                            rdf:_1 ?project_paragraph ;
                        ] .

                    ?project_paragraph a xyz:Paragraph ;
                        rdf:_1 [ a xyz:Link ;
                            xyz:destination ?destination ;
                            rdf:_1 ?label
                        ] .

                    optional {{
                        ?project_paragraph rdf:_2 ?description_with_dash .
                        filter(substr(?description_with_dash, 0, 4) = " - ")
                        bind(substr(?description_with_dash, 4) as ?description)
                    }}


                }}
            }}
            """))
        print(self.awesome_items.serialize(format='turtle'))
        return self.awesome_items
