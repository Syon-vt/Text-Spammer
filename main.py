# importing libraries
from pyautogui import write, press
from time import sleep

# setting variables
FAILSAFE = True
i = 0
msgs = 0
st = 5

text = input("Enter Text:")

print("########## Move cursor to top left corner to stop ##########")

# 5 second cooldown
while st > 0:
    print("Starting in %d seconds    " % (st), end='\r')
    sleep(1)
    st = st-1

# void loop()
while True:

    # sending messages
    while i < 100:
        write(text)
        sleep(0.25)
        press('enter')
        sleep(0.25)
        i = i+1
        msgs = msgs+1
        print("Messages sent = %d    " % (msgs), end='\r')
    i = 0
    sleep(30)
