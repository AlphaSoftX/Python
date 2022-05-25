import random;
import time;

print("Guess the number game.\n");
print("Rules: You have to guess a number from 1 to 100, I will give you hints according to your input and you can quit game anytime by typing endgame in your guess.\n");
print("Starting game...");
num = None;
trys = None;

def start():
    global num, trys;
    num = random.randint(1,100);
    trys = 0;
    time.sleep(1);
    print("I have guessed a number, let's start.");
    guess();

def guess():
    a = input("Enter your guessed number: ");
    try:
        a = int(a);
        check(a);
    except:
        if a.lower()=='endgame' :
            replay();
        else:
            print("Some error occurred, please retry.");
            guess();

def check(a):
    global num, trys;
    trys = trys + 1;
    if a==num :
        print("Your guess is right");
        print("The number is", num);
        print("You have guessed this number in", trys, end=" ");
        if trys==1 :
            print("try.");
        else:
            print("trys.");
        replay();
    elif a>num :
        print("This number is greater than the number I have guessed.");
        guess();
    elif a<num :
        print("This number is smaller than the number I have guessed.");
        guess();

def replay():
    a = input("Do you want to replay? (Y/n): ");
    if a.lower()=='y' or a=='' :
        print("Restarting game...");
        start();
    elif a.lower()=='n' :
        print("OK, Thanks for playing, Bye Bye");
    else:
        print("Sorry, I don't understand.");
        replay();

start();