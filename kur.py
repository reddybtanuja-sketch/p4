num=int (input("enter the fibonacci sequence length to be generated:"))
first_term=0
second_term=1
print("the fibonacci series with","num","term is :")
print(first_term,second_term,end=" ")
for i in range (2,num):
    curterm=first_term+second_term
    print(curterm,end=" ")
    first_term=second_term
    second_term=curterm
    print()
