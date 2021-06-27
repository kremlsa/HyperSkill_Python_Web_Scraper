import requests

print("Input the URL:")
url_ = input()
print()
response = requests.get(url_)
if response.status_code != 200:
    print("The URL returned {}!".format(response.status_code))
    exit(0)
source = response.content
with open('source.html', 'wb') as file:
    file.write(source)
print("Content saved.")
