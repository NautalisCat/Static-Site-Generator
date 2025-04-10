import unittest

from textnode import TextNode, TextType


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
  


if __name__ == "__main__":
    unittest.main()
