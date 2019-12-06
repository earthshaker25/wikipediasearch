#import wikipedia
#BASIC FUNCTIONS FOR QUERY GIVEN, TECHNICALLY UNNECESSARY


def get_name(page):
    print("Page name: %s" % page.title)


def get_url(page):
    print("Page URL: %s" % page.url)


def get_summary(page):
    print(page.summary)


def get_content(page):
    print(page.content)


def get_images(page):
    print(page.images)


def get_links(page):
    print(page.links)


def get_categories(page):
    print(page.categories)


def get_references(page):
    print(page.references)


def get_sections(page):
    print(page.sections)
