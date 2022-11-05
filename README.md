
# Computer-vision game

Google's Teachable Machine is a web-based tool that makes creating machine learning models fast, easy, and accessible. I've used this tool to create Rock,papers and scissors game with the help of camera inbed in the device. computer vision and Python programming language are used to achive it.


## Milestone 1:


Utilizing the [Teachable Machine's](https://teachablemachine.withgoogle.com/)  functionality we've created four categories namely Rocks,papers,scissors and nothing was trained. which classifies the images shown to it during the operation. this trained model is downloaded by tensorflow header files and loaded to the directory.


![teachable machine](https://user-images.githubusercontent.com/101912572/200111750-ec3baabe-1455-491f-b947-853ca9f8f26d.png)

## Milestone 2:

To avoid dependency conflicts with different versions of the libraries. the project is done under conda environment. As I am using Ubuntu flavoured linux, current version of tensorflow is not supported. so, we've installed python version 3.8 . we have installed, tensorflow: a package for Machine learning and CV2: a package for computer vision is installed.

~~~
conda install -n myenv pip
conda activate myenv
conda install -c anaconda python=3.8
pip install cv2
pip install tensorflow
~~~


## Milestone 3: Manual Game

We have created a manual game to simulate our actual computer vision integration game. In this functionality we give the input of use's choice using the keyborad and computers choice by random() function. By comparing the choices the winner is being selected. we have created a function to simulate the actual game "play".
~~~
pick an item: Rock[0], Paper[1] , Scissors[2]1
Scissors shreds Paper, you Lose!
pick an item: Rock[0], Paper[1] , Scissors[2]2
It's a tie!
pick an item: Rock[0], Paper[1] , Scissors[2]2
Scissors shreds Paper, you Win!
pick an item: Rock[0], Paper[1] , Scissors[2]3
Invalid entry, enter a value from: range(0, 2)
~~~

## Milestone 4: Camera integration

In python using OOPS concepts, we have a class with different methods are created which are vital for camera frames acquision, random choice of the computer, and a method to determine the winner of the game.

Later on, we have created the Play() function which holds the actual logic of the game is created. the time.time() function  is used to keep the counter on the game for the choices the user make.
~~~
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
~~~



