import click
import sys

from .list_parser import ListParser


@click.command()
@click.option(
    "--awesome-file", "-a", help="The location of the awesome list (Markdown)."
)
@click.option(
    "--graph-output", "--output", "-o", help="Where to write the graph to.", default="-"
)
@click.option("--base-iri", "--iri", help="The base IRI of the document.")
def cli(awesome_file, base_iri, graph_output):
    """Get the urls from the markdown files"""

    if graph_output == "-":
        graph_output = sys.stdout

    parser = ListParser(awesome_file, base_iri)
    parser.parse()
    print("===========")
    parser.get_concepts()
    # parser.get_projects()
    # graph_generation = GraphGeneration()
    # graph = graph_generation(parser)


if __name__ == "__main__":
    cli()
