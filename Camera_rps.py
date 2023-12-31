import cv2
from keras.models import load_model
import numpy as np 

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1,224,224,3), dtype=np.float32)

import random
import time

def get_computer_choice():
    """
    This functions generates the computer's choice in the rock-paper-scissors game.

    The purpose of this function is to return a random option 
    from the list of options provided in the options_list
    """
    options_list = ["scissors", "rock", "paper"] 
    # List of all the options the computer can choose
    return random.choice(options_list)
    # Returns a random option from the list of options

def get_prediction():
    """
    This function uses a deep learning model to predict the result of the hand gestures related to the rock-paper-scissors game.

    The function uses opencv-python for computer vision and outputs the result of the model to the variable called predicitons. 
    Each element in the output corresponds to the probability of the input image representing a particular class and I used the 
    argmax() method to get the highest value in the row to get the most likely class. 
    """
    time_passed = time.time() + 3
    options_list = ["rock", "scissors", "paper", "nothing"]
    while time.time() < time_passed: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        index = np.argmax(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return options_list[int(index)]

def get_user_choice():
    """
    This functions stores the user's choice in the rock-paper-scissors game.

    The purpose of this function is to return the user's option 
    from their hand gesture
    """
    user_choice = get_prediction()
    print(f"You choose {user_choice}")
    return user_choice


computer_wins = 0
user_wins = 0
rounds = 0
# Initalises the wins and rounds of the rock-paper-scissors game

def get_winner(computer_choice, user_choice):
    """
    This function determines the winner of the rock-paper-scissors round.

    The purpose of this function is to return the winner of the game based on the if-elif-statements.
    This is used to determine whether the comptuer won, user won or tied. The variables are made global so they be accessed 
    outside of the function as well (not limited to the scope of the function).
    """
    global computer_wins, user_wins, rounds
    if computer_choice == user_choice:
        print("It is a tie!")
        rounds +=1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won this round !")
        user_wins += 1
        rounds +=1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won this round!")
        user_wins += 1
        rounds +=1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won this round!")
        user_wins += 1
        rounds +=1
    else:
        print("You lost this round")
        computer_wins += 1
        rounds +=1
    # The above prints a message according to the condition that it meets

def play():
    """
    This function runs the game logic

    The while loop runs for the duration of the game and the if else statements determine whether the end of the
    game has been reached or not. Inside the first if statement, the winner is determined or if there is a tie.
    """
    while True:
        if computer_wins == 3 or user_wins == 3 or rounds == 5:
            if computer_wins == user_wins:
                print("You tied the best of three")
            elif computer_wins > user_wins:
                print("You lost the game")
            else:
                print("You won the game")
            break
        # Checks who the winner of the game is or if there is a tie
        else:
            computer_choice = get_computer_choice()
            user_choice =  get_user_choice()
            get_winner(computer_choice, user_choice)
            print("Wins by computer: ", computer_wins)
            print("Wins by computer: ", user_wins)
        # Runs the game logic
play()


