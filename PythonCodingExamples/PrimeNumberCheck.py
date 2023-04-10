# Natural number > 1
# Which has only 2 factors 1 and itself

# 19 => 1 and 19 => Prime Number
# 28 => 1,2,4,7,14,28 => Not a Prime Number
num = 19
count = 0

if num > 1:
    for i in range(1, num + 1):
        if(num % i) == 0:
            count = count + 1
            print(count)
    if count == 2:
        print("Number is Prime")
    else:
        print("Number is Not Prime")
