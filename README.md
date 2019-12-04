# WikipediaSearch

To get help, type -h<br/>

## When presented with prompt "Next: "

To search for a wikipedia page: `search x`<br/>
To set a main wikipedia page: `new`<br/>
To list sentences containing a single word: `report sent x`<br/>

###### Mult Search
To search multiple pages for words: `mult x`<br/>
Separate search terms with the '&' symbol<br/>
*Known problems: If a page checks false for all terms, it will list only the first search term as false. Pages will end up on both contains and notcontains list, which must be fixed.*

## If you have set a page to work with prompt "Query actions: "

### Listing Information
To print the title of the page: `name`<br/>
To print the URL of the page: `url`<br/>
To print the sections of the page: `sections`<br/>
To print the summary of the page: `summary`<br/>
To print the content of the page: `content`<br/>
To print a list of the images on the page: `images`<br/>
To print a list of the references on the page (openable urls): `references`<br/>
To print a list of links on the page (not openable): `links`<br/>

### Searching for Information
To report if a single word is found in the content: `search x`<br/>
To report from a list of words what words are found in the content: `mult x`<br/>
To list the sentences that contain a single word: `report sent x`<br/>

To find the number of images: `len list images`<br/>
To find the number of references: `len list references`<br/>
To find the index of an image: `find index image`<br/>
To find the index of a reference: `find index reference`<br/>

### Opening Images or References in a new Window
To open an image: `open image x`<br/>
To open a reference: `open reference x`<br/>


To quit the program: quit
