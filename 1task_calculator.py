if __name__ == '__main__':
    history=[['+'],['-'],['/'],['*']]
    while True:
        a = int(input())
        b = int(input())
        operation = input()
        if operation=="+":
            c=f'{a}+{b}={a+b}'
            print(c)
            history[0].append(c)
        elif operation=="-":
            c=f'{a}-{b}={a-b}'
            print(c)
            history[1].append(c)
        elif operation=="*":
            c=f'{a}*{b}={a*b}'
            print(c)
            history[3].append(c)
        elif operation=="/":
            c=f'{a}/{b}={a/b}'
            print(c)
            history[2].append(c)
        else:
            print("Incorrect enter")
        for j in range(len(history)):
            print(history[j][0],history[j][1:])
