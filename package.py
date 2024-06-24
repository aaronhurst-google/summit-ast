import subprocess
import sys
from lxml import etree
from pathlib import Path

def insert_xml(outer_xml_path, inner_xml_path, xpath, output_path):
    outer_tree = etree.parse(outer_xml_path)
    inner_tree = etree.parse(inner_xml_path)

    # Find the target node in the outer XML
    parent_nodes = outer_tree.xpath(xpath)
    if len(parent_nodes) != 1:
      raise ValueError(f"Could not match xpath {xpath}")
    # Insert the inner XML as an element of the target node
    parent_nodes[0].append(inner_tree.getroot())
    # Write the modified XML back to the file
    outer_tree.write(output_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')

if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    out_dir = root / "bazel-bin"

    version = open(root / 'VERSION').read().strip()

    # Inject authors file
    original_pom = out_dir / "maven_assemble_pom.xml"
    preformat_xml = out_dir / "maven_assemble_pom_with_authors.xml"
    final_pom = out_dir / f"summit-ast-{version}.pom"
    insert_xml(original_pom, root / "authors.xml", '//*[local-name()="project"]', preformat_xml)
    subprocess.run(["xmllint", "--format", preformat_xml, "-o", final_pom])

    # Create dummy docs JAR (required for release)
    readme_content = "This release does not yet include complete documentation."
    with open(out_dir / "README", 'w') as readme_file:
      readme_file.write(readme_content)
    subprocess.run(["jar", "cf", f"summit-ast-{version}-javadoc.jar", "README"], cwd=out_dir)

    # Rename files with version
    subprocess.run(["cp", "-f", out_dir / "com.google.summit-summit-ast-sources.jar", out_dir / f"summit-ast-{version}-sources.jar"])
    subprocess.run(["cp", "-f", out_dir / "com.google.summit-summit-ast.jar", out_dir / f"summit-ast-{version}.jar"])
