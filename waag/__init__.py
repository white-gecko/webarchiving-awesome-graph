import click

from list_parser import ListParser
from graph_generation import GraphGeneration

@click.command()
@click.option("--file", help="The location of the awesome list (Markdown).")
@click.option("--base-iri", "--iri", help="The base IRI of the document.")
def cli(file, base_iri):
    """Get the urls from the markdown files"""
    parser = ListParser(file, base_iri)
    parser.parse()
    print("===========")
    # parser.get_concepts()
    parser.get_projects()
    # graph_generation = GraphGeneration()
    # graph = graph_generation(parser)


if __name__ == "__main__":
    cli()
