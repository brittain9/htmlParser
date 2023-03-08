from urllib.request import Request

class GetHTML:
    req_url = ''
    req_headers={'User-Agent': 'Mozilla/5.0'}
    req = None

    def __init__(self, url2valid):
        if GetHTML.ValidateURL(url2valid):
            self.req_url = url2valid
        else:
            print('Error while constructing. Invalid URL.')
        self.req = Request(url=self.req_url)
        

    def GetHtmlStr(self) -> str:
        '''Returns str of the HTML code'''
        from urllib.request import urlopen
        from urllib.error import HTTPError, URLError

        try:
            with urlopen(self.req) as httpReq:
                return httpReq.read()

        except HTTPError:
            print(HTTPError.code)
        except URLError:
            print(URLError.reason)  
        except:
            print('AB: Error')

    def ValidateURL(validate) -> bool:
        '''Returns True if URL is valid'''
        from validators import url

        if url(validate):
            return True
        return False