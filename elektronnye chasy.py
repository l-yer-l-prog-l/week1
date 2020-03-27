N = int(input())
time1 = N // 60
time2 = N % 60
if N < 1440:
    print(time1, time2)
else:
    i = N // 1440
    count = i * 1440
    time = N - count
    time3 = time // 60
    time4 = time % 60
    print(time3, time4)
