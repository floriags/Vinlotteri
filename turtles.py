from random import randint, shuffle
import time
from turtle import *
import pygame as pg
import numpy as np

songs = [("williamTell.wav", 12.5), ("valkyries.wav", 10.5), ("pokemon.wav", 14)]
shuffle(songs)

pg.mixer.init()
gun = pg.mixer.Sound("sound/gun.wav")
cheer = pg.mixer.Sound("sound/cheer.wav")
song = [pg.mixer.Sound("sound/"+s[0]) for s in songs]

finale = pg.mixer.Sound("sound/fortuna.wav")
finaleWait = 22.5

players = ["jimi", "morbius", "tinder"]

while "" in players: players.remove("")

shuffle(players)

for player in players:
    register_shape("players/"+player+".gif")

title("Sylow Grand Prix")
setup(width=1848, height=1016, startx=0, starty=0)

goal = 715
start_x, start_y = -880, 375

heats = [[]]
n = len(players)
print("Antall spillere:", n)
max_players = 10

while n > max_players:
    n -= max_players
    heats.append([])

i = 0
for player in players:
    if i > len(heats)-1:
        i = 0
    heats[i].append(player)
    i += 1

heats.append([None for i in range(len(heats))])

for h, heat in enumerate(heats):
    track_name = "tracks/"+str(len(heat))+".gif"
    register_shape(track_name)
    track = Turtle()
    track.shape(track_name)
    
    turtles = []
    lanes = np.zeros(len(heat))

    for p, player in enumerate(heat):
        t = Turtle()
        t.shape("players/"+player+".gif")
        t.speed(0)
        t.penup()
        start_lane = start_y-p*83.5
        lanes[p] = start_lane
        t.goto(start_x, start_lane)
        turtles.append(t)
    
    if h != len(heats)-1:
        song[h].play()
        time.sleep(songs[h][1])
        gun.play()
        while heats[-1][h] == None:
            for turtle in turtles:
                if turtle.xcor() >= goal:
                    for t in turtles:
                        t.hideturtle()
                    turtle.showturtle()
                    turtle.home()
                    winner = turtle.shape()[8:-4]
                    heats[-1][h] = winner
                    time.sleep(5)
                    song[h].stop()
                    break
                else:
                    #turtle.forward(randint(0,10))
                    if turtle.speed() == 10:
                        turtle.forward(randint(0,1))
                        if randint(0, 100) < 15:
                            turtle.speed(0)
                    else:
                        step = randint(0, 3)
                        turtle.forward(step*step)
                        if randint(0, 100) < 5:
                            turtle.speed(5)
                        if turtle.speed() > 0:
                            turtle.forward(5)
                            speed = turtle.speed()
                            speed += 1
                            turtle.speed(speed)

    else:
        finale.play()
        time.sleep(finaleWait)
        gun.play()
        while True:
            for turtle in turtles:
                if turtle.xcor() >= goal:
                    for t in turtles:
                        t.hideturtle()
                    turtle.showturtle()
                    turtle.home()
                    cheer.play()
                    time.sleep(5)
                    exit()
                else:
                    turtle.forward(randint(0, 10))