from tkinter import *
from stack import mystack
import string
import random
img=mystack()
img.push("C:\\Users\\AMR\\Desktop\\Candy.png")
img.push("C:\\Users\\AMR\\Desktop\\Round.png")
word=mystack()
word.push("CANDY")
word.push("ROUND")
class myGame:
    def __init__(self, master):
        
        self.label= Label(master, text="4 pics 1 word", bg="yellow")
        self.label.pack(side=TOP,fill=X)
        self.canvas = Canvas(width=400, height=250, bg="blue")
        self.canvas.pack()
        self.photo=PhotoImage(file=img.pop())
        self.canvas.create_image(75,0, image=self.photo, anchor=NW)
        self.first=word.pop()
        self.Ent=[]   
        
        #self.s=StringVar()
        
        for i in range(len(self.first)):
            
            self.entry= Entry(master)
            #, textvariable=self.s)
                #self.Ent.append(self.s1)
            #self.Ent.append(self.entry.get())
            #self.Ent.append(self.s1)
            self.entry.pack()
            self.Ent.append(self.entry)
        
            
        self.btn = Button(master, text="submit letter",command=self.getEntry)
        self.btn.pack()

        y=12-len(self.first)
        chars=string.ascii_uppercase
        
        for j in range(y):
            self.let=random.choice(chars)
            self.letter=Label(master, text=self.let, bg="red")
            self.letter.pack()
        for t in range(len(self.first)):
            self.letter=Label(master, text=self.first[t], bg="red")
            self.letter.pack()
            
        if self.first==self.final:
            b=myGame(root)
            return "you win"
        return "your word is not right"
        
        
        self.quitbutton = Button(master, text="Quit", command=master.quit)
        self.quitbutton.pack(side=BOTTOM)
            
    def getEntry(self):
        self.new=[]
        for t in self.Ent:
            print(t.get())
            self.new.append(t.get())
        self.c=self.new
        #for v in range(len(self.c)):
        self.final="".join(self.c)
        print(self.final)
       
         
    def moveWord(self):
        
        #print(self.Ent)
        #self.wordofuser=""
        #for h in range(len(self.first)):
            #self.wordofuser=self.wordofuser+self.Ent[h]
        #print(self.wordofuser)
        y=12-len(self.first)
        chars=string.ascii_uppercase
        
        for j in range(y):
            self.let=random.choice(chars)
            self.letter=Label(master, text=self.let, bg="red")
            self.letter.pack()
        for t in range(len(self.first)):
            self.letter=Label(master, text=self.first[t], bg="red")
            self.letter.pack()
            
        '''if self.first==self.final:
            b=myGame(root)
        
        
        self.quitbutton = Button(master, text="Quit", command=master.quit)
        self.quitbutton.pack(side=BOTTOM)'''
    #def getEntry():
        
class Level(myGame):
    def __init__(self):
        print("the level has changed")
        if super.self.first==super.self.final:
            super.myGame()
        
root=Tk()
a=myGame(root)
it=Level()
#b=myGame(root)
#a.moveWord()
root.mainloop()
