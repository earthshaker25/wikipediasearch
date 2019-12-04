#import wikipedia

#Functions for finding indices
def find_image_index(page,find):
    l = page.images
    for i in l:
        if find in i:
            print("'%s' found at index: %s" % (find, l.index(i)))
        else:
            continue

def find_reference_index(page,find):
    l = page.references
    for i in l:
        if find in i:
            print("'%s' found at index: %s" % (find, l.index(i)))
        else:
            continue
