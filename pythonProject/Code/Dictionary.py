phonebook = {"Tom": 69658158513, "Bob": 854416846416}
print(phonebook)
phonebook["Arinjay"] = 7003828489
print(phonebook)
del phonebook["Bob"]
print(phonebook)
phonebook["Tanurjay"] = 7003828488
for key in phonebook:
    print("Name:-", key, "Number:-", phonebook[key])
for k, v in phonebook.items():
    print("Name:-", k, "Number:-", v)
print("Tom" in phonebook)
print("Tomeshwari" in phonebook)
phonebook.clear()
print(phonebook)