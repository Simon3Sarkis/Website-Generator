import os
from block_markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path, "r")
    markdown_content = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown_content)
    content_html = html_node.to_html()

    page_title = extract_title(markdown_content)

    final_output = template_content.replace("{{ Title }}", page_title)
    final_output = final_output.replace("{{ Content }}", content_html)

    final_output = final_output.replace('href="/', f'href="{basepath}')
    final_output = final_output.replace('src="/', f'src="{basepath}')


    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    output_file = open(dest_path, "w")
    output_file.write(final_output)
    output_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)