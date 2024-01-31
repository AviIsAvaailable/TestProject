import random


# p1 = generate12()
def generate(num):
    result = ""
    count = 0
    if num > 4 :
        while count < num:
            if count < num//3:
                result += chr(random.randint(65, 90))
                count += 1
            elif count < 2*(num//3):
                result += chr(random.randint(97, 122))
                count += 1
            else:
                result += chr(random.randint(48, 57))
                count += 1
        result = ''.join(random.sample(result, len(result)))
    else:
        result = "Password must be al least 4 characters !"
    return result

p1 = generate(3)
print(p1)
# print(len(p1))