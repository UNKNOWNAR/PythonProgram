class RecursiveGCD:
    def GCD(self,num1,num2):
        if num1<num2:
            num1, num2 = num2, num1
        if num1%num2==0:
            return num2
        return self.GCD(num2,num1%num2)
if __name__=="__main__":
    obj = RecursiveGCD()
    print(obj.GCD(6,35))