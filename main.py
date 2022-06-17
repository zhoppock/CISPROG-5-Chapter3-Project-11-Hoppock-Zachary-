#import random
import random
#input a beginnign pot amount
print("Lucky Sevens!")
pot = input("Enter how much money you will put into the pot: $")
count = 0
totalPot = int(pot)
maximum = pot

while totalPot > 0:
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  print("\n>> You rolled a", str(roll1), "and a", roll2)
  count += 1
  rollSum = roll1 + roll2
  print("Together, they add up to", rollSum)
  if rollSum == 7:
    totalPot += 4
    print(">> Congratulations!  You won $4")
  else:
    totalPot -= 1
    print(">> Ouch.  You just lost $1")
  print("The total pot is now $" + str(totalPot))
  if totalPot > int(pot) and totalPot > int(maximum):
    maximum = totalPot

print("\nWith a starting pot of $" + pot + ", you rolled", count, "time(s) until you lost it all!  The maximum amount of money in the pot was $" + str(maximum))