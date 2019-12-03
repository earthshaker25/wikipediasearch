import webbrowser

def search_page_for_word(page,word):
    if word in page.content:
        print("The word '%s' is in this page!" % word)
    else:
        print("'%s' not found on this page" % word)

def search_multiple_pages_for_word(page,word):
        pass
    
def open_image(page,index):
    print("OPENING: %s" % page.images[index])
    webbrowser.open(page.images[index])
