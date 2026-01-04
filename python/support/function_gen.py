import xml.etree.ElementTree as ET
import re
import json

def to_class_name(func_name):
    """
    Convert a function name (e.g. "Type Must Be Cluster")
    to a valid Python class name (e.g. "TypeMustBeCluster").
    """
    # Remove non-alphanumeric characters and title-case each word.
    words = re.findall(r'\w+', func_name)
    return ''.join(word.capitalize() for word in words)

def generate_function_node_class(function_elem):
    """
    Given an XML <function> element, generate a Python class definition
    string for a function node.
    """
    func_name = function_elem.attrib.get('name', 'UnnamedFunction')
    class_name = to_class_name(func_name)
    chunks = function_elem.attrib.get('chunks', '1')
    
    # Start building the class definition.
    lines = []
    lines.append(f"class {class_name}(GrowableFunction):")
    lines.append("    def __init__(self):")
    lines.append(f"        GrowableFunction.__init__(self, \"{func_name}\", chunks={chunks})")
    
    # Generate terminals from the XML.
    for term in function_elem.findall('terminal'):
        term_name = term.attrib.get('name', 'UnnamedTerminal')
        datatype = term.attrib.get('datatype', 'Unknown')
        direction = term.attrib.get('dir', 'in').lower()
        is_input = True if direction == 'in' else False
        # You could embed the datatype as a comment if desired.
        # lines.append(f"        # Terminal: {term_name} (datatype: {datatype}, direction: {direction})")
        inputTag = ""
        if not is_input:
            inputTag = f", isInput={is_input}"
        lines.append(f"        LVNode.addTerminal(self, \"{term_name}\", varType=\"{datatype}\"{inputTag})")
    
    # Set additional attributes
    lines.append(f"        self.attributes[\"type\"] = \"{func_name}\"")
    lines.append("")  # Blank line for readability
    return "\n".join(lines)

def generate_classes_from_xml(xml_file):
    """
    Parse the given XML file and generate Python class definitions
    for each function.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Assume the top-level element is <functions>.
    classes = []
    for func in root.findall('function'):
        classes.append(generate_function_node_class(func))
    
    return "\n\n".join(classes)

def generate_function_summary(xml_file, output_file):
    """
    Reads an XML file containing function definitions and outputs a compact JSON summary.
    
    The JSON will be a dictionary where each key is a function name and its value is a list
    of terminal definitions. Each terminal is represented as a dictionary with keys:
    "dir", "datatype", and "name".
    
    The JSON is generated with minimal whitespace for efficiency.
    
    Example XML input:
    <functions>
      <function name="Type Must Be Cluster">
        <terminal datatype="LV Variant" dir="in" name="any"/>
      </function>
      <function name="Type Of">
        <terminal datatype="LV Variant" dir="out" name="type"/>
        <terminal datatype="LV Variant" dir="in" name="any"/>
      </function>
    </functions>
    """
    # Parse the XML file.
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Build a dictionary mapping function names to a list of terminal dicts.
    functions_summary = {}
    for func in root.findall('function'):
        func_name = func.attrib.get('name', 'UnnamedFunction')
        terminals = []
        x = 0
        for term in func.findall('terminal'):
            terminal_info = {
                'dir': term.attrib.get('dir', ''),
                'datatype': term.attrib.get('datatype', ''),
                'name': term.attrib.get('name', f'term{x}')
            }
            terminals.append(terminal_info)
            x += 1
        functions_summary[to_class_name(func_name)] = terminals

    # Dump the dictionary as a minimal JSON string.
    # The separators argument removes extra whitespace.
    json_output = json.dumps(functions_summary, separators=(',', ':'))

    # Write the JSON string to the output file.
    with open(output_file, 'w') as f:
        f.write(json_output)

    return json_output  # Also return the JSON string if needed


def generate_function_summary_short(xml_file, output_file):
    # Parse the XML file.
    tree = ET.parse(xml_file)
    root = tree.getroot()

    dataTypes = {}

    # Build a dictionary mapping function names to a list of terminal dicts.
    functions_summary = {}
    for func in root.findall('function'):
        func_name = func.attrib.get('name', 'UnnamedFunction')
        terminals = []
        for term in func.findall('terminal'):
            direction = term.attrib.get('dir', 'in').lower()
            dataType = term.attrib.get('datatype', '')
            if dataType not in dataTypes:
                dataTypes[dataType] = len(dataTypes) + 1
            dataTypeIndex = dataTypes[dataType]
            is_input = 0 if direction == 'in' else 1
            terminal_info = [
                is_input,
                dataTypeIndex,
                term.attrib.get('name', 'UnnamedTerminal')
            ]
            terminals.append(terminal_info)
        functions_summary[to_class_name(func_name)] = terminals

    # Dump the dictionary as a minimal JSON string.
    # The separators argument removes extra whitespace.
    json_output = json.dumps(functions_summary, separators=(',', ':'))

    # Write the JSON string to the output file.
    with open(output_file, 'w') as f:
        f.write(str(dataTypes))
        f.write(json_output)

    return json_output 


if __name__ == '__main__':
    # generated_code = ""
    xml_file = f"/Users/jake/projects/Go to LV/LVGPT/LabVIEW/support_files/functions/growable.xml"
    # generated_code = "from node import LVNode, GrowableFunction, ObjectFunction\n" + generate_classes_from_xml(xml_file)

    # with open("python/lvGraph/growable.py", "w") as f:
    #     f.write(generated_code)

    # generate_function_summary(xml_file, "/Users/jake/projects/Go to LV/LVGPT/LabVIEW/support_files/functions/function_summary.json")
    generate_function_summary_short(xml_file, "/Users/jake/projects/Go to LV/LVGPT/LabVIEW/support_files/functions/growable_summary_short.json")
    
