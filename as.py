import random
import time

w=0
f=0
t=0
l = 0
while l<5:
    l = l + 1
    lst = ["stone","paper","scissor"]
    a = random.choice(lst)
    s = input("Enter Your Choice : Stone, Paper, Scissor -> ")

    if s == a :
        print(f"Computer's Choice -> {a}")
        print("No One is Winner, Tie\n")
        t = t+1
        
    elif (s == "stone" and a == "scissor") or (s == "paper" and a == "stone") or (s == "scissor" and a == "paper"):
        print(f"Computer's Choice -> {a}")
        print("Woohoo!, You are Winner\n")
        w = w+1

    elif (s == "stone" and a == "paper") or (s == "paper" and a == "scissor") or (s == "scissor" and a == "stone"):
        print(f"Computer's Choice -> {a}")
        print("You Loose, Try Again\n")
        f = f+1

    time.sleep(1)

print(f"You WIN {w} times and LOOSE {f} times and TIE UP {t} times\n")