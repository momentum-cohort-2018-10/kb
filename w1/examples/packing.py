print("You are packing for a big trip.")
print("You can take up to 50 lbs of luggage before you have to pay extra.")

limit = 50
current = 0

while current <= limit:
    luggage_wgt = int(
        input("What's the weight of your next piece of luggage? "))
    current += luggage_wgt
    print("You have", current, "pounds of luggage")

print("That's too much luggage!")
