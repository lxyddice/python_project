import random

def insert_dots(string):
    # 开头加入（透过口球）
    result = "（透过口球）"

    # 遍历输入字符串的每个字符
    for i, char in enumerate(string):
        # 随机生成3-5个点号.
        dots = random.randint(2, 4) * '.'

        # 每隔3-6个字符插入
        if (i + 1) % random.randint(3, 6) == 0:
            # 30%几率为“啊”，70%为“嗯”
            r = random.random()
            if r < 0.3:
                result += '.啊' + dots + char
            else:
                result += '.嗯' + dots + char
        else:
            result += dots + char

        # 每隔10-20个字符删除一个字符
        if (i + 1) % random.randint(4, 16) == 0:
            result = result[:-1]

    return result

# 输入字符串
user_input = input("请输入字符串: ")

# 调用函数插入字符和删除字符
result_string = insert_dots(user_input)

# 输出结果
print(result_string)
