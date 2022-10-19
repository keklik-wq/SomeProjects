import os


while True:
    operation=input().split()
    if operation[0]=='cmd':
        print(os.getcwdb())
    if operation[0]=='cd':
        os.chdir(operation[1])
    if operation[0]=='touch':
        file = open(f"{operation[1]}", 'w')
        file.close()
    if operation[0]=='cat':
        try:
            file=open(f"{operation[1]}", 'r')
            content=file.read()
            print(*content)
            file.close()
        except:
            print("Incorrect file name")
    if operation[0] == 'ls':
        print(*os.listdir())
    if operation[0] == 'rm':
        try:
            os.remove(f'{operation[1]}')
        except:
            print("Incorrect file name")