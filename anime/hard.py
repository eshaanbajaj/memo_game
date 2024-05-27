import time
import threading
from tkinter import *
import random
import os
from PIL import Image, ImageTk
from tkinter import messagebox


class gameclass(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1900x850")
        self.config(bg="purple")
        self.number = 0
        self.number_list = []
        self.random_character = ""
        self.Label2 = Label(self, text="HARD", font=("Forte", 25),fg='#00FFFF', bg='purple')
        self.Label2.place(x=130, y=100)
        self.Label2 = Label(self, text="ANIME", font=("Forte", 40),fg='blue', bg='purple')
        self.Label2.place(x=80, y=35)
    def Label(self):
        self.Label1 = Label(self, text="", font=("times", 30), bg='purple')
        self.Label1.place(x=184, y=450)

        self.random_character_label = Label(self, text="", font=("times", 30), bg='white')
        self.Label1.place(x=274, y=450)

        self.button1 = Button(self, image="", bg='magenta', command=lambda: self.check(1), borderwidth=2, height=7, width=23)
        self.button1.place(x=350, y=25)
        
        self.button2 = Button(self, text="", bg='magenta', command=lambda: self.check(2), borderwidth=2, height=7, width=23)
        self.button2.place(x=570, y=25)

        self.button3 = Button(self, text="", bg='magenta', command=lambda: self.check(3), borderwidth=2, height=7, width=23)
        self.button3.place(x=790, y=25)

        self.button4 = Button(self, text="", bg='magenta', command=lambda: self.check(4), borderwidth=2, height=7, width=23)
        self.button4.place(x=1010, y=25)

        self.button5 = Button(self, text="", bg='magenta', command=lambda: self.check(5), borderwidth=2, height=7, width=23)
        self.button5.place(x=1230, y=25)

        self.button6 = Button(self, text="", bg='magenta', command=lambda: self.check(6), borderwidth=2, height=7, width=23)
        self.button6.place(x=350, y=155)

        self.button7 = Button(self, text="", bg='magenta', command=lambda: self.check(7), borderwidth=2, height=7, width=23)
        self.button7.place(x=570, y=155)

        self.button8 = Button(self, text="", bg='magenta', command=lambda: self.check(8), borderwidth=2, height=7, width=23)
        self.button8.place(x=790, y=155)

        self.button9 = Button(self, text="", bg='magenta', command=lambda: self.check(9), borderwidth=2, height=7, width=23)
        self.button9.place(x=1010, y=155)

        self.button10 = Button(self, text="", bg='magenta', command=lambda: self.check(10), borderwidth=2, height=7, width=23)
        self.button10.place(x=1230, y=155)

        self.button11 = Button(self, text="", bg='magenta', command=lambda: self.check(11), borderwidth=2, height=7, width=23)
        self.button11.place(x=350, y=285)

        self.button12 = Button(self, text="", bg='magenta', command=lambda: self.check(12), borderwidth=2, height=7, width=23)
        self.button12.place(x=570, y=285)

        self.button13 = Button(self, text="", bg='magenta', command=lambda: self.check(13), borderwidth=2, height=7, width=23)
        self.button13.place(x=790, y=285)

        self.button14 = Button(self, text="", bg='magenta', command=lambda: self.check(14), borderwidth=2, height=7, width=23)
        self.button14.place(x=1010, y=285)

        self.button15 = Button(self, text="", bg='magenta', command=lambda: self.check(15), borderwidth=2, height=7, width=23)
        self.button15.place(x=1230, y=285)
        
        self.button16 = Button(self, text="", bg='magenta', command=lambda: self.check(16), borderwidth=2, height=7, width=23)
        self.button16.place(x=350, y=415)

        self.button17 = Button(self, text="", bg='magenta', command=lambda: self.check(17), borderwidth=2, height=7, width=23)
        self.button17.place(x=570, y=415)
        
        self.button18 = Button(self, text="", bg='magenta', command=lambda: self.check(18), borderwidth=2, height=7, width=23)
        self.button18.place(x=790, y=415)
        
        self.button19 = Button(self, text="", bg='magenta', command=lambda: self.check(19), borderwidth=2, height=7, width=23)
        self.button19.place(x=1010, y=415)
        
        self.button20 = Button(self, text="", bg='magenta', command=lambda: self.check(20), borderwidth=2, height=7, width=23)
        self.button20.place(x=1230, y=415)
        
        self.button21 = Button(self, text="", bg='magenta', command=lambda: self.check(21), borderwidth=2, height=7, width=23)
        self.button21.place(x=350, y=545)
        
        self.button22 = Button(self, text="", bg='magenta', command=lambda: self.check(22), borderwidth=2, height=7, width=23)
        self.button22.place(x=570, y=545)       
        self.button23 = Button(self, text="", bg='magenta', command=lambda: self.check(23), borderwidth=2, height=7, width=23)
        self.button23.place(x=790, y=545)
        
        self.button24 = Button(self, text="", bg='magenta', command=lambda: self.check(24), borderwidth=2, height=7, width=23)
        self.button24.place(x=1010, y=545)
        
        self.button25 = Button(self, text="", bg='magenta', command=lambda: self.check(25), borderwidth=2, height=7, width=23)
        self.button25.place(x=1230, y=545)

        self.showbutton = Button(self,bg='cyan', text="show", command=self.start_shuffle, borderwidth=0, height=7, width=23)
        self.showbutton.place(x=100, y=360)

    def start_shuffle(self):
        # self.number_list=[]
        if (self.number % 2) == 0:
            self.number_list = os.listdir('.')
            self.number_list.remove("hard.py")
            self.number_list.remove("blank.png")
            random.shuffle(self.number_list)
            self.img1 = ImageTk.PhotoImage(Image.open(self.number_list[0]))
            self.button1 = Button(self, image=self.img1, command=lambda: self.check(1))
            self.button1.place(x=350, y=25)
            # button1.config(image=img)
            self.img2 = ImageTk.PhotoImage(Image.open(self.number_list[1]))
            self.button2 = Button(self, image=self.img2, command=lambda: self.check(2))
            self.button2.place(x=570, y=25)
            # button2.config(text=number_list[1])
            self.img3 = ImageTk.PhotoImage(Image.open(self.number_list[2]))
            self.button3 = Button(self, image=self.img3, command=lambda: self.check(3))
            self.button3.place(x=790, y=25)

            self.img4 = ImageTk.PhotoImage(Image.open(self.number_list[3]))
            self.button4 = Button(self, image=self.img4, command=lambda: self.check(4))
            self.button4.place(x=1010, y=25)

            self.img5 = ImageTk.PhotoImage(Image.open(self.number_list[4]))
            self.button5 = Button(self, image=self.img5, command=lambda: self.check(5))
            self.button5.place(x=1230, y=25)
            # button1.config(image=img)
            self.img6 = ImageTk.PhotoImage(Image.open(self.number_list[5]))
            self.button6 = Button(self, image=self.img6, command=lambda: self.check(6))
            self.button6.place(x=350, y=155)
            # button2.config(text=number_list[1])
            self.img7 = ImageTk.PhotoImage(Image.open(self.number_list[6]))
            self.button7 = Button(self, image=self.img7, command=lambda: self.check(7))
            self.button7.place(x=570, y=155)

            self.img8 = ImageTk.PhotoImage(Image.open(self.number_list[7]))
            self.button8 = Button(self, image=self.img8, command=lambda: self.check(8))
            self.button8.place(x=790, y=155)

            self.img9 = ImageTk.PhotoImage(Image.open(self.number_list[8]))
            self.button9 = Button(self, image=self.img9, command=lambda: self.check(9))
            self.button9.place(x=1010, y=155)

            self.img10 = ImageTk.PhotoImage(Image.open(self.number_list[9]))
            self.button10 = Button(self, image=self.img10, command=lambda: self.check(10))
            self.button10.place(x=1230, y=155)

            self.img11 = ImageTk.PhotoImage(Image.open(self.number_list[10]))
            self.button11 = Button(self, image=self.img11, command=lambda: self.check(11))
            self.button11.place(x=350, y=285)

            self.img12 = ImageTk.PhotoImage(Image.open(self.number_list[11]))
            self.button12 = Button(self, image=self.img12, command=lambda: self.check(12))
            self.button12.place(x=570, y=285)

            self.img13 = ImageTk.PhotoImage(Image.open(self.number_list[12]))
            self.button13 = Button(self, image=self.img13, command=lambda: self.check(13))
            self.button13.place(x=790, y=285)

            self.img14 = ImageTk.PhotoImage(Image.open(self.number_list[13]))
            self.button14 = Button(self, image=self.img14, command=lambda: self.check(14))
            self.button14.place(x=1010, y=285)

            self.img15 = ImageTk.PhotoImage(Image.open(self.number_list[14]))
            self.button15 = Button(self, image=self.img15, command=lambda: self.check(15))
            self.button15.place(x=1230, y=285)

            self.img16 = ImageTk.PhotoImage(Image.open(self.number_list[15]))
            self.button16 = Button(self, image=self.img16, command=lambda: self.check(16))
            self.button16.place(x=350, y=415)
            
            self.img17 = ImageTk.PhotoImage(Image.open(self.number_list[16]))
            self.button17 = Button(self, image=self.img17, command=lambda: self.check(17))
            self.button17.place(x=570, y=415)
            
            self.img18 = ImageTk.PhotoImage(Image.open(self.number_list[17]))
            self.button18 = Button(self, image=self.img18, command=lambda: self.check(18))
            self.button18.place(x=790, y=415)
            
            self.img19 = ImageTk.PhotoImage(Image.open(self.number_list[18]))
            self.button19 = Button(self, image=self.img19, command=lambda: self.check(19))
            self.button19.place(x=1010, y=415)
            
            self.img20 = ImageTk.PhotoImage(Image.open(self.number_list[19]))
            self.button20 = Button(self, image=self.img20, command=lambda: self.check(20))
            self.button20.place(x=1230, y=415)
            
            self.img21 = ImageTk.PhotoImage(Image.open(self.number_list[20]))
            self.button21 = Button(self, image=self.img21, command=lambda: self.check(21))
            self.button21.place(x=350, y=545)
            
            self.img22 = ImageTk.PhotoImage(Image.open(self.number_list[21]))
            self.button22 = Button(self, image=self.img22, command=lambda: self.check(22))
            self.button22.place(x=570, y=545)
            
            self.img23 = ImageTk.PhotoImage(Image.open(self.number_list[22]))
            self.button23 = Button(self, image=self.img23, command=lambda: self.check(23))
            self.button23.place(x=790, y=545)
            
            self.img24 = ImageTk.PhotoImage(Image.open(self.number_list[23]))
            self.button24 = Button(self, image=self.img24, command=lambda: self.check(24))
            self.button24.place(x=1010, y=545)
            
            self.img25 = ImageTk.PhotoImage(Image.open(self.number_list[24]))
            self.button25 = Button(self, image=self.img25, command=lambda: self.check(25))
            self.button25.place(x=1230, y=545)
            

            self.showbutton.config(text="Hide", bg='red')
            self.number = self.number + 1
            self.Label1.destroy()
            self.random_character_label.destroy()
            # print(jkb)
            # print(self.number_list)

            # return self.number_list,self.number
            return self.number


        else:
            self.random_character = random.choice(self.number_list)
            # print(self.random_character)
            # print(self.number_list)
            self.imgbtn = ImageTk.PhotoImage(Image.open("blank.png"))
            self.showbutton.config(text="Show",bg='cyan')
            self.button1.config(image=self.imgbtn)
            self.button2.config(image=self.imgbtn)
            self.button3.config(image=self.imgbtn)
            self.button4.config(image=self.imgbtn)
            self.button5.config(image=self.imgbtn)
            self.button6.config(image=self.imgbtn)
            self.button7.config(image=self.imgbtn)
            self.button8.config(image=self.imgbtn)
            self.button9.config(image=self.imgbtn)
            self.button10.config(image=self.imgbtn)
            self.button11.config(image=self.imgbtn)
            self.button12.config(image=self.imgbtn)
            self.button13.config(image=self.imgbtn)
            self.button14.config(image=self.imgbtn)
            self.button15.config(image=self.imgbtn)
            self.button16.config(image=self.imgbtn)
            self.button17.config(image=self.imgbtn)
            self.button18.config(image=self.imgbtn)
            self.button19.config(image=self.imgbtn)
            self.button20.config(image=self.imgbtn)
            self.button21.config(image=self.imgbtn)
            self.button22.config(image=self.imgbtn)
            self.button23.config(image=self.imgbtn)
            self.button24.config(image=self.imgbtn)
            self.button25.config(image=self.imgbtn)
            self.Label1 = Label(self, text="FIND THE IMAGE", font=("times", 30), bg='purple')
            self.Label1.place(x=500, y=700)

            self.random_character_label_image = ImageTk.PhotoImage(Image.open(self.random_character))
            self.random_character_label = Label(self, image=self.random_character_label_image)
            self.random_character_label.place(x=950, y=670)

            # number_list=[]
            self.number = self.number + 1
        # print(number_list,number)
        # return self.number_list,self.number

    def check(self, btnnmbr):
        if self.number_list == []:
            messagebox.showinfo("Memeory Game", "Lets start the Game first")
            return

        elif self.random_character == "":
            messagebox.showinfo("Memeory Game", "Lets start the Game first")

        # print(self.number_list)
        # print(self.random_character)
        elif btnnmbr == 1:
            if self.number_list[0] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 2:
            if self.number_list[1] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 3:
            if self.number_list[2] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 4:
            if self.number_list[3] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 5:
            if self.number_list[4] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 6:
            if self.number_list[5] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")


        elif btnnmbr == 7:
            if self.number_list[6] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 8:
            if self.number_list[7] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")


        elif btnnmbr == 9:
            if self.number_list[8] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
        elif btnnmbr == 10:
            if self.number_list[9] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
     
        elif btnnmbr == 11:
            if self.number_list[10] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
     
        elif btnnmbr == 12:
            if self.number_list[11] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
     
        elif btnnmbr == 13:
            if self.number_list[12] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
     
        elif btnnmbr == 14:
            if self.number_list[13] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
     
        elif btnnmbr == 15:
            if self.number_list[14] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
     
        elif btnnmbr == 16:
            if self.number_list[15] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
        elif btnnmbr == 17:
            if self.number_list[16] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
        elif btnnmbr == 18:
            if self.number_list[17] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
        elif btnnmbr == 19:
            if self.number_list[18] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
        elif btnnmbr == 20:
            if self.number_list[19] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 21:
            if self.number_list[20] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 22:
            if self.number_list[21] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 23:
            if self.number_list[22] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")
        elif btnnmbr == 24:
            if self.number_list[23] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice")

        elif btnnmbr == 25:
            if self.number_list[24] == self.random_character:
                messagebox.showinfo("Memeory Game", "Correct Choice") 

     
if __name__ == "__main__":
    Game = gameclass()
    Game.Label()
    Game.mainloop()
