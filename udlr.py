import streamlit as st 
import os
import random
import time
# # Set the app title 
# st.title('My First Streamlit App') 
# # Add a welcome message 
# st.write('Welcome to my Streamlit app!') 
# # Create a text input 
# widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# # Display the customized message 
# st.write('Customized Message:', widgetuser_input)

l_combinations = ["UULL", "UULR", "UURL", "UURR", 
                  "UDLL", "UDLR", "UDRL", "UDRR", 
                  "DULL", "DULR", "DURL", "DURR", 
                  "DDLL", "DDLR", "DDRL", "DDRR", ]

l_hand = ["L", "R"]

mapper_directions = {"U":"Up", "D":"Down", "L":"Left", "R":"Right"}

n_round = int(st.text_input("Number of Round", "4"))
speed = int(st.text_input("Speed", "1"))
max_number = int(st.text_input("Max Number", "10"))

if st.button("Start"):
    l_num = []
    time.sleep(1)
    for i in range(0, n_round):
        path = random.choice(l_combinations)
        hand = random.choice(l_hand)
        num = random.randint(0, max_number)
        l_num.append(num)
        for d in path:
            os.system("say '{}'".format(mapper_directions[d]))
            time.sleep(0.5 / speed)
        os.system("say '{}'".format(mapper_directions[hand]))
        time.sleep(0.5 / speed)
        os.system("say '{}'".format(num))
        time.sleep(0.5 / speed)
        st.text("{}  {}  {}".format(path, hand, num))
    os.system("say '{}'".format("Sum number"))
    st.text("Sum = {}".format(sum(l_num)))