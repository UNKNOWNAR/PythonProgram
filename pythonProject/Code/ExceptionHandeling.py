x = input("Enter Number1:- ")
y = input("Enter Number2:- ")
try:
    z = int(x)/int(y)
except Exception as e:
    print("Exception occured:- ",e)
    z = 'None'
print("Result:- ",z)

class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception",self.msg)

try:
    raise Accident("crash between two cars")
except Accident as e:
    e.print_exception()
def file_processing():
    try:
        f = open("E:\\Python Folders\\pythonProject\\files\\book1.txt", "r")
        x=1/0
    except FileNotFoundError as e:
        print("inside exception")
    finally:#these closes the file even though there is an exception
        print("closed file")
        f.close()
file_processing()
