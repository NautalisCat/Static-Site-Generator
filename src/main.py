from textnode import *
from htmlnode import *
from copy_static import *
print("Hello world")
def main():
    dummy = TextNode("Help, I've fallen and I can't get up", TextType.CODE, "https://www.youtube.com/watch?v=q9jhpOtubII")
    dummy.__repr__()

    dict_holder = {
    "href": "https://www.google.com",
    "target": "_blank",
    }
    recurs_filecopy(static_directory, public_directory)

if __name__ == '__main__':
    main()
