def gcd(a,b):
    while b:
        a,b = b,a % b
    return a
def common_divisors(num1,num2):
    g = gcd(num1,num2)
    divisors = [i for i in range(1,g+1) if g%i == 0]
    return divisors
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))

common_divs= common_divisors(num1,num2)

print("مقسوم عليه هاي مشترک به صورت نزولي :",
sorted(common_divs, reverse=True))

if common_divs:
    max_common_divisor = max(common_divs)
    min_common_divisor = min(common_divs)
    print("بزرگترين مقسوم عليه مشترک :",
max_common_divisor)
    print("کوچکترين مقسوم عليه مشترک :",
min_common_divisor)
else:
    print("هيچ مقسوم عليه مشترکي وجود ندارد.")
         
