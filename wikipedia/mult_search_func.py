import wikipedia

def multsearch(list1,word):
    pages = []
    contains = []
    try:
        for v in list1: # Convert to wiki.page, add try block
            v = wikipedia.page(v)
            pages.append(v)
            #Now there is a list of wiki pages
            for c in pages:
                p = c.title
                c = c.content
                if word in c:
                    if p not in contains:
                        contains.append(p)
                        print("%s: True" % p)
                    elif p in contains:
                        continue
                else:
                    print("%s: False" % p)
    except wikipedia.exceptions.DisambiguationError:
        pass
    print("Result: %s/%s contain the word '%s'" % (len(contains),(len(list1)),word))

