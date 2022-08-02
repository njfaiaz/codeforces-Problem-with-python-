for i in range(5):
    arr = [int(x) for x in input().split()]
    for z in range(5):
        if arr[z] == 1:
            print(abs(2-i) + abs(2-z))
            exit
