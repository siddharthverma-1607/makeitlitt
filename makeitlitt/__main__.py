"""When executing a package with python -m as you did earlier, Python runs the contents of __main__.py.
In other words, __main__.py acts as the entry point of your program and takes care of the main flow, calling other parts as needed:
eg- python -m makeitlitt"""

# __main__.py

import sys

#from makeitlitt import generate


def main():
    """Read the use cases from makeitlitt"""

    # If an article ID is given, then show the article
    if len(sys.argv) > 1:
        #article = feed.get_article(sys.argv[1])
        # viewer.show(article)
        print("arg passed")

    # If no ID is given, then show a list of all articles
    else:
        #site = feed.get_site()
        #titles = feed.get_titles()
        #viewer.show_list(site, titles)
        print("without arg passed")


if __name__ == "__main__":
    main()
