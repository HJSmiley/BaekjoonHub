str = input()

if (not str) or (str == '"') or (str == '""') or (str[0] != '"' or str[-1] != '"'):
    print("CE")
else:
    print(str[1:-1])
