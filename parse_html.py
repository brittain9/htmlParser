from bs4 import BeautifulSoup

class ParseHTML:
    def ParseHtml(htmlStr):
        parsed = BeautifulSoup(htmlStr, 'html.parser')
        print(parsed.prettify())
