from enum import Enum
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode, LeafNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"



def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        block = block.strip()

        if block != "":
            filtered_blocks.append(block)
            
    return filtered_blocks

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(block) >= 6 and block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")
    
    if block.startswith(">"):
        is_quote = True
        for line in lines:
            if not line.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return BlockType.QUOTE

    if block.startswith("- "):
        is_ulist = True
        for line in lines:
            if not line.startswith("- "):
                is_ulist = False
                break
        if is_ulist:
            return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        is_olist = True
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                is_olist = False
                break
            i += 1
        if is_olist:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:] 
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def code_to_html_node(block):
    text = block.strip("`").strip()
    
    text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(text_node)

    code_node = ParentNode("code", [child])
    return ParentNode("pre", [code_node])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[item.find(" ") + 1:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    raise ValueError("invalid block type")

def markdown_to_html_node(markdown):

    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
        
    return ParentNode("div", children)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("All pages need an h1 header")

