#Write a Python program to convert an integer to a string in any base using recursion
class RecursiveBaseConversion:
    def character(self,number):
        if number <10:
            return number
        elif number<36:
            number+=55# Adjust for uppercase letters
            return chr(number)# A-Z (10-35)
        else:
            number+=71# Adjust for lowercase letters
            return chr(number)# a-z (36-61)

    def base_conversion(self,number,base):
        if number<base:
            return self.character(number)
        return self.base_conversion(number//base,base)+self.character(number % base)
if __name__=="__main__":
    obj = RecursiveBaseConversion()
    print(obj.base_conversion(476087,31))
    print(obj.base_conversion(42520,35))
    print(obj.base_conversion(20071180,29))