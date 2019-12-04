import wikipedia
#SEARCHING FOR A SPECIFIC WORD AMONG MULTIPLE PAGES


global search_history_list
search_history_list = []

def search_history(pageslist):
    search_history_list.append(pageslist)
    return search_history_list

def store_original_length(olist):
    original_length_of_list = len(olist)
    print(original_length_of_list)
    return original_length_of_list

def multsearch(list1,word,contains=[]):
    pages = []
    notcontains = []
    #print("start/restart list1: %s" % list1)
    #print("start/restart contains: %s" % contains)
    #print("start/restart notcontains: %s" % notcontains)
    try:
        for v in list1: # Convert to wiki.page, add try block, now v = input value
            v = wikipedia.page(v)
            pages.append(v) # pages is a list of wiki.page
            #Now there is a list of wiki pages, v = wikipedia.page
            for c in pages: #c is each element of pages, c is content, p is title
                p = c.title
                c = c.content.lower()
                #print("Repeat contains %s" % contains)
                if word in c:
                    if p in contains:
                        #print("Doubles check")
                        continue
                    else:
                        contains.append(p)
                        print("%s: True" % p)
                else:
                    if p not in notcontains:
                        notcontains.append(p)
                        print("%s: False" % p)
                    else:
                        continue
    except wikipedia.exceptions.DisambiguationError:
        print("'%s' was too vague" % v) # v is input,list to use is list1
        correction = input("Please specify your term: ")
        #Get index of error
        errorindex = list1.index(v)
        #Replace with correction
        list1[errorindex] = correction
        #TESTS
        #print(list1)
        #print(contains)
        #Continues from error index, will change the length of list1
        multsearch(list1[errorindex:],word,contains)
    #Adjust so only prints if proper fraction
    print("Final %s " % contains) # Contains seems to keep variables, find a way to reset contains
    print("Final not%s " % notcontains)
    if (len(contains)/len(list1)) <= 1:
        print("Result: %s/%s contain the word '%s'" % (len(contains),len(list1),word))
    #Reset lists, not working.
    page = []
    contains = []
    notcontains = []
    print(contains,notcontains)

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
