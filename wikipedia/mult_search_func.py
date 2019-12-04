import wikipedia
#SEARCHING FOR A SPECIFIC WORD AMONG MULTIPLE PAGES


global search_history_list
search_history_list = []
    
def search_history(pageslist):
    search_history_list.append(pageslist)
    return search_history_list

def multsearch(list1,word):
    pages = []
    contains = []
    notcontains = []
    try:
        for v in list1: # Convert to wiki.page, add try block, now v = input value
            v = wikipedia.page(v)
            pages.append(v)
            #Now there is a list of wiki pages, v = wikipedia.page
            for c in pages:
                p = c.title
                c = c.content.lower()
                if word in c:
                    if p not in contains:
                        contains.append(p)
                        print("%s: True" % p)
                    elif p in contains:
                        continue
                else:
                    notcontains.append(p)
                    print("%s: False" % p)
    except wikipedia.exceptions.DisambiguationError:
        print("'%s' was too vague" % v) # v is input,list to use is list1
        correction = input("Please specify your term: ")
        #Get index of error
        errorindex = list1.index(v)
        #Replace with correction
        list1[errorindex] = correction
        #Run function again with new list
        print(list1)
        print(contains)
        #Continue from error index? Decide. Right now it does the whole list
        multsearch(list1,word)
    print("Result: %s/%s contain the word '%s'" % (len(contains),(len(list1)),word))
    #Reset lists, necessary?
    page = []
    contains = []
    notcontains = []

#SING WORD FOR CONTENT PRINT

def singsearch(page,word):
    page = wikipedia.page(page)
    if word in page.content:
        print("'%s' was found on this page!" % word)
        return True
    else:
        print("'%s' not found" % word)
        return False

def wordssearch(words,page):
    for i in words:
        if i in page.content:
            print("%s: True" % i)
        elif i not in page.content:
            print("%s: False" % i)
