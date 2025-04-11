import click
import sys
from pathlib import Path

from .graph_generation import GraphGeneration


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

    graph_generation = GraphGeneration(base_iri=base_iri)
    graph_generation.init_from_dir(Path(output_dir))
    graph_generation.init_from_readme(awesome_file)
    graph_generation.fetch_doap()
    graph_generation.store_to_dir(awesome_file, Path(output_dir))


if __name__ == "__main__":
    cli()
