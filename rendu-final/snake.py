import turtle
import time
import random
import sys

delay = 0.1

try:
    turtle.Screen()
except turtle.Terminator:
    print("Pas d'interface graphique disponible. Quitter le programme.")
    sys.exit()

# Score
score = 0
high_score = 0

# Initialiser le prénom du joueur
prenom_joueur = turtle.textinput("Bienvenue au Snake Game!", "Entrez votre prénom: ")

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Désactive les mises à jour de l'écran

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "up"  # Initialiser la direction du serpent

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Joueur: {}  Score: 0  Record: 0".format(prenom_joueur), align="center", font=("Courier", 24, "normal"))

# Fonctions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up" and head.direction != "down":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down" and head.direction != "up":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left" and head.direction != "right":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right" and head.direction != "left":
        x = head.xcor()
        head.setx(x + 20)

# Touches du clavier
wn.listen()
wn.onkey(go_up, "o")
wn.onkey(go_down, "l")
wn.onkey(go_left, "k")
wn.onkey(go_right, "m")

# Boucle principale du jeu
while True:
    wn.update()

    # Vérifier la collision avec les bords
    if head.xcor() > 290:
        head.goto(-290, head.ycor())

    if head.xcor() < -290:
        head.goto(290, head.ycor())

    if head.ycor() > 290:
        head.goto(head.xcor(), -290)

    if head.ycor() < -290:
        head.goto(head.xcor(), 290)

    # Vérifier la collision avec la nourriture
    if head.distance(food) < 20:
        # Déplacer la nourriture à un endroit aléatoire
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Ajouter un segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        # Réduire le délai
        delay -= 0.001

        # Augmenter le score
        score += 10

        if score > high_score:
            high_score = score

        # Mettre à jour l'affichage du score
        pen.clear()
        pen.write("Joueur: {}  Score: {}  Record: {}".format(prenom_joueur, score, high_score), align="center", font=("Courier", 24, "normal"))

    # Déplacer les segments à la fin en ordre inverse
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Déplacer le segment 0 où se trouve la tête
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Vérifier la collision de la tête avec les segments du corps
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Cacher les segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Effacer la liste des segments
            segments.clear()

            # Réinitialiser le score
            score = 0

            # Réinitialiser le délai
            delay = 0.1

            # Mettre à jour l'affichage du score
            pen.clear()
            pen.write("Joueur: {}  Score: {}  Record: {}".format(prenom_joueur, score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

turtle.mainloop()
