from textnode import *
from htmlnode import *
from copy_static import *
from generate_page import *
def main():
    print("Hello, this is main!")
    param1 = "/Users/sleeper/Dev/Static-Site-Generator/content/index.md"
    param2 = "/Users/sleeper/Dev/Static-Site-Generator/template.html"
    param3 = "/Users/sleeper/Dev/Static-Site-Generator/content/public/index.html"
    recurs_filecopy(static_directory, public_directory)
    generate_page(param1,param2, param3)
if __name__ == '__main__':
    main()
