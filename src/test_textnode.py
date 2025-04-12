import unittest

from textnode import *
from htmlnode import *
from split_nodes import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_noteq_url(self):
          node = TextNode("This is a text node", TextType.CODE)
          node2 = TextNode("This is a text node", TextType.CODE, "https://www.yahoo.com")
          self.assertNotEqual(node, node2)
    def test_noteq_enum(self):
          node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
          node2 = TextNode("This is a text node", TextType.CODE, "https://www.google.com")
          self.assertNotEqual(node, node2)
    def test_noteq_content(self):
          node = TextNode("wassup, foo?", TextType.BOLD, "https://www.google.com")
          node2 = TextNode("Howdy, partner?", TextType.CODE, "https://www.google.com")
          self.assertNotEqual(node, node2)
  
    def test_text(self):
            node = TextNode("This is a text node", TextType.TEXT)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")
    def test_TextType(self):
      node = TextNode("This is text with a `code block` word", TextType.TEXT)
      new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
      self.assertEqual(new_nodes[0].text, "This is text with a ")
      
    def test_italic(self):
      node = TextNode("This is text with an _italic_ block word", TextType.TEXT)
      new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
      self.assertEqual(new_nodes[1].text, "italic")


if __name__ == "__main__":
    unittest.main()
