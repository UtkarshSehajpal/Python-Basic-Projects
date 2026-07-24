import time

my_time = int(input("Enter your time in seconds: "))

# for i in reversed(range(0, my_time)):
#     print(i + 1)
#     time.sleep(1)
# print("Time is Up!")
# print()

#Another method-
# for i in range(my_time, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Time is Up!")
# print()

#Digital Clock Countdown-

for i in range(my_time, 0, -1):
    seconds = i % 60
    mins = (i // 60) % 60
    hours = (i // 3600) % 60
    print(f"{hours:02}:{mins:02}:{seconds:02}")
    time.sleep(1)
print("END!")