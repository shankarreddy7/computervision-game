
# Computer-vision game

Google's Teachable Machine is a web-based tool that makes creating machine learning models fast, easy, and accessible. I've used this tool to create Rock,papers and scissors game with the help of camera inbed in the device. computer vision and Python programming language are used to achive it.


## Milestone 1:


Utilizing the [Teachable Machine's](https://teachablemachine.withgoogle.com/)  functionality we've created four categories namely Rocks,papers,scissors and nothing was trained. which classifies the images shown to it during the operation. this trained model is downloaded by tensorflow header files and loaded to the directory.


![teachable machine](https://user-images.githubusercontent.com/101912572/200111750-ec3baabe-1455-491f-b947-853ca9f8f26d.png)

## Milestone 2:

To avoid dependency conflicts with different versions of the libraries. the project is done under conda environment. As I am using Ubuntu flavoured linux, current version of tensorflow is not supported. so, we've installed python version 3.8 . we have installed, tensorflow: a package for Machine learning and CV2: a package for computer vision is installed.
'''
conda install -n myenv pip
conda activate myenv
'''


## Milestone 3: Manual Game

We have created a manual game to simulate our actual computer vision integration game. In this functionality we give the input of use's choice using the keyborad and computers choice by random() function. By comparing the choices the winner is being selected. we have created a function to simulate the actual game "play".


## Milestone 4: Camera integration

In python using OOPS concepts, we have a class with different methods are created which are vital for camera frames acquision, random choice of the computer, and a method to determine the winner of the game.

Later on, we have created the Play() function which holds the actual logic of the game is created. the time.time() function  is used to keep the counter on the game for the choices the user make.
## Working Demonstration



