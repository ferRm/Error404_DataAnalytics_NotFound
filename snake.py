import random
import curses
import time
import inquirer
from prettytable import PrettyTable

scoreboard = PrettyTable()
scoreboard.title = "Los Chingones"
scoreboard.field_names = ['Names','Scores','dificultad']
scoreboard.add_row(['Aquiles Gano', 6, 'Gran Danes ALV'])
scoreboard.add_row(['Benito Carmelo', 5, 'Labrador'])
scoreboard.add_row(['Mike Hawk', 4, 'Chihuahua'])

name = input("¿Cual es tu nombre tigre?")

print ("Quiubole " + name, "! Hora de hacer ALGO QUE NO ES DATA ANALYTICS  ¯\_(ツ)_/¯ ")

questions = [
  inquirer.List('size',
                message="Que tan perro lo quieres?",
                choices=['Chihuahua','Labrador', 'Gran Danes ALV']
            ),
]
answers = inquirer.prompt(questions)
print("Game Over")
for x in answers.values():
    print("dificultad "+ x)

dif=0
if x == 'Chihuahua':
    dif= dif+100
elif x == 'Labrador':
    dif=dif+60
elif x == 'Gran Danes ALV':
    dif=dif+30

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(dif)


snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        score =len(snake)
        score= score-3
        score= str(score)
        print("Puntuacion:"+ score)
        score= int(score)
        scoreboard.add_row([name,score,x])
        scoreboard.sortby = 'Scores'
        scoreboard.reversesort = True
        print(scoreboard)
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(2, sh-1),
                random.randint(2, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]),' ')
    try:
        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    except:
      curses.endwin()
      score =len(snake)
      score= score-3
      score= str(score)
      print("Puntuacion:"+ score)
      score= int(score)
      scoreboard.add_row([name,score,x])
      scoreboard.sortby = 'Scores'
      scoreboard.reversesort = True
      print(scoreboard)
      quit()	
