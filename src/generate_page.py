from split_nodes import extract_title
from markdown_blocks import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read files
    from_file = open(from_path, 'r')
    from_template = open(template_path, 'r')
    read_from_file = from_file.read()
    read_from_template = from_template.read()
    
    # Extract title and convert markdown to HTML
    title = extract_title(read_from_file)
    markdown_node = markdown_to_html_node(read_from_file)
    html_string = markdown_node.to_html()
    
    # Replace placeholders in template
    final_html = read_from_template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    
    # Ensure destination directory exists
    import os
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write to destination file
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_html)
    
    # Close original file handles
    from_file.close()
    from_template.close()

