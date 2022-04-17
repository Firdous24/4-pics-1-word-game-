from tkinter import *
from stack import mystack
import string
import random

img = mystack()
img.push("C:\\Users\\Areeba\\Desktop\\Candy.png")
img.push("C:\\Users\\Areeba\\Desktop\\Round.png")

word = mystack()
word.push("CANDY")
word.push("ROUND")

class myGame:
    def __init__(self, master):
        self.master=master
        self.main_menu = Menu(self.master)
        self.master.config(menu=self.main_menu)
        self.ins = Menu(self.main_menu)
        self.main_menu.add_cascade(label="File", menu=self.ins)
        self.ins.add_command(label="Instructions", command=self.Help)
        self.label = Label(self.master, text="4 pics 1 word", bg="yellow")
        self.label.grid(row=0,columnspan=5)
        self.canvas = Canvas(width=400, height=250, bg="blue")
        self.canvas.grid(row=1,columnspan=5)
        x=img.pop()
        self.photo = PhotoImage(file=x)
        self.canvas.create_image(75, 0, image=self.photo, anchor=NW)
        self.first = word.pop()
        self.Ent = []
        b=0
        while b<len(self.first):
            for i in range(len(self.first)):
                self.entry = Entry(self.master)
                self.entry.grid(row=2,column=b)
                self.Ent.append(self.entry)
                b=b+1

        self.btn = Button(self.master, text="submit word", command=self.getEntry)
        self.btn.grid(row=3,columnspan=5)
        self.btn2 = Button(self.master, text="Next Level", command=self.levelchanger)
        self.btn2.grid(row=4,columnspan=5)
        y = 12 - len(self.first)
        chars = string.ascii_uppercase
        self.jumble=[]
        for j in range(y):
            self.let = random.choice(chars)
            self.jumble.append(self.let)
        for t in range(len(self.first)):
            self.jumble.append(self.first[t])
        random.shuffle(self.jumble)
        print(self.jumble)
        r=5
        c=0
        while c<6:
            self.letter = Label(self.master, text=self.jumble[c], bg="white")
            self.letter.grid(row=r,column=c)
            c+=1
        r=6
        c=0
        f=6
        while c<6 and f<12:
            self.letter = Label(self.master, text=self.jumble[f], bg="white")
            self.letter.grid(row=r, column=c)
            c+=1
            f+=1
         
        
             
    def Help(self):
        this = Tk()
        lab = Label(this, text="four pictures are provided to the player, with some similarity. The player is expected to make the word to which all the pictures are pointing, from the given letters and move to next level", bg="yellow")
        lab.pack()
        labe = Label(this, text="the player should enter letters in capital form", bg="green")
        labe.pack()
        
        
        this.mainloop()
        
    def levelchanger(self):
        if hasattr(self,'final'):
            if self.first == self.final:
                self.master.destroy()
                win2 = Tk ()
                myGame(win2)
                win2.mainloop()
            
        else:
            noEntry= Tk()
            noEntry.title('No Entry')
            erro = Label(noEntry, text='Submit Your Answer First', fg='red', font=('arial', '14', 'bold'), width=30)
            erro.pack()

    def getEntry(self):
        self.new = []
        for t in self.Ent:
            print(t.get())
            self.new.append(t.get())
        self.c = self.new
        self.final = "".join(self.c)
        print(self.final)
        if self.first == self.final:
            congo = Tk()
            congo.title("Congratulations ! You may proceed to the next Level")
            title = Label(congo, text='Correct Answer', bg='violet', fg='dark blue', width=45, height=3, font=('fixedsys', '18', 'bold'))
            title.pack()
            congo.mainloop()
        else:
            err= Tk()
            err.title("Wrong Answer")
            erro = Label(err, text='Wrong Answer !', fg='red', font=('arial', '14', 'bold'), width=20)
            erro.pack()
            err.mainloop
    def moveWord(self):

        y = 12 - len(self.first)
        chars = string.ascii_uppercase

        for j in range(y):
            self.let = random.choice(chars)
            self.letter = Label(self.master, text=self.let, bg="red")
            self.letter.pack()
        for t in range(len(self.first)):
            self.letter = Label(self.master, text=self.first[t], bg="red")
            self.letter.pack()



