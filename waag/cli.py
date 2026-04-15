import click
from pathlib import Path

from waag.graph_generation import GraphGeneration


@click.command()
@click.option(
    "--awesome-file", "-a", help="The location of the awesome list (Markdown)."
)
@click.option(
    "--output-dir", help="Where to write the individual graphs to.", default="graphs"
)
@click.option("--base-iri", "--iri", help="The base IRI of the document.")
def cli(awesome_file, base_iri, output_dir):
    """Get the urls from the markdown files

    This function serves as the command-line interface for the awesome list processing tool.
    It parses command-line arguments and orchestrates the generation of RDF graphs from awesome lists.

    Args:
        awesome_file (str): Path to the awesome list markdown file
        base_iri (str): Base IRI for the generated RDF resources
        output_dir (str): Directory where output graphs will be written
    """
    graph_generation = GraphGeneration(base_iri=base_iri)
    graph_generation.init_from_dir(Path(output_dir))
    graph_generation.init_from_readme(awesome_file)
    graph_generation.fetch_doap()
    graph_generation.store_to_dir(awesome_file, Path(output_dir))


if __name__ == "__main__":
    cli()
