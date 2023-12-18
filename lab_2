def check(str):
    brackets = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    f = False
    for k in range(len(str)):
        if str[k] in "{}[]()":
            brackets[str[k]] += 1
            if brackets['('] < brackets[')'] or brackets['['] < brackets[']'] or brackets['{'] < brackets['}']:
                f = True
                break
    if f or brackets['('] != brackets[')'] or brackets['['] != brackets[']'] or brackets['{'] != brackets['}']:
        return False
    else:
        return True


def func(str):
    if '(' in str:
        cur = str.index("(")
        end = str.index(")")
        while not check(str[cur+1:end]):
            end += str[end + 1:].index(")") + 1
        return func(str[:cur] + func(str[cur + 1:end]) + str[end + 1:])
    elif "*" in str and "/" in str:
        if str.index("*") < str.index("/"):
            i = str.index("*")
            cur = i - 1
            end = i + 1
            while cur > -1 and str[cur] in "0123456789":
                cur -= 1
            while end < len(str) and str[end] in "0123456789":
                end += 1
            res = "{}".format(int(int(str[cur + 1:i]) * int(str[i + 1:end])))
            return func(str[:cur+1] + res + str[end:])
        else:
            i = str.index("/")
            cur = i - 1
            end = i + 1
            while cur > -1 and str[cur] in "0123456789":
                cur -= 1
            while end < len(str) and str[end] in "0123456789":
                end += 1
            res = "{}".format(int(int(str[cur + 1:i]) / int(str[i + 1:end])))
            return func(str[:cur+1] + res + str[end:])
    elif "*" in str:
        i = str.index("*")
        cur = i - 1
        end = i + 1
        while cur > -1 and str[cur] in "0123456789":
            cur -= 1
        while end < len(str) and str[end] in "0123456789":
            end += 1
        res = "{}".format(int(int(str[cur + 1:i]) * int(str[i + 1:end])))
        return func(str[:cur+1] + res + str[end:])
    elif "/" in str:
        i = str.index("/")
        cur = i - 1
        end = i + 1
        while cur > -1 and str[cur] in "0123456789":
            cur -= 1
        while end < len(str) and str[end] in "0123456789":
            end += 1
        res = "{}".format(int(int(str[cur + 1:i]) / int(str[i + 1:end])))
        return func(str[:cur+1] + res + str[end:])
    elif "+" in str and "-" in str:
        if str.index("+") < str.index("-"):
            i = str.index("+")
            cur = i - 1
            end = i + 1
            while cur > -1 and str[cur] in "0123456789":
                cur -= 1
            while end < len(str) and str[end] in "0123456789":
                end += 1
            res = "{}".format(int(str[cur + 1:i]) + int(str[i + 1:end]))
            return func(str[:cur+1] + res + str[end:])
        else:
            i = str.index("-")
            cur = i - 1
            end = i + 1
            while cur > -1 and str[cur] in "0123456789":
                cur -= 1
            while end < len(str) and str[end] in "0123456789":
                end += 1
            res = "{}".format(int(str[cur + 1:i]) - int(str[i + 1:end]))
            return func(str[:cur+1] + res + str[end:])
    elif "+" in str:
        i = str.index("+")
        cur = i - 1
        end = i + 1
        while cur > -1 and str[cur] in "0123456789":
            cur -= 1
        while end < len(str) and str[end] in "0123456789":
            end += 1
        res = "{}".format(int(str[cur + 1:i]) + int(str[i + 1:end]))
        return func(str[:cur+1] + res + str[end:])
    elif "-" in str:
        i = str.index("-")
        cur = i - 1
        end = i + 1
        while cur > -1 and str[cur] in "0123456789":
            cur -= 1
        while end < len(str) and str[end] in "0123456789":
            end += 1
        res = "{}".format(int(str[cur + 1:i]) - int(str[i + 1:end]))
        return func(str[:cur+1] + res + str[end:])
    str.replace("=", "")
    return str.replace("=", "")


s = input()
if check(s) and "/0" not in s:
    print(func(s))
else:
    print("err")
