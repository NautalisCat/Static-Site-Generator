from textnode import *
print("Hello world")
def main():
    dummy = TextNode("Help, I've fallen and I can't get up", TextType.CODE, "https://www.youtube.com/watch?v=q9jhpOtubII")
    dummy.__repr__()
if __name__ == '__main__':
    main()
