import click
import sys
from pathlib import Path

from .list_parser import ListParser


def call_and_write(callable, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    graph = callable()
    with open(path, mode="wb") as file:
        print(f"Write out to: {path}", end="...")
        graph.serialize(destination=file, format="turtle")
        print("done")


@click.command()
@click.option(
    "--awesome-file", "-a", help="The location of the awesome list (Markdown)."
)
@click.option(
    "--graph-output", "--output", "-o", help="Where to write the graph to.", default="-"
)
@click.option(
    "--output-dir", help="Where to write the individual graphs to.", default="graphs"
)
@click.option("--base-iri", "--iri", help="The base IRI of the document.")
def cli(awesome_file, base_iri, graph_output, output_dir):
    """Get the urls from the markdown files"""

    if graph_output == "-":
        graph_output = sys.stdout

    parser = ListParser(awesome_file, base_iri)

    call_and_write(parser.parse, Path(output_dir) / "any.ttl")
    call_and_write(parser.get_concepts, Path(output_dir) / "concepts.ttl")
    call_and_write(parser.get_projects, Path(output_dir) / "projects.ttl")
    call_and_write(parser.get_awesome_graph, Path(output_dir) / "awesome.ttl")
    # graph_generation = GraphGeneration()
    # graph = graph_generation(parser)


if __name__ == "__main__":
    cli()
