import time

seconds = bool(
    input("do you want to convert minuites into seconds(1 for yes , 0 for no):"))
if seconds == 1:
    min = int(input("enter time in minuites:"))
    sec = min*60
else:
    print("you are good to go :)")
print(f"{min} minuites is {sec} seconds")

print("<-------------------------------->")
def count_down(n):
    while n:
        mins, sec = divmod(n, 60)
        timer = '{:02d}:{:02d}'.format(mins, sec)
        print(timer, end="\r")
        time.sleep(1)
        n -= 1

    print('Timer completed!')


n = int(input("Enter the time in seconds:"))

count_down(n)

timer = int(input("Enter time in sec:"))
for i in range(timer, 0, -1):
    print(i)
    time.sleep(1)
print("time out !")
