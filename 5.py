user = int(input("Введите целое десятичное число: "))
k = 0
N = user
while user > 0 :
    x = user % 10
    user = user // 10
    if (x!=0) and (x%2==0):
        k = k+1
    
print("Сумма четных цифр в числе ", N ," равна ", k)


