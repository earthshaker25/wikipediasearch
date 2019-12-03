#import wikipedia
#BASIC FUNCTIONS FOR QUERY GIVEN

def get_name(page):
    print("Page name: %s" % page.title)

def get_url(page):
    print("Page URL: %s" % page.url)
    
def get_summary(page):
    print(page.summary)

def get_content(page):
    print(page.content)

def get_images(page):
    print(page.images)

def get_links(page):
    print(page.links)
