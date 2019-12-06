import wikipedia
from mult_search_func import singsearch  # Will receive word searching function
from termcolor import cprint


# RETURN SENTENCES WITH GIVE WORD - THIS IS WHERE INPUT FUNCTION WILL GO


# Pretend singsearch defined here ():


def content_to_list(page):
    a = wikipedia.page(page)
    a = a.content
    global sentences
    sentences = list(a.split("."))
    return sentences


# Needs to check if word is on page
# Needs to make a list of the contents
# Needs to return a list of sentences (with for)


def report_sentences(page, word):
    global n
    n = 1
    x = singsearch(page, word)
    if x:
        content_to_list(page)
        for y in sentences:
            if word in y:
                n += 1
                print("%s. %s" % (n, y))
            else:
                continue
    elif not x:
        cprint("Word not found anywhere on the page. Returning.", 'red')
        return
