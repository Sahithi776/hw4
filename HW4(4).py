import string
import random
#Ways to build url shortner:
#Using functions,Using classes
#by using functions it is very limited. 
#by using Classes It helps to approach in many ways
class UrlShort():
    domain = 'https://www.geeksforgeeks.org/' 
    #created 3 methods for creating short URLs
    #checking short URLs, and finally customized short urls and update the URLs.


     
    def __init__(self):
         
        self.data = {}
    # here we are generating 5 random lowercase characters 
    #we append them to our domain URL, so that becomes our shortner URL.

 
    def create_shortURL(self,url):
         #shortURL: It allows us to create short URLs for the original URL. 
         #here we will store the original URL and generate a short URL
         
        chars = string.ascii_lowercase
        s_url = ''.join(random.choice(chars) for i in range(5))
        short_url = self.domain+s_url
             
        if not short_url  in self.data:
            self.data[short_url] = url
        else:
            for self.i in range(5):
                try:
                    s_url = ''.join(random.choice(chars) for i in range(5))
                    short_url = self.domain+s_url        
                 
                    if not short_url  in self.data:
                       self.data[short_url] = url
                       break
                except:
                    pass
                     
             
        print('------------ Your short URL was created!...............')
         
        print('Your URL:',url)
        print('Shorten URL:',short_url)
         
        return short_url
         
    def check_URL(self,url):
        #It allows us to check short urls. 
        #if it exist It will give you the stored original url 
        if url in self.data:
            print('\n.................url info.................')
            print('Your original url:',self.data[url.strip()])
        else:
            print('No url found HTTP404..!')
     
    def update_url(self,url):
        #It allows us to customize the short URL or update URL. 
        #overriding the randomly generated short URL.


        if url in self.data:
            self.data.pop(url.strip())
             
            main_url = input('Enter Your original URL:')
            short_url = input('enter shorturl')
            short_url = self.domain+short_url
             
            if short_url not in self.data and not main_url=='':
                self.data.update(short_url=main_url)
                print('\n.............Successfully updated..!..................')
                print('customized url:',short_url)
            else:
                print('Already taken..!')
        else:
            print('No data found ...!')
             
             
s = UrlShort()
url = s.create_shortURL('https://www.geeksforgeeks.org/python-language-advantages-applications/?ref=lbp') 
s.data  
s.check_URL(url)
 
s.update_url(url)  
