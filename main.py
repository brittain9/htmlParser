from get_html import GetHTML
from parse_html import ParseHTML


def UserGetHtmlFactory() -> GetHTML:
    while(True):
        url = input('Enter url: ')
        htmlObj = GetHTML(url)
        if(htmlObj.req_url):
            return htmlObj
        else:
            continue

if __name__ == "__main__":
    Obj = UserGetHtmlFactory()
    htmlStr = Obj.GetHtmlStr()

    ParseHTML.ParseHtml(htmlStr)
    

