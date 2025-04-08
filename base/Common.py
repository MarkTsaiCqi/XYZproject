import string, random
import random

# 获取随机数字
def create_random_string():
    """随机生成一个大写或小写的英文字母"""
    return random.choice(string.ascii_letters)

# 随机生成一串字母
def create_random_strings(number):
    """随机生成一串包含大写或小写的英文字母"""
    value = "".join([random.choice(string.ascii_letters) for _ in range(number)])
    return value

# 随机生成一串小写字母
def create_random_lower_letters(number):
    """随机生成一串包含大写或小写的英文字母"""
    value = "".join([random.choice(string.ascii_letters) for _ in range(number)])
    return value.lower()

def create_random_big_letters(number):
    """随机生成一串包含大写或小写的英文字母"""
    value = "".join([random.choice(string.ascii_letters) for _ in range(number)])
    return value.upper()

if __name__ == '__main__':
    asd = create_random_big_letters(4)
    print(asd)