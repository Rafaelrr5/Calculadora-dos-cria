from tkinter import *
import time
##pyinstaller.exe --noconsole --icon=calc.ico calccria.py
#calculadora dos cria
def clique_s():
    pronto.place(x=100,y=220)
    result["text"]=("O seu resultado é: " + str(int(num1.get()) + int(num2.get())))

def clique_d():
    pronto.place(x=100,y=220)
    result["text"]=("O seu resultado é: " + str(int(num1.get()) / int(num2.get())))

def clique_m():
    pronto.place(x=100,y=220)
    result["text"]=("O seu resultado é: " + str(int(num1.get()) * int(num2.get())))

def clique_sub():
    pronto.place(x=100,y=220)
    result["text"]=("O seu resultado é: " + str(int(num1.get()) - int(num2.get())))

def poze():
    pozea = Label(jan,text=
    """
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣾⠟⡛⠿⠿⣭⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣽⡟⡏⢩⣦⡝⠋⢸⣶⠄⢲⡟⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣌⡳⣜⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⡛⢌⢿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠄⠙⠌⣸⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡿⠉⠉⠉⠉⢿⣿⣿⣿⠏⠉⠉⠉⠉⠉⠆⠄⠁⠄⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡗⠫⠿⠆⠄⠸⢿⣿⣿⠂⠒⠲⡿⠛⠛⠂⠄⠄⢠⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡛⣧⡔⠢⠴⣃⣠⣼⣿⣧⡀⠘⢢⣀⠄⠄⠄⠄⠄⢈⠁⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠄⠄⠄⣸⠆⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣼⢿⣿⣿⣿⣿⡀⠄⠘⡀⢠⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡌⠿⣫⣿⣦⠬⢭⣥⣶⣬⣾⣿⢿⣿⡟⠄⢀⣿⣶⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣧⠘⣉⠛⢻⣛⣛⣛⣻⡶⠮⠙⠃⣉⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡆⠸⣿⣶⢾⣿⣯⣤⣄⣀⣾⡟⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿
    ⠟⠿⠿⠿⠿⢿⣷⠄⣿⣿⣎⣹⢻⣿⣿⡿⡿⠁⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿
    ⠄⠄⠄⠄⠄⠄⠄⣠⠘⣿⣿⣿⣿⣿⣿⡟⠁⣀⣀⣀⠄⠘⠿⣿⣿⣿⣿⣿⣿⣿""")
    pozea.place(x=10,y=50)
    time.sleep(5)

jan = Tk()
jan.title("Calculadora dos cria")
jan.geometry("500x500+400+100")

tit=Label(jan,text="CALCULADORA DOS CRIA")
num1 = Entry(jan)
num2 = Entry(jan)
pronto = Label(jan,text="pronto")
result = Label(jan,text="Seu resultado aparecerá aqui")
soma = Button(jan,text="Soma", command=clique_s, width=10)
divi = Button(jan,text="Divisão", command=clique_d,width=10)
sub = Button(jan,text="Subtração",command=clique_sub,width=10)
mult = Button(jan,text="Multiplicação",command=clique_m,width=10)
poze=Button(jan,text="poze",width=5,command=poze)

tit.pack(side=TOP)
num1.place(x=100,y=100)
num2.place(x=100,y=150)
result.place(x=100,y=250)
soma.place(x=100,y=300)
divi.place(x=100,y=330)
sub.place(x=180,y=300)
mult.place(x=180,y=330)
poze.place(x=300,y=350)

jan.mainloop()