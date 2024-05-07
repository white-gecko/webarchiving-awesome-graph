import io
import json
import click
import pypandoc
import panflute
from rdflib import URIRef
from graph_generation import GraphGeneration


def action(elem, doc):
    print("#walk")
    print(elem)


def action_list_items(elem, doc):
    if isinstance(elem, panflute.ListItem):
        item = {}
        for i in elem.content:
            action_walk_list_item(i, doc=item)
        pattern = [panflute.Space(), panflute.Str("-"), panflute.Space()]
        if "description" in item:
            print("#description")
            print(item["description"])
            for p in pattern:
                print(pattern, p)
                if p == item["description"][0]:
                    print("#match")
                    item["description"].pop(0)
        print("item")
        print(item)
        doc.append(item)


def action_walk_list_item(elem, doc):
    if "url" not in doc and isinstance(elem, panflute.Link):
        doc["title"] = panflute.stringify(elem)
        doc["url"] = elem.url
    else:
        if "description" not in doc:
            doc["description"] = []
        doc["description"].append(elem)


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

    # doc.walk(action, doc=doc)

    panflute.debug(doc)
    gg = GraphGeneration()
    doc.parent_id = None
    doc.current_header = None
    doc.headers = {}
    doc.lists = []
    doc = panflute.run_filter(action_headers, doc=doc)
    doc.walk(action_headers, doc=doc)

    #    print(json.dumps(doc.headers, indent=4))

    for header_id, header_obj in doc.headers.items():
        print(panflute.stringify(header_obj["elem"]))
        print(header_id)
        panflute.debug(header_obj["elem"])
        if "list" in header_obj:
            bullet_list = header_obj["list"]
            extracted = []
            bullet_list = bullet_list.walk(action_list_items, doc=extracted)
            print("complete list")
            print(extracted)
            # panflute.debug(bullet_list)


if __name__ == "__main__":
    cli()
