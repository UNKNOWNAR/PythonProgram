start = int(input("Enter the starting digit:- "))
end = int(input("Enter the funal digit:- "))+1
for i in range(start,end):
    print (i);
exp=[2340, 2500, 2100, 3100, 2980]
total=0
for i in range (len (exp)):
    print('Month:', (i+1), 'Expense:', exp[i])
    total = total + exp[i]
print('Total expense is:', total)
i = 1;
while i<=5:
    print(i)
    i+=1