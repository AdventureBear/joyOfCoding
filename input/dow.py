# What does this program output when it's ...
# 1. Monday?
# 2. Saturday?
# 3. Sunday?
# 4. Raining?

DoW = input("Enter a day: ")

if DoW.lower() == "saturday":
    print("Wake up at 9 am")
elif DoW.lower() == "sunday":
    print("Wake up at 10 am")
else:
    print("Wake up at 7 am")