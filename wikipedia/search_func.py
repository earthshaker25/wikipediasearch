import webbrowser
import sys
from termcolor import colored,cprint

#SEARCH FUNCTIONS FOR QUERY GIVEN

def search_page_for_word(page,word):
    if word in page.content.lower():
        print("The word '%s' is in this page!" % word)
    else:
        print("'%s' not found on this page" % word)

def search_multiple_pages_for_word(page,word):
        pass
    
def open_image(page,index):
    cprint("OPENING: %s" % page.images[index],'green')
    webbrowser.open(page.images[index])

def open_reference(page,index):
    cprint("OPENING: %s" % page.references[index],'green')
    webbrower.open(page.references[index])
