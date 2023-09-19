import random

# Function to get the computer's choice
def get_computer_choice():
    options = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(options)
    return computer_choice

# Function to get the user's choice

def get_user_choice():
    while True:
        user_choice = input("Enter your choice(Rock/Paper/Scissors): ")
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose from Rock,Paper or Scissors")
            
# Main game logic 
def main():
    print("Welcome to Rock-Paper-Scissors!")
    
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        
        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif(
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
        ):
            print("You win!")
        else:
            print("Computer wins!")
            
            play_again = input("Play again? (yes/no): ").strip.lower()
            if play_again != "yes":
                break
    if __name__ == "__main__":
        main()