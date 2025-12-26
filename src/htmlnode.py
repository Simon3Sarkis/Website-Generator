class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""

        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result

    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag}, "
            f"value={self.value}, "
            f"children={self.children}, "
            f"props={self.props})"
        )
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("All lead nodes must have a value")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag should have a value")

        if self.children is None:
            raise ValueError("Children should have a value")

       
        props_str = ""
        if self.props:
            props_str = " " + " ".join(
                f'{key}="{value}"' for key, value in self.props.items()
            )

        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
