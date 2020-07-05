"""Convert an XML string to an n-ary tree"""


# Creating class for type of XML Element
class XmlElementType:

    ELEMENT_UNKNOWN = 1
    ELEMENT_OPENING_TAG = 2
    ELEMENT_CLOSING_TAG = 3
    ELEMENT_TEXT = 4


# Creating class for the element itself
class XmlElement:

    def __init__(self):
        self.element_type = XmlElementType.ELEMENT_UNKNOWN
        self.node_name = ""


# Creating tokenizer class for the xml doc
class XmlTokenizer:

    def __init__(self, xml_str):
        self.xml = xml_str
        self.current_index = 0

    def get_next_element(self, element):

        idx = self.xml.find("<", self.current_index)

        if idx == -1:
            return False

        temp = self.xml[self.current_index:idx]
        temp = temp.strip()

        if len(temp) != 0:
            element.node_name = temp
            element.element_type = XmlElementType.ELEMENT_TEXT

            self.current_index = idx
            return True

        j = self.xml.find(">", idx)

        if self.xml[idx+1] == '/':
            element.node_name = self.xml[idx+2:j]
            element.element_type = XmlElementType.ELEMENT_CLOSING_TAG

        else:
            element.node_name = self.xml[idx+1:j]
            element.element_type = XmlElementType.ELEMENT_OPENING_TAG

        self.current_index = j + 1
        return True


# Creating Node class for the element
class Node:

    def __init__(self, name):
        self.node_name = name
        self.children = []


def create_xml_tree(xml):

    tok = XmlTokenizer(xml)
    element = XmlElement()

    if tok.get_next_element(element) is False:
        return None

    stack = []
    root = Node(element.node_name)
    stack.append(root)

    while tok.get_next_element(element) is True:

        n = None

        if (element.element_type == XmlElementType.ELEMENT_OPENING_TAG) or (element.element_type == XmlElementType.ELEMENT_TEXT):
            n = Node(element.node_name)
            stack[-1].children.append(n)

        if element.element_type == XmlElementType.ELEMENT_OPENING_TAG:
            stack.append(n)

        elif element.element_type == XmlElementType.ELEMENT_CLOSING_TAG:
            stack.pop()

    return root


# Trim Spaces from both sides
def trim(stack):
    print(stack.strip())


def print_tree(root, depth):

    if not root:
        return

    for x in range(0, depth):
        print(end="\t")

    print(root.node_name)

    for x in range(0, len(root.children)):
        print_tree(root.children[x], depth + 1)


xml = "<xml><data>hello world     </data>    <a><b></b><b><c></c></b></a></xml>"
head = create_xml_tree(xml)

print_tree(head, 0)
