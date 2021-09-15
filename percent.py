import time

k = 0
while True:
    k += 1
    print(k)
    if 4000 % k == 0:
        print("******")
    if 2000 % k == 0:
        print("Running")
    time.sleep(0.2)
