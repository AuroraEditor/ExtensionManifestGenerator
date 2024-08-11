import json
import os
from jinja2 import Template
from datetime import datetime

# Load JSON schema from a file
def load_schema(schema_file):
    with open(schema_file, 'r') as file:
        schema = json.load(file)
    return schema

# Jinja2 template for Swift class generation
swift_template = """//
//  Extension{{ class_name }}.swift
//  AuroraEditorSourceEditor
//
//  Created by Aurora Editor on {{ date }}.
//

import Foundation

// WARNING: This file is auto-generated by the code generation tool.
// Modifications to this file may be overwritten and lost if the code is regenerated.
// If you need to make changes, update the source schema or generation process instead.
// DO NOT EDIT THIS FILE MANUALLY.
struct Extension{{ class_name }}: Codable {
    {% for property_name, property_info in properties.items() -%}
    var {{ property_name }}: {{ property_info.type }}{{ "?" if not property_info.required }}{% if not loop.last %}{% endif %}
    {% endfor %}
}
"""

# Map JSON schema types to Swift types
type_mapping = {
    "string": "String",
    "integer": "Int",
    "boolean": "Bool",
    "array": "Array",
    "object": "Object"
}

# Recursively generate Swift class structures
def generate_classes(name, schema):
    classes = {}
    properties = schema.get('properties', {})
    required = schema.get('required', [])
    class_properties = {}

    for prop_name, prop_schema in properties.items():
        prop_type = prop_schema.get('type')
        is_required = prop_name in required

        if prop_type == 'object':
            nested_class_name = prop_name.capitalize()
            nested_classes = generate_classes(nested_class_name, prop_schema)
            classes.update(nested_classes)
            class_properties[prop_name] = {
                'type': nested_class_name,
                'required': is_required
            }
        elif prop_type == 'array':
            items = prop_schema.get('items', {})
            item_type = items.get('type')
            if item_type == 'object':
                nested_class_name = prop_name.capitalize()
                nested_classes = generate_classes(nested_class_name, items)
                classes.update(nested_classes)
                class_properties[prop_name] = {
                    'type': f"[{nested_class_name}]",
                    'required': is_required
                }
            else:
                class_properties[prop_name] = {
                    'type': f"[{type_mapping.get(item_type, 'Any')}]",
                    'required': is_required
                }
        else:
            class_properties[prop_name] = {
                'type': type_mapping.get(prop_type, 'Any'),
                'required': is_required
            }

    classes[name] = class_properties
    return classes

# Generate Swift classes from the schema
def generate_swift_models(schema_file):
    schema = load_schema(schema_file)
    swift_classes = generate_classes("Manifest", schema)

    # Get the current date
    current_date = datetime.now().strftime("%m/%d/%y")

    # Create output directory if it doesn't exist
    output_directory = "./GeneratedSwiftModels"
    os.makedirs(output_directory, exist_ok=True)

    # Render each class to a separate file
    template = Template(swift_template)
    for class_name, properties in swift_classes.items():
        output = template.render(class_name=class_name, properties=properties, date=current_date)
        # Remove any trailing whitespace from each line
        output = '\n'.join(line.rstrip() for line in output.splitlines())
        output_file = os.path.join(output_directory, f"Extension{class_name}.swift")
        with open(output_file, "w") as f:
            f.write(output)
        print(f"Generated {output_file}")

# Main execution
if __name__ == "__main__":
    schema_file = "ExtensionManifestScheme.json"
    generate_swift_models(schema_file)