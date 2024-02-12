print("Welcome to the Wi-Fi troubleshooter!")
print("This program will help you troubleshoot your Wi-Fi connection. We will need you to try a couple of things during this process.")
print("First, let's reboot your computer.")
reboot = input("Did that fix the problem? (yes or no): ")
if reboot == "yes":
    print("Great! You're all set!")
else:
    print("Next, let's reboot your router.")
    router = input("Did that fix the problem? (yes or no): ")
    if router == "yes":
        print("Great! You're all set!")
    else:
        print("Next, let's check the cables.")
        cables = input("Did that fix the problem? (yes or no): ")
        if cables == "yes":
            print("Great! You're all set!")
        else:
            print("Next, let's move the router.")
            move = input("Did that fix the problem? (yes or no): ")
            if move == "yes":
                print("Great! You're all set!")
            else:
                print("It's time to replace the router.")
                new_router = input("Did that fix the problem? (yes or no): ")
                if new_router == "yes":
                    print("Great! You're all set!")
                else:
                    print("Something is really broken you should seek further assistance.")    
print("Goodbye!")
