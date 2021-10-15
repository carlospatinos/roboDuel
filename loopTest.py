import time

x = 0
while True:
    print(x)
    x += 1
    time.sleep(1)
    if x > 10:
        continue
    print("next iteration")
