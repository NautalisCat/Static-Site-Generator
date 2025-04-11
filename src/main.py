from textnode import *
from htmlnode import *
print("Hello world")
def main():
    dummy = TextNode("Help, I've fallen and I can't get up", TextType.CODE, "https://www.youtube.com/watch?v=q9jhpOtubII")
    dummy.__repr__()

    dict_holder = {
    "href": "https://www.google.com",
    "target": "_blank",
}
    dummy2 = htmlnode("p", "Text goes here", "1", dict_holder)
    htmlnode_string = dummy2.props_to_html()
    print(htmlnode_string)
    dummy2.__repr__()

    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(type(html_node))
    print(html_node.value)

if __name__ == '__main__':
    main()
