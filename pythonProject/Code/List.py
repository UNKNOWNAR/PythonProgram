
class List:
    heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
    print(len(heros))#length of liat
    heros.append("black panther")#adds an elementn at the back of the list
    print(heros)
    heros.remove("black panther")#removes the first occurence of specific element
    heros.insert(3,"black panther")
    print(heros)
    heros[1:3] = ['doctor strange']
    print(heros)
    heros.sort()
    print(heros)