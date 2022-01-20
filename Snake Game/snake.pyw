from tkinter import *
import keyboard
import time
import random

def start():
  score = 0
  loose = 0
  facing = 4
  key = "w"
  timer = 0
  apple = 0
  appleX = 0
  appleY = 0
  snekX = random.randint(1, 23) * 10
  snekY = random.randint(1, 23) * 10
  i = 0
  e = 0
  f = 1
  moveArr = []
  snekBlock = []
  moveHist = [0]

  # The Snake will exist between x/y 10 - 220
  field = Canvas(main, width = 250, height = 250)
  snek = field.create_rectangle(snekX, snekY, snekX + 10, snekY + 10, outline="black", fill="green")
  b1 = field.create_rectangle(0, 0, 250, 10, fill="grey", outline="grey")
  b2 = field.create_rectangle(0, 0, 10, 250, fill="grey", outline="grey")
  b3 = field.create_rectangle(0, 240, 250, 250, fill="grey", outline="grey")
  b4 = field.create_rectangle(240, 0, 250, 250, fill="grey", outline="grey")

  text.pack_forget()
  startButton.pack_forget()
  field.pack()
  field.update()

  appleX = random.randint(1, 23) * 10
  appleY = random.randint(1, 23) * 10
  appl = field.create_rectangle(appleX, appleY, appleX + 10, appleY + 10, outline="black", fill="red")

  while loose != 1:
    field.update()
    # Keyboard Events Handler
    if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
      moveHist[0] = facing
      if facing != 2:
        facing = 0
    elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
      moveHist[0] = facing
      if facing != 3:
        facing = 1
    elif keyboard.is_pressed("s") or keyboard.is_pressed("down"):
      moveHist[0] = facing
      if facing != 0:
        facing = 2
    elif keyboard.is_pressed("a") or keyboard.is_pressed("left"):
      moveHist[0] = facing
      if facing != 1:
        facing = 3

    # Apple Generator
    if apple == 1:
      appleX = 0
      appleY = 0
      appleX = random.randint(1, 23) * 10
      appleY = random.randint(1, 23) * 10
      if score >= 1:
        while (appleX == field.coords(snek)[0] and appleY == field.coords(snek)[1]) or (appleX == field.coords(snekBlock[e])[0] and appleY == field.coords(snekBlock[e])[1]):
          if appleX == field.coords(snek)[0] or appleX == field.coords(snekBlock[e])[0]:
            appleX = random.randint(1, 23) * 10
          elif appleY == field.coods(snek)[0] or appleY == field.coords(snekBlock[e])[0]:
            appleY = random.randint(1, 23) * 10
          e = e + 1
      else:
        while appleX == field.coords(snek)[0] and appleY == field.coords(snek)[1]:
          if appleX == field.coords(snek)[0]:
            appleX = random.randint(1, 23) * 10
          elif appleY == field.coods(snek)[0]:
            appleY = random.randint(1, 23) * 10
      field.coords(appl, appleX, appleY, appleX + 10, appleY + 10)
      apple = 0
      e = 0
    
    if timer == 10:
      i = score 
      # Go Up
      if facing == 0:
        field.move(snek, 0, -10)
        while i != 0:
          if moveHist[i] == 0:
            field.move(snekBlock[i - 1], 0, -10)
          elif moveHist[i] == 1:
            field.move(snekBlock[i - 1], 10, 0)
          elif moveHist[i] == 2:
            field.move(snekBlock[i - 1], 0, 10)
          elif moveHist[i] == 3:
            field.move(snekBlock[i - 1], -10, 0)
          moveHist[i] = moveHist[i - 1]
          i = i - 1
      # Right
      elif facing == 1:
        field.move(snek, 10, 0)
        while i != 0:
          if moveHist[i] == 0:
            field.move(snekBlock[i - 1], 0, -10)
          elif moveHist[i] == 1:
            field.move(snekBlock[i - 1], 10, 0)
          elif moveHist[i] == 2:
            field.move(snekBlock[i - 1], 0, 10)
          elif moveHist[i] == 3:
            field.move(snekBlock[i - 1], -10, 0)
          moveHist[i] = moveHist[i - 1]
          i = i - 1
      # Down
      elif facing == 2:
        field.move(snek, 0, 10)
        while i != 0:
          if moveHist[i] == 0:
            field.move(snekBlock[i - 1], 0, -10)
          elif moveHist[i] == 1:
            field.move(snekBlock[i - 1], 10, 0)
          elif moveHist[i] == 2:
            field.move(snekBlock[i - 1], 0, 10)
          elif moveHist[i] == 3:
            field.move(snekBlock[i - 1], -10, 0)
          moveHist[i] = moveHist[i - 1]
          i = i - 1
      # Left
      elif facing == 3:
        field.move(snek, -10, 0)
        while i != 0:
          if moveHist[i] == 0:
            field.move(snekBlock[i - 1], 0, -10)
          elif moveHist[i] == 1:
            field.move(snekBlock[i - 1], 10, 0)
          elif moveHist[i] == 2:
            field.move(snekBlock[i - 1], 0, 10)
          elif moveHist[i] == 3:
            field.move(snekBlock[i - 1], -10, 0)
          moveHist[i] = moveHist[i - 1]
          i = i - 1
      if field.coords(snek)[0] == 0:
        loose = 1
      elif field.coords(snek)[1] == 0:
        loose = 1
      elif field.coords(snek)[2] == 250:
        loose = 1
      elif field.coords(snek)[3] == 250:
        loose = 1
      if score >= 2:
        while f < score:
          if field.coords(snek)[0] == field.coords(snekBlock[f])[0] and field.coords(snek)[1] == field.coords(snekBlock[f])[1]:
            loose = 1
            break
          f = f + 1
      f = 1

      time.sleep(.1)
      if appleX == field.coords(snek)[0] and appleY == field.coords(snek)[1]:
        snekBlock.append(score)
        # appending information on the location of other snake blocks relative to the head
        if score == 0:
          if facing == 0:
            moveArr.append([score, 0])
            moveHist.append(0)
            snekBlock[score] = field.create_rectangle(field.coords(snek)[0], field.coords(snek)[1] + 10,
                                 field.coords(snek)[2], field.coords(snek)[3] + 10, outline="black", fill="lightgreen", tags = "a")
          elif facing == 1:
            moveArr.append([0, score])
            moveHist.append(1)
            snekBlock[score] = field.create_rectangle(field.coords(snek)[0] - 10, field.coords(snek)[1],
                                 field.coords(snek)[2] - 10, field.coords(snek)[3], outline="black", fill="lightgreen", tags = "a")
          elif facing == 2:
            moveArr.append([-1 * (score), 0])
            moveHist.append(2)
            snekBlock[score] = field.create_rectangle(field.coords(snek)[0], field.coords(snek)[1] - 10,
                                 field.coords(snek)[2], field.coords(snek)[3] - 10, outline="black", fill="lightgreen", tags = "a")
          elif facing == 3:
            moveArr.append([0, -1 * (score)])
            moveHist.append(3)
            snekBlock[score] = field.create_rectangle(field.coords(snek)[0] + 10, field.coords(snek)[1],
                                 field.coords(snek)[2] + 10, field.coords(snek)[3], outline="black", fill="lightgreen", tags = "a")
        else:
          if moveHist[score - 1] == 0:
            moveArr.append([score, 0])
            moveHist.append(0)
            snekBlock[score] = field.create_rectangle(field.coords(snekBlock[score - 1])[0], field.coords(snekBlock[score - 1])[1] + 10,
                                   field.coords(snekBlock[score - 1])[2], field.coords(snekBlock[score - 1])[3] + 10, outline="black", fill="lightgreen", tags = "a")
          elif moveHist[score - 1] == 1:
            moveArr.append([0, score])
            moveHist.append(1)
            snekBlock[score] = field.create_rectangle(field.coords(snekBlock[score - 1])[0] - 10, field.coords(snekBlock[score - 1])[1],
                                 field.coords(snekBlock[score - 1])[2] - 10, field.coords(snekBlock[score - 1])[3], outline="black", fill="lightgreen", tags = "a")
          elif moveHist[score - 1] == 2:
            moveArr.append([-1 * (score), 0])
            moveHist.append(2)
            snekBlock[score] = field.create_rectangle(field.coords(snekBlock[score - 1])[0], field.coords(snekBlock[score - 1])[1] - 10,
                                                     field.coords(snekBlock[score - 1])[2], field.coords(snekBlock[score - 1])[3] - 10, outline="black", fill="lightgreen", tags = "a")
          elif moveHist[score - 1] == 3:
            moveArr.append([0, -1 * (score)])
            moveHist.append(3)
            snekBlock[score] = field.create_rectangle(field.coords(snekBlock[score - 1])[0] + 10, field.coords(snekBlock[score - 1])[1],
                                 field.coords(snekBlock[score - 1])[2] + 10, field.coords(snekBlock[score - 1])[3], outline="black", fill="lightgreen", tags = "a")
        score = score + 1
        i = score
        apple = 1
      timer = 0
    i = score
    timer = timer + 1
  field.pack_forget()

  def restart():
    fail.pack_forget()
    scor.pack_forget()
    again.pack_forget()
    start()
  
  fail = Message(main, text = "You Loose! Your Score:", relief = RAISED)
  scor = Message(main, text = score, relief = RAISED)
  again = Button(main, bg= "lightgreen", text = "Again?", command = restart)
  
  fail.pack()
  scor.pack()
  again.pack()
  main.mainloop()

main = Tk()
main.title("Snake Game")
startButton = Button(main, bg = "lightgreen", text = "START", command = start)
var = StringVar()
text = Message(main, textvariable = var, relief = RAISED)
var.set("Snake Game!")

text.pack()
startButton.pack()
main.mainloop()  
