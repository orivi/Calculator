import tkinter as tk

window=tk.Tk()

#Applies characters to the screen
def apply(char):
    if len(screen.get()) < 14:
        lastChar = screen.get()[-1:]
        if lastChar == "+" or lastChar == "-" :
            if char == "+" or char == "-":
                char = ""
        screen.insert(tk.END, char)
    
#Clear and backspace
def delete():
    equation = screen.get()
    equation = equation[:-1]
    screen.delete(0, tk.END)
    screen.insert(tk.END, equation)
    
def clear():
    screen.delete(0, tk.END)

def displayResult(result):
    screen.delete(0, tk.END)
    screen.insert(tk.END, result)
    
def minusEquation(equation):
    try:
        equation = equation.split("-")
        result = int(equation[0])
        for number in equation:
            if int(number) == result:
                None
            else:
                result = result - int(number)
        return result
    except:
        screen.delete(0, tk.END)
        screen.insert(tk.END, "Try switching the numbers!")

def plusEquation(equation):
    try:
        result = 0
        for number in equation:
            result = result + int(number)
        return result
    except:
        screen.delete(0, tk.END)
        screen.insert(tk.END, "Try switching the numbers!")
    
#Equals
def equals():
    equation = screen.get()
    if "+" in equation:
        #for multiple operators
        if "-" in equation:
            equations = equation.split("+")
            simplifiedEquation = []
            for equation in equations:
                if "-" in equation:
                    simplifiedEquation.append(minusEquation(equation))
            displayResult(plusEquation(simplifiedEquation))
        
        #plus operator
        equation = screen.get().split("+")
        displayResult(plusEquation(equation))
        
    #minus operator
    if "-" in equation:
        if equation[0] == "-" and len(screen.split("-"))>2:
            if ValueError:
                screen.delete(0, tk.END)
                screen.insert(tk.END, "Try switching the numbers")
        else:
            displayResult(minusEquation(equation))
    else:
        lastChar = screen.get()[-1:]
        if lastChar == "+" or lastChar == "-" :
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Inappropriate operators")
        try:
            numbers = screen.get().split("+")
            for number in numbers:
                number.split("-")
                int(number)
        except:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Please use numbers")
        
if "__name__" == "__equals__":
    equals()

#User interface          
#Screen
screen=tk.Entry(window,width=15)
screen.grid(row=0,column=0,columnspan=3)

#Buttons
b1=tk.Button(window,text="1",command=lambda: apply(1))
b2=tk.Button(window,text="2",command=lambda: apply(2))
b3=tk.Button(window,text="3",command=lambda: apply(3))
b1.grid(row=4, column=0,pady=2)
b2.grid(row=4, column=1,pady=2)
b3.grid(row=4, column=2,pady=2)

b4=tk.Button(window,text="4",command=lambda: apply(4))
b5=tk.Button(window,text="5",command=lambda: apply(5))
b6=tk.Button(window,text="6",command=lambda: apply(6))
b4.grid(row=3,column=0,pady=2)
b5.grid(row=3,column=1,pady=2)
b6.grid(row=3,column=2,pady=2)

b7=tk.Button(window,text="7",command=lambda: apply(7))
b8=tk.Button(window,text="8",command=lambda: apply(8))
b9=tk.Button(window,text="9",command=lambda: apply(9))
b7.grid(row=2, column=0,pady=2)
b8.grid(row=2, column=1,pady=2)
b9.grid(row=2, column=2,pady=2)

b0=tk.Button(window,text="0",command=lambda: apply(0))
b0.grid(row=5,column=0,pady=2)

#Plus, minus, equal sign, clear and backspace
bplus=tk.Button(window,text="+",command=lambda: apply("+"))
bplus.grid(row=5, column=1)

bminus=tk.Button(window,text="-",command=lambda: apply("-"))
bminus.grid(row=5, column=2)

equals=tk.Button(window,text="=",command=equals,width=12)
equals.grid(row=6, column=0, columnspan=3,pady=2)

backspace=tk.Button(window,text="backspace",command=delete,width=6)
backspace.grid(row=1, column=1, columnspan=3)

clear=tk.Button(window,text="AC",command=clear,width=1)
clear.grid(row=1, column=0)

window.mainloop()