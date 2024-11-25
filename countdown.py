import time

m=int(input("Enter the amount of seconds you want to countdown: "))

def countdown(n):
    if n==0:
        print("Time's up!")
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)

countdown(m)