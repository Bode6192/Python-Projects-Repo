import requests 

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))

# The Response object has a status_code attribute that can be 
# checked against requests.codes.ok to see whether the download
# succeeded. 
print(res.status_code == requests.codes.ok)

print(len(res.text))

print()

print(res.text[:250])

print()

# Saving Downloaded Files to the Hard Drive.
# The iter_content() method returns chunks of byte data
# We could specify the number of bytes the method should 
# return
PlayFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    PlayFile.write(chunk)

PlayFile.close()


# Using Try and Except to catch error with the Response 
# method raise_for_status()
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))



