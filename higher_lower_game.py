from random import choice, randint
from game_data import data
from art import logo, vs
import os

#celeb = celebrity
size_of_data = len(data)-1
celeb_A = data[randint(0,size_of_data)]
celeb_B = data[randint(0,size_of_data)]
score = 0


def get_new_celeb():
    return data[randint(0,size_of_data)]

#swapping celebs and changing 2nd celeb
def change_celebs(celeb_A, celeb_B):
    for info in celeb_A:
        celeb_A[info] = celeb_B[info]   
    
    temp_celeb = get_new_celeb()
    while temp_celeb["name"] == celeb_A["name"]:
        temp_celeb = get_new_celeb
    
    for key in celeb_B:
        celeb_B[key] = temp_celeb[key]
    
#print formatted celeb description
def celeb_desc(celeb):
    print(f"{celeb["name"]}, a {celeb["description"]}, from {celeb["country"]}.")


def play_game(celeb_A, celeb_B, score):
    os.system("clear")
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
        
    print("Compare A: ", end="")
    celeb_desc(celeb_A)
    
    print(f"\n{vs}")
    
    print("Against B: ", end="")
    celeb_desc(celeb_B)
    
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    while user_answer != "a" and user_answer != "b":
        user_answer = input("Invalid character, please type 'A' or 'B':")
    
    correct_score = "a" if celeb_A['follower_count'] > celeb_B["follower_count"] else "b"
    
    if user_answer == correct_score:
        score+=1
        change_celebs(celeb_A, celeb_B)
        play_game(celeb_A, celeb_B, score)
    else:
        os.system("clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        
        

    
play_game(celeb_A, celeb_B, score)