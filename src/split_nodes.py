from textnode import *
from htmlnode import *
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
         new_node = TextNode(node.text,node.text_type, node.url)
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
             
             
def extract_markdown_images(text):
   matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
   return matches
   
def extract_markdown_links(text):
   matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
   return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    node_list = []
    for node in old_nodes:
      if node.text_type != TextType.TEXT:
         node_list.append(node)
         continue
      origin_text = node.text
      links = extract_markdown_links(origin_text)
      if len(links) == 0:
            node_list.append(node)
            continue
      for link in links:
          sections = origin_text.split(f"[{link[0]}]({link[1]})", 1)
          if sections[0] !="":
             node_list.append(TextNode(sections[0], TextType.TEXT))
          node_list.append(TextNode(link[0], TextType.LINK, link[1]))
          origin_text = sections[1]
      if origin_text != "":
          node_list.append(TextNode(origin_text, TextType.TEXT))
    return node_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD )
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC )
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE )
    return nodes

