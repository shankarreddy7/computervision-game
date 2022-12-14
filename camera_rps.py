from enum import IntEnum
import random
import cv2
from keras.models import load_model
import numpy as np
import time


class items(IntEnum):
        Rock =  0
        Paper = 1
        Scissors = 2
        Nothing = 3
class VisualRps():    

    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.computer_score = 0
        self.user_score = 0
        self.rounds = 0
        
        

    # audio intro into the game with instruction to click
    def introduction(self):
        self.name = input("pls your name: ")
        print(f" Welcome {self.name} to the ROCK PAPER SCISSORS GAME, have fun!")
 
    # left click to begin and move along in the game
    def left_click(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            time.time()

    # to get user choice
    def get_prediction(self):
        prediction = self.model.predict(self.data)
        choice = np.argmax(prediction[0])
        print(choice)
        self.user_choice = items(choice)
        print(self.user_choice)
        return self.user_choice
        
    # get computer choice and choice name
    def get_comp_choice(self):
        
        self.pick = random.randint(0, len(items) - 1)
        self.comp_choice = items(self.pick)
        print(self.comp_choice)
        return self.comp_choice
    
    # get winner
    def get_winnner(self, comp_choice, user_choice):
  
        if comp_choice == user_choice:
            self.rounds += 1
            self.winner = "it's a tie!"
        
        elif user_choice == items.Rock and comp_choice == items.Scissors:
            self.user_score += 1
            self.winner = self.name
            self.rounds += 1
            
        elif user_choice == items.Rock and comp_choice == items.Paper:
            self.computer_score += 1
            self.winner = "comp"
            self.rounds += 1

        elif user_choice == items.Paper and comp_choice == items.Rock:
            self.user_score += 1
            self.winner = self.name
            self.rounds += 1
            
        elif user_choice == items.Paper and comp_choice == items.Scissors:
            self.computer_score += 1
            self.winner = "comp"
            self.rounds += 1
        elif user_choice == items.Scissors and comp_choice == items.Paper:
            self.user_score += 1
            self.winner = self.name
            self.rounds += 1
        elif user_choice == items.Scissors and comp_choice == items.Rock:
            self.computer_score += 1
            self.winner = "comp"
            self.rounds += 1
        else:
            
            self.winner = "NO WINNER!!"
            print(self.winner)
            print("play again")
            return(self.winner)
        
        

    def open(self):
        
        #displays instruction for starting and getting through the game
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, self.frame = self.cap.read()
        if self.frame is None:
            print('No image')
        else: 
            self.frame = self.frame[32:, 188:]
        resized_frame = cv2.resize(self.frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image

         # records and instruction box
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(self.frame, (10,10), (600, 120), (255,255,0), -1)
        message = "Stage: " + str(self.rounds) + " "  + "Scores " + str(self.name) + ":" + str(self.user_score) + " CPU:" + str(self.computer_score)
        cv2.putText(self.frame, message, (20,60), 1, 2, (0,0,0))
        cv2.putText(self.frame, 'Hold b to start or q to quit', (20,100), 1, 2, (255,0,0))
        cv2.imshow('self.frame', self.frame)

    
    def end_game(self):
        # for ending the game
        self.cap.release()
        if self.computer_score == 2 or self.user_score == 2:
            print(f'Game over we have a winner')
        else:
            print(f'You left game before the outcome was determined')
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)



def play():
    #instantiating the class
    game = VisualRps()
    game.introduction()
    
    while True:
        timer = 5
        #opens camera
        game.open()
         # press b to start game
        if cv2.waitKey(80) & 0xFF == ord('b'):
            prev_time = time.time()
            while timer > 0:
                game.open()
                cv2.putText(game.frame, str(timer), (190,420), 2, 3, (0,0,0))
                cv2.imshow('game.frame', game.frame)
                cv2.waitKey(1)
  
                #countdown
                curr_time = time.time()
                if curr_time - prev_time >= 1:
                    prev_time = curr_time
                    timer = timer - 1
            # after coundown show choices and winner
            else:
                game.open()
                game.get_prediction()
                user_choice = game.get_prediction()
                comp_choice = game.get_comp_choice()
                game.get_winnner(comp_choice, user_choice)

                # output winner 
                font = cv2.FONT_HERSHEY_SIMPLEX 
                cv2.putText(game.frame, f" {game.name}'s  Move: {game.user_choice.name}",
                            (50, 250), font, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(game.frame, f" CPU's Move: {game.comp_choice.name}",
                            (600, 250), font, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
                
                cv2.putText(game.frame, f" Winner: {game.winner}",
                            (300, 600), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                cv2.imshow('game.frame', game.frame)
                cv2.waitKey(1)


                # pick over all winner
                if game.computer_score == 2:
                    # always call the open() in order to read and show the displays
                    game.open()
                    cv2.rectangle(game.frame, (50,80), (402, 160), (180,170,50), -1)
                    cv2.putText(game.frame, "GAME OVER", (135,110), 3, 1, (0,0,0))
                    cv2.putText(game.frame, "Once again, a machine defeats a human!", (110,150), 3, 1, (0,0,0))
                    cv2.imshow('game.frame', game.frame)
                    cv2.waitKey(6000)
                    game.end_game()
                    break

                elif game.user_score == 2:
                  
                    game.open()
                    cv2.rectangle(game.frame, (50,80), (402, 160), (180,170,50), -1)
                    cv2.putText(game.frame, "GAME OVER", (135,110), 3, 1, (0,0,0))
                    cv2.putText(game.frame, game.name + " wins!", (110,150), 3, 1, (0,0,0))
                    cv2.imshow('game.frame', game.frame)
                    cv2.waitKey(6000)
                    game.end_game()
                    break
                
            
        #if user press q camera and game stops
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
play()