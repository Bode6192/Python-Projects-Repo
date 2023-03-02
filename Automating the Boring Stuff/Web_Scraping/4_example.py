import os, requests, bs4



# Example 1

# res = requests.get('http://nostarch.com')

# print(res.raise_for_status)

# noStarchSoup = bs4.BeautifulSoup(res.text)

# print(type(noStarchSoup))

print()



# Example 2

exampleFile = open('4_example.html')

exampleSoup = bs4.BeautifulSoup(exampleFile.read())

elems = exampleSoup.select('#author')

print(elems)

print(type(elems))

print(len(elems))

# The input to the type() is indexed because the elems could 
# returns more than one tags depending on how many of the 
# requested tag is in the HTML File. 
print(type(elems[0]))

print(elems[0].getText())

print(elems[0])

print(elems[0].attrs)

print()



# Example 3

pElems = exampleSoup.select('p')

print(str(pElems[0]))

print(pElems[0].getText())

print(pElems[1])

print(pElems[1].getText())

print(str(pElems[2]))

print(pElems[2].getText())

exampleFile.close()



# Example 4
# Getting Data from an Element's Attributes

soup = bs4.BeautifulSoup(open('4_example.html'))

spanElem = soup.select('span')[0]

print(spanElem)

print(spanElem.get('id'))

print(spanElem.get('some_nonexistent_addr') == None)

print(spanElem.attrs)