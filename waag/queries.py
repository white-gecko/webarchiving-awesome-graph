from undent import undent
from textwrap import dedent

prefixes = dedent("""
    prefix fx: <http://sparql.xyz/facade-x/ns/>
    prefix xyz: <http://sparql.xyz/facade-x/data/>
    prefix dct: <http://purl.org/dc/terms/>
    prefix skos: <http://www.w3.org/2004/02/skos/core#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix sioc: <http://rdfs.org/sioc/ns#>
    """)


def spo(file_path):
    """This query just passes on all triples from the sparql-anything service to the default graph."""
    return dedent(f"""
        construct {{
            ?s ?p ?o
        }} where {{
            service <x-sparql-anything:file://{file_path}> {{
                ?s ?p ?o
            }}
        }}
        """)


def concept_taxonomy(file_path, base_iri):
    """This query extracts all concepts and their taxonomy from the document."""
    return prefixes + dedent(f"""
        construct {{
            ?concept_iri a skos:Concept ;
                rdfs:label ?label ;
                skos:narrower ?sub_concept_iri .

            ?sub_concept_iri a skos:Concept ;
                rdfs:label ?sub_label ;
                skos:broader ?concept_iri .
        }} where {{
            service <x-sparql-anything:file://{file_path}> {{
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

                bind(iri(concat("{base_iri}", ?destination)) as ?concept_iri)

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

                    bind(iri(concat("{base_iri}", ?sub_destination)) as ?sub_concept_iri)
                }}

            }}
        }}
        """)

def concept_description(file_path, base_iri):
    """This query extracts the concept's descriptions from the document."""
    return prefixes + undent(f"""
        construct {{
            ?concept_iri a skos:Concept ;
                rdfs:label ?label ;
                dct:description ?description .

            ?sub_concept_iri a skos:Concept ;
                rdfs:label ?sub_label ;
                dct:description ?sub_description .
        }} where {{
            service <x-sparql-anything:file://{file_path}> {{
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

                bind(iri(concat("{base_iri}", ?destination)) as ?concept_iri)
            }}
        }}
        """)

def awesome_items(file_path):
    """Get the actual awesome items from the list."""

    return prefixes + undent(f"""
        construct {{
            ?destination a sioc:Item ;
                rdfs:label ?label ;
                dct:description ?description .

        }} where {{
            service <x-sparql-anything:file://{file_path}> {{
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
        """)
