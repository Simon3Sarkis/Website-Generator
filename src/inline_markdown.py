from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
<<<<<<< HEAD

def extract_markdown_images(text):
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r'(?<!\!)\[([^\]]*)\]\(([^)]+)\)'
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_nodes = []
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        last_index = 0
        for match in re.finditer(pattern, old_node.text):
            start, end = match.span()

            if start > last_index:
                new_nodes.append(
                    TextNode(old_node.text[last_index:start], TextType.TEXT)
                )

            alt_text, url = match.groups()
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            last_index = end

        if last_index < len(old_node.text):
            new_nodes.append(
                TextNode(old_node.text[last_index:], TextType.TEXT)
            )

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = r'(?<!\!)\[([^\]]*)\]\(([^)]+)\)'

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        last_index = 0
        for match in re.finditer(pattern, old_node.text):
            start, end = match.span()

            if start > last_index:
                new_nodes.append(
                    TextNode(old_node.text[last_index:start], TextType.TEXT)
                )

            link_text, url = match.groups()
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            last_index = end

        if last_index < len(old_node.text):
            new_nodes.append(
                TextNode(old_node.text[last_index:], TextType.TEXT)
            )

    return new_nodes
=======
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches
>>>>>>> ea919dca1357a724b0a905e12ab12df60763b6a7
