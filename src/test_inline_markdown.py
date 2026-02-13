import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        text = (
            "This is a [link](https://boot.dev) "
            "and another [youtube](https://youtube.com)"
        )

        result = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("youtube", "https://youtube.com"),
            ],
            result,
        )
    def test_extract_markdown_links(self):
        text = (
            "This is a [link](https://boot.dev) "
            "and another [youtube](https://youtube.com)"
        )

        result = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("youtube", "https://youtube.com"),
            ],
            result, )
    def test_split_nodes_image(self):
        nodes = [
            TextNode(
                "Start ![one](https://img.com/1.png) middle ![two](https://img.com/2.png) end",
                TextType.TEXT,
            ),
            TextNode(
                "![solo](https://img.com/solo.png)",
                TextType.TEXT,
            ),
            TextNode(
                "Just plain text",
                TextType.TEXT,
            ),
            TextNode(
                "existing image",
                TextType.IMAGE,
                "https://img.com/existing.png",
            ),
        ]

        result = split_nodes_image(nodes)

        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("one", TextType.IMAGE, "https://img.com/1.png"),
                TextNode(" middle ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "https://img.com/2.png"),
                TextNode(" end", TextType.TEXT),

                TextNode("solo", TextType.IMAGE, "https://img.com/solo.png"),

                TextNode("Just plain text", TextType.TEXT),

                TextNode("existing image", TextType.IMAGE, "https://img.com/existing.png"),
            ],
            result,
        )
    def test_split_nodes_link(self):
        old_nodes = [
            TextNode(
                "This is a [link](https://boot.dev) and another [site](https://example.com)",
                TextType.TEXT,
            )
        ]

        new_nodes = split_nodes_link(old_nodes)

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("site", TextType.LINK, "https://example.com"),
            ],
        )

        
    def test_text_to_textnodes(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        nodes = text_to_textnodes(text)

        assert nodes == [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]


if __name__ == "__main__":
    unittest.main()
