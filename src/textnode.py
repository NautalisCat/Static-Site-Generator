from enum import Enum

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
    
