import json

# Create a dictionary 'book' and populate it with data
book = {}
book['tom'] = {
    'name': 'tom',
    'address': '1 red street, NY',
    'phone': 98989898
}
book['bob'] = {
    'name': 'bob',
    'address': '1 green street, NY',
    'phone': 234
}

# Convert the dictionary to a JSON string
s = json.dumps(book)

# Specify the full file path where you want to save the JSON data
with open("E:\\Python Folders\\pythonProject\\files\\book.txt", "w") as f:
    f.write(s)