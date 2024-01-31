import random


def generate(num):
    result = ""
    count = 0
    min_length = 4
    if num > min_length:
        while count < num:
            # The distribution of the password is 1/3 : lower case letters, 1/3 upper case letters
            # and the rest as numbers
            # Generates the lower case letters
            if count < num//3:
                result += chr(random.randint(65, 90))
                count += 1
            # Generates the upper case letters
            elif count < 2*(num//3):
                result += chr(random.randint(97, 122))
                count += 1
            # Generates the numbers
            else:
                result += chr(random.randint(48, 57))
                count += 1
        # randomly shuffles the result
        result = ''.join(random.sample(result, len(result)))
    else:
        result = "Password must be al least 4 characters !"
    return result

p1 = generate(3)
print(p1)
# print(len(p1))