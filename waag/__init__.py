import io
import json
import click
import pypandoc
import panflute
from rdflib import URIRef
from graph_generation import GraphGeneration


def action_lists(elem, doc):
    if isinstance(elem, panflute.BulletList):
        doc.lists.append(elem)


def action_links(elem, doc):
    if isinstance(elem, panflute.Link):
        doc.links.append(elem)


def action_headers(elem, doc):
    if isinstance(elem, panflute.Header):
        if doc.current_header is None:
            doc.parent_id = None
        elif doc.current_header.level < elem.level:
            doc.parent_id = doc.current_header.identifier
        else:
            doc.parent_id = doc.headers[doc.current_header.identifier]["parent"]
        doc.current_header = elem
        doc.headers[elem.identifier] = {"elem": elem, "parent": doc.parent_id}
        if isinstance(elem.next, panflute.BulletList):
            doc.headers[elem.identifier]["list"] = elem.next
            panflute.debug(elem)


@click.command()
@click.option("--file", help="The location of the awesome list (Markdown).")
@click.option("--base-iri", "--iri", help="The base IRI of the document.")
def cli(file, base_iri):
    """Get the urls from the markdown files"""
    data = pypandoc.convert_file(file, "json")
    doc = panflute.load(io.StringIO(data))
    doc_json_s = io.StringIO()
    panflute.dump(doc, doc_json_s)
    doc_json = json.loads(doc_json_s.getvalue())
    print(json.dumps(doc_json, indent=4))
    panflute.debug(doc)
    gg = GraphGeneration()
    doc.parent_id = None
    doc.current_header = None
    doc.headers = {}
    doc.lists = []
    doc.links = []
    doc = panflute.run_filter(action_headers, doc=doc)
    # doc.walk(action_headers, doc=doc)

    print(json.dumps(doc.headers, indent=4))

    print("List of URLs:")
    for image in doc.links:
        print(image.url)
    for header_id, header_obj in doc.headers.items():
        print(header_id)
        print(header_obj)
        panflute.debug(header_obj["elem"])
        panflute.debug(header_obj["list"]) if "list" in header_obj else None
        print(header_obj["elem"].level)
        print(header_obj["elem"].identifier)
        print(panflute.stringify(header_obj["elem"]))


if __name__ == "__main__":
    cli()
