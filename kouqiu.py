import random

def insert_dots(string):
    result = "（透过口球）"
    for i, char in enumerate(string):
        dots = random.randint(2, 4) * '.'
        if (i + 1) % random.randint(3, 6) == 0:
            r = random.random()
            if r < 0.25:
                result += '.啊' + dots + char
            elif r < 0.70:
                result += '.嗯' + dots + char
            else:
                result += '.唔' + dots + char
        else:
            result += dots + char
        if (i + 1) % random.randint(4, 16) == 0:
            result = result[:-1]
    return result

user_input = input("请输入字符串: ")
result_string = insert_dots(user_input)
print(result_string)
