
import time

class Main:

    my_time = int(input("Enter the time in seconds: "))


    for x in reversed(range(0, my_time)):

        secondi = x % 60
        minuti = int(x / 60) % 60
        print(f"00:{minuti:02}:{secondi:02}")
        time.sleep(1)

    print("Tempo finito!!!")

