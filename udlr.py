import streamlit as st 
import os
import random
import time
from plyer import tts


l_combinations = ["UULL", "UULR", "UURL", "UURR", 
                  "UDLL", "UDLR", "UDRL", "UDRR", 
                  "DULL", "DULR", "DURL", "DURR", 
                  "DDLL", "DDLR", "DDRL", "DDRR", ]

l_hand = ["L", "R"]

mapper_directions = {"U":"Up", "D":"Down", "L":"Left", "R":"Right"}

n_round = int(st.text_input("Number of Round", "4"))
speed = int(st.text_input("Speed", "3"))
max_number = int(st.text_input("Max Number", "10"))

if st.button("Start"):
    l_num = []
    time.sleep(1.5)
    for i in range(0, n_round):
        path = random.choice(l_combinations)
        hand = random.choice(l_hand)
        num = random.randint(1, max_number)
        l_num.append(num)
        for d in path:
            # os.system("say '{}'".format(mapper_directions[d]))
            msg = "{}".format(mapper_directions[d])
            tts.speak(message=msg)

            time.sleep(0.5 / speed)
        # os.system("say '{}'".format(mapper_directions[hand]))
        msg = "{}".format(mapper_directions[hand])
        tts.speak(message=msg)
        time.sleep(0.5 / speed)
        # os.system("say '{}'".format(num))
        msg = "{}".format(num)
        tts.speak(message=msg)
        time.sleep(0.5 / speed)
        st.text("{}  {}  {}".format(path, hand, num))
    # os.system("say '{}'".format("Sum number"))
    msg = "{}".format("Sum number")
    tts.speak(message=msg)
    st.text("Sum = {}".format(sum(l_num)))

