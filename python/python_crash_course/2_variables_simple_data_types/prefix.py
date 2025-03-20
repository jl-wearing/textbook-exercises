#The removeprefix() method is used to remove a prefix, e.g. https:// from a url.

url = 'https://www.nostarch.com'
url_prefix_removed = url.removeprefix('https://')

print(url)
print(url_prefix_removed)

food = "Pork: Bacon Sausage Ribs"
print(food.removeprefix('Pork: '))