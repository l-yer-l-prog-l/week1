N = int(input())
time1 = N // 60
time2 = N % 60
if N < 1440:
    print(time1, time2)
else:
    while N < 1440:
        N -= 1440
    time3 = N // 60
    time4 = N % 60
    print(time3, time4)
