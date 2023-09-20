import time
import cv2
from keras.models import load_model
import numpy as np 

# Load the model (if it's not in the same folder, provide the full path)
model = load_model('keras_model.h5')

# Function to get the computer's choice using the model prediction
def get_prediction():
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1,224,224,3), dtype=np.float32)
    
    countdown_start = time.time() # Record the start time
    countdown_duration = 8 # Set the countdown duration in seconds
    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224,224),interpolation = cv2.INTER_AREA)
        image_np =np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32)/ 127.0) - 1 #Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame',frame)
        predicted_class = np.argmax(prediction)
        # Calculate the time elapsed since the countdown started
        elapsed_time = time.time() - countdown_start
        
        #Return the class with the highest probability (index of max element)
        if elapsed_time >= countdown_duration:
            
            break # Move the break statement inside this block
        #Print the remaining time of the countdown
        remaining_time = int(countdown_duration - elapsed_time)
        print(f"Countdown: {remaining_time} seconds", end='\r')
        
        cap.release()
        cv2.destroyAllWindows()
        return predicted_class
        #Function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Enter your choice(Rock/Paper/Scissors): ")
        if user_choice in ["Rock","Paper","Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose from Rock, Paper, or Scissors")
            
#Function to determine the winner based on the game logic 
def get_winner(computer_choice, user_choice):
    # Implement your game logic here
    # This function should return a string indicating the result of the game
    # For example, "Computer wins!", "You win!", "It's a tie!"
    pass

def play():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        computer_choice = get_prediction()
        user_choice = get_user_choice()
        
        print(f"Computer chose: {computer_choice}")
        print(f"You chose:{user_choice}")
        
        result = get_winner(computer_choice, user_choice)
        print(result)
        
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
                
if __name__ == "__main__":
    play()
                
