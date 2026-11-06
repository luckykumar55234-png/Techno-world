num = int(input("Enter a number: "))

prime_numbers = []

if num > 1:
    for i in range(2, num + 1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

print("Prime numbers:",prime_numbers)
      
   
    
