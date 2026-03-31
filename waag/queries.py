from textwrap import dedent

prefixes = dedent("""
    prefix fx: <http://sparql.xyz/facade-x/ns/>
    prefix xyz: <http://sparql.xyz/facade-x/data/>
    prefix dct: <http://purl.org/dc/terms/>
    prefix skos: <http://www.w3.org/2004/02/skos/core#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix sioc: <http://rdfs.org/sioc/ns#>
    prefix doap: <http://usefulinc.com/ns/doap#>
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
                ?root ?li_contents [ a xyz:Heading ;
                        xyz:level 2 ;
                        rdf:_1 "Contents" ] ;
                    ?li_contents_list [ a xyz:BulletList ;
                        ?li_concept ?concept_node ] .

                filter(fx:next(?li_contents) = ?li_contents_list) .

                ?concept_node rdf:_1 [ a xyz:Paragraph ;
                    rdf:_1 [ a xyz:Link ;
                        xyz:destination ?destination ;
                        rdf:_1 ?label
                    ]
                ] .

                bind(
                    iri(
                        concat(
                            "{base_iri}",
                            if(strStarts(?destination, "#"), substr(?destination, 2), ?destination)
                        )
                    ) as ?concept_iri
                )

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

                    bind(
                        iri(
                            concat(
                                "{base_iri}",
                                if(strStarts(?sub_destination, "#"), substr(?sub_destination, 2), ?sub_destination)
                            )
                        ) as ?sub_concept_iri
                    )
                }}

            }}
        }}
        """)


def concept_description(file_path, base_iri):
    """This query extracts the concept's descriptions from the document."""
    return prefixes + dedent(f"""
        construct {{
            ?concept_iri a skos:Concept ;
                rdfs:label ?label ;
                dct:description ?description .
        }} where {{
            service <x-sparql-anything:file://{file_path}> {{
                ?root ?li_contents [ a xyz:Heading ;
                        xyz:level 2 ;
                        rdf:_1 "Contents" ] ;
                    ?li_contents_list [ a xyz:BulletList ;
                        ?li_concept ?concept_node ] .

                filter(fx:next(?li_contents) = ?li_contents_list) .

                ?concept_node rdf:_2?/fx:anySlot?/rdf:_1 [ a xyz:Paragraph ;
                    rdf:_1 [ a xyz:Link ;
                        xyz:destination ?destination ;
                        rdf:_1 ?label
                    ]
                ] .

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

                bind(
                    iri(
                        concat(
                            "{base_iri}",
                            if(strStarts(?destination, "#"), substr(?destination, 2), ?destination)
                        )
                    ) as ?concept_iri
                )
            }}
        }}
        """)


def awesome_items(file_path, base_iri):
    """Get the actual awesome items from the list."""

    return prefixes + dedent(f"""
        construct {{
            ?item_iri a sioc:Item ;
                owl:sameAs ?destination_iri ;
                rdfs:label ?label ;
                dct:description ?description ;
                doap:category [ a skos:Concept ;
                    rdfs:label ?category_label
                ], ?stability .
            ?stability a skos:Concept ;
                rdfs:label ?stability_label .

        }} where {{
            service <x-sparql-anything:file://{file_path}> {{
                ?root ?li_heading [ a xyz:Heading ;
                        rdf:_1 ?category_label ] .
                optional {{
                    ?root ?li_paragraph [ a xyz:Paragraph ;
                            rdf:_1 ?paragraph_text ] .
                    filter(fx:next(?li_heading) = ?li_paragraph)
                }}
                ?root ?li_projects_list ?projects_list .

                filter(fx:next(if(bound(?li_paragraph), ?li_paragraph, ?li_heading)) = ?li_projects_list)
                filter(?category_label != "Contents")

                ?projects_list a xyz:BulletList ;
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
                    filter(strStarts(?description_with_dash, " - "))
                    bind(substr(?description_with_dash, 4) as ?description)
                }}

                optional {{
                    ?project_paragraph fx:anySlot [ a xyz:Emphasis ;
                        rdf:_1 ?stability_str ]  .
                    bind(substr(?stability_str, 2, strlen(?stability_str) - 2) as ?stability_label)
                    bind(iri("{base_iri}", replace(?stability_label, " ", "_")) as ?stability)
                }}

                bind(
                    iri(
                        if(
                            strStarts(?destination, "#"),
                            concat("{base_iri}", substr(?destination, 2)),
                            ?destination
                        )
                    ) as ?destination_iri
                )

                bind(
                    iri(
                        concat("{base_iri}", encode_for_uri(replace(?label, " ", "_")))
                    ) as ?item_iri
                )

            }}
        }}
        """)


def merge_blank_categories():
    """Assign the named node categories to the projects based on the label.

    During the item extraction (`awesome_items()`), the projects get blank nodes as categories,
    while the category IRIs are minted in `concept_taxonomy()`.
    In this query the blank nodes are merged with the named nodes.
    """

    return prefixes + dedent("""
        delete {
            ?project_iri doap:category ?blank_category .
            ?blank_category a skos:Concept ;
                rdfs:label ?category_label .
        } insert {
            ?project_iri doap:category ?category_iri .
        } where {
            ?project_iri doap:category ?blank_category .
            ?blank_category a skos:Concept ;
                    rdfs:label ?category_label .
            ?category_iri a skos:Concept ;
                rdfs:label ?category_label .
            filter(isBlank(?blank_category))
            filter(!isBlank(?category_iri))
        }
        """)


def identify_tools(base_iri):
    """Make all tools doap projects.

    During the item extraction (`awesome_items()`) all items of the awesoe list are treated as doap:Items.
    In this step all items in the `tools--software` category additinally assigned to the class doap:Project.
    """

    return prefixes + dedent(f"""
        insert {{
            ?project_iri a doap:Project .
        }} where {{
            {{
                bind(<{base_iri}tools--software> as ?projects)
            }} union {{
                <{base_iri}tools--software> skos:narrower ?projects .
            }}
            ?project_iri doap:category ?projects
        }}
        """)


def list_projects():
    """Select all projects and their platform project URLs, i.e., the URL of the respective GitHub project.

    It is assumed, that the GitHub project is linked as owl:sameAs.
    """

    return prefixes + dedent("""
        select ?project ?platform_project {
            ?project a doap:Project .
            optional {
                ?project owl:sameAs ?platform_project .
            }
        }
    """)
