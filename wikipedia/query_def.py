from basic_func import *
from search_func import *

#INPUTS FOR QUERY GIVEN

def query_given(query):
    while True:
        do = input("Query actions: ")
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
        #Extra Special Functions from search_func
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
        elif "quit" in do:
            print("Query actions exited")
            break
        elif "new" in do:
            print("Rerouting to general actions")
            break
