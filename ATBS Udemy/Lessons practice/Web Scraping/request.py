import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

print(res.status_code == requests.codes.ok)
print(len(res.text))

print(res.text[:100])

#get the status code for the site. 200 is for success.

print(res.status_code)

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
