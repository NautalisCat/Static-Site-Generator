import unittest
from htmlnode import *

class TestHtmlNode(unittest.TestCase):
    
    def test_check_string(self):
        temp_dict = {
        "href": "https://www.google.com",
         "target": "_blank",
        }
        node = htmlnode("b", "Text goes here now", "12", temp_dict)
        node_string = node.props_to_html()
        self.assertIn("https://www.google.com", node_string)


    def test_diff(self):
        node = htmlnode("b", "Text goes there")
        node2 = htmlnode("c", "Text does not goin here")
        self.assertNotEqual(node, node2)


    def test_repr(self):
        node = htmlnode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

class TestLeafNodeP(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = leafnode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

class TestLeafNodeB(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = leafnode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = leafnode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = leafnode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )



if __name__ == "__main__":
    unittest.main()
