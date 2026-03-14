from enum import Enum

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