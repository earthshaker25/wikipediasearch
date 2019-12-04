from basic_func import *
from search_func import *
from content_to_list import *

#INPUTS FOR QUERY GIVEN

def query_given(query):
    while True:
#Get input
        do = input("Query actions: ")
#Basic info
        if "name" == do:
            get_name(query)
        elif "url" == do:
            get_url(query)
        elif "summary" == do:
            get_summary(query)
        elif "content" == do:
            get_content(query)
        elif "images" == do:
            get_images(query)
        elif "links" == do:
            get_links(query)
        elif "categories" == do:
            get_categories(query)
        elif "references" == do:
            get_references(query)
        elif "sections" == do:
            get_sections(query)
#Extra Special Functions from search_func
        elif "search" in do:
            sw = do[7:]
            search_page_for_word(query,sw)
        elif "searches" in do:
            getwords = input("Enter list of words separated by commas: ")
            words = list(getwords.split(","))
            wordssearch(words,query)
        elif "report sent" in do:
            n=1
            sw = do[12:]
            report_sentences(query,sw)
#Images and links with additional INDEX value
        elif "open image" in do:
            index = do[11:]
            index = int(index)
            print("You chose index %s" % index)
            open_image(query,index)
        elif "open link" in do:
            index = do[10:]
            index = int(index)
            print("You chose index %s" % index)
            open_link(query,index)
        elif "len list images" in do:
            print(len(query.images))
        elif "len list links" in do:
            print(len(query.references))
#Exit options
        elif "quit" in do:
            print("Query actions exited")
            break
        elif "new" in do:
            print("Rerouting to general actions")
            break
