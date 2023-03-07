from getHTML import GetHTML
# def parseHtml(str_html):
#     from bs4 import BeautifulSoup

#     parsed = BeautifulSoup(str_html, 'html.parser')
#     print(parsed.prettify())

if __name__ == "__main__":

    while(True):
        url = input('Enter url: ')

        htmlObj = GetHTML(url)
        
        if(htmlObj.url_for_request):
            break
        else:
            continue

    htmlStr = htmlObj.GetHtmlStr()
    print(htmlStr)