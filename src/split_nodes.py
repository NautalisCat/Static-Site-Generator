from textnode import *
from htmlnode import *
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
         new_node = TextNode(node.text,node.text_type)
         node_list.append(new_node)
        else:
           new_list = node.text.split(delimiter)
           if len(new_list) % 2 == 0:
              raise Exception ("Invalid Markdown syntax, unmatched delimiters")
           for i in range(len(new_list)):
              if new_list[i] != "": 
                 if i % 2 == 0:
                    node_list.append(TextNode(new_list[i], TextType.TEXT))
                 else:
                     node_list.append(TextNode(new_list[i], text_type))
    return node_list
              
              
       


           
