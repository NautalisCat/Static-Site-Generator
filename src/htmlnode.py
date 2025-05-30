class htmlnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        holder = ""
        for keys, values in self.props.items():
            holder += str((f" {keys}:\"{values}\" "))
        return holder
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class leafnode(htmlnode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(htmlnode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        temp_string = ""
        if self.tag is None:
            raise ValueError("No tag")
        if self.children is None:
            raise ValueError("No children tags")
        for child in self.children:
            temp_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{temp_string}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.props})"