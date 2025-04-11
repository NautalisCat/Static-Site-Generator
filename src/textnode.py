from enum import Enum
from htmlnode import *
        
class TextType(Enum):
    TEXT = 'text'
    ITALIC = "italic"
    BOLD = "bold"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(node1, node2 ):
        return (node1.text == node2.text and 
        node1.text_type == node2.text_type and
        node1.url == node2.url
    )
    def __repr__(TextNode):
        print(f"TextNode({TextNode.text}, {TextNode.text_type.value}, {TextNode.url})")

    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return leafnode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return leafnode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return leafnode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return leafnode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return leafnode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return leafnode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")