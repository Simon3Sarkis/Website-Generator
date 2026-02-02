import unittest
from inline_markdown import (
    split_nodes_delimiter,
<<<<<<< HEAD
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
=======
    extract_markdown_links,
    extract_markdown_images,
>>>>>>> ea919dca1357a724b0a905e12ab12df60763b6a7
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
        self.assertEqual(
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
<<<<<<< HEAD
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
        nodes = [
            TextNode(
                "Go to [boot](https://boot.dev) and [yt](https://youtube.com)",
                TextType.TEXT,
            ),
            TextNode(
                "[solo](https://solo.com)",
                TextType.TEXT,
            ),
            TextNode(
                "Just text",
                TextType.TEXT,
            ),
            TextNode(
                "This is an ![image](https://img.com/a.png)",
                TextType.TEXT,
            ),
            TextNode(
                "boot",
                TextType.LINK,
                "https://boot.dev",
            ),
        ]

        result = split_nodes_link(nodes)

        self.assertListEqual(
            [
                TextNode("Go to ", TextType.TEXT),
                TextNode("boot", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("yt", TextType.LINK, "https://youtube.com"),

                TextNode("solo", TextType.LINK, "https://solo.com"),

                TextNode("Just text", TextType.TEXT),

                TextNode("This is an ![image](https://img.com/a.png)", TextType.TEXT),

                TextNode("boot", TextType.LINK, "https://boot.dev"),
            ],
            result,
=======
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
>>>>>>> ea919dca1357a724b0a905e12ab12df60763b6a7
        )


if __name__ == "__main__":
    unittest.main()
