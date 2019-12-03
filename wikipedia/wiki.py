#MAIN CODE
import wikipedia
from search_func import *
from basic_func import *
from mult_search_func import multsearch
from query_def import * #give query options

#Function to define and work with a query
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
        query_given(query) #from import
        break

#Input reciever without defined query
while True:
    #Input Line
    do = input("Next: ")
    #Basic Page Functions
    if "new" in do:
        get_new_query() #keep funcdef in wiki.py
    elif "mult search" in do:
        sw = do[12:]
        pagesdata = input("Enter pages separated by comma: ")
        pageslist = list(pagesdata.split(","))
        multsearch(pageslist,sw)
    #Special functions
    elif "quit" in do:
        break
    elif "-h" in do:
        print("Useful commands: Title of page: name, Page URL: url, Content, images, links, Search for a word: search")
    else:
        print("Command not found! Please try again!")
