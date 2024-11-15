f = open("E:\\Python Folders\\pythonProject\\files\\book1.txt", "a")
f.write("I Love Python")
f.write("\nI Love Java")
f.write("\nI Love C++")
f.write("\nI Love Kotlin")
f = open("E:\\Python Folders\\pythonProject\\files\\book1.txt", "r")
print(f.read())
f.seek(0)
for line in f:
     line += " "
     length = len(line)
     i = 0
     flag = 0
     while i!=length:
         c = line[i]
         if c==' ':
             flag+=1
         i+=1
     print(flag)
f.close()