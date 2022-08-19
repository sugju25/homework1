
def main(str1, str2):
    if isinstance(str1,str) == isinstance(str2, str):
        return 0
    elif str1 == str2:
        return 1
    elif str1  is not str2 and len(str1)>len(str2):
        return 2
    elif str1 is not str2 and str2 =='learn':
        return 3

print(main('2', 'lel'))
print(main('lol','lol'))
print(main('l', 'lmao'))
print(main('len', 'learn'))