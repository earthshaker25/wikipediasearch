#Working Code
import wikipedia
import webbrowser
from search_func import *
from basic_func import *

#keep this in wiki.py
while True:
    try:
        search = input("Enter your initial query: ")
        query = wikipedia.page(search)
    except wikipedia.exceptions.DisambiguationError:
        check = input("Be more specific! Would you like a list of all relevant pages? [y/n]: ")
        if "y" in check:
            print(wikipedia.search(search,results=100))
            continue
        else:
            continue
    print("Intial Query Found: %s" % query)
    break

#Function to change query, keep in wiki py
def get_new_query():
    while True:
        try:
            search = input("Enter new search term: ")
            #Important element to change the 'query' variable
            global query
            query = wikipedia.page(search)
        except wikipedia.exceptions.DisambiguationError:
            check = input("Be more specific! Would you like a list of all relevant pages? [y/n]: ")
            if "y" in check:
                print(wikipedia.search(search,results=100))
                continue
            else:
                continue
        print("New Query Found: %s" % query)
        return query
        break

#Keep this in wiki.py, input reciever
while True:
    #Input Line
    do = input("Next: ")
    #Basic Page Functions
    if "name" in do:
        get_name(query)
    elif "url" in do:
        get_url(query)
    elif "summary" in do:
        get_summary(query)
    elif "content" in do:
        get_content(query)
    elif "images" in do:
        get_images(query)
    elif "links" in do:
        get_links(query)
    #Extra Special Functions
    elif "search" in do:
        sw = do[7:]
        search_page_for_word(query,sw)
    elif "open image" in do:
        index = do[11:]
        index = int(index)
        print("You chose index %s" % index)
        open_image(query,index)
    elif "len list" in do:
        print(len(query.images))
    #Special functions
    elif "quit" in do:
        break
    elif "new" in do:
        get_new_query() #keep funcdef in wiki.py
    elif "-h" in do:
        print("Useful commands: Title of page: name, Page URL: url, Content, images, links, Search for a word: search")
    else:
        print("Command not found! Please try again!")
