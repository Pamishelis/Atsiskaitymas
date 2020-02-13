import tkinter as tk
from tkinter import ttk

a = ' '

def press(num):
    global a
    a = a + str(num)
    equation.set(a)

def matrixsum():
    matrix1 = [[1, -2, 3, 4]]
    matrix2 = [[1, 1, 0, 6]]
    result = [[0, 0, 0, 0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    for total in result:
        equation.set(total)

def matrixmin():
    matrix1 = [[4, -2, 3]]
    matrix2 = [[1, 9, 15]]
    result = [[0, 0, 0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]

    for total in result:
        equation.set(total)

def equalpress():
    try:
        global a
        total = str(eval(a))
        equation.set(total)
        a = ' '

    except:
        equation.set('Negaliu atlikti veksmų')
        a = ' '
        a = '++'

def clear():
    global a
    a = ' '
    equation.set(' ')

if __name__ == '__main__':

#iššokantis langas

    dk = tk.Tk()
    dk.title('Skaičiuotuvas')
    dk.geometry('258x170')
    dk.maxsize(width=258, height=170)
    dk.configure(bg='white')


#ekranas

equation = tk.StringVar()
dis_entry = ttk.Entry(dk,width = 40, state = 'readonly', background = 'red',textvariable = equation)
dis_entry.grid(row = 0, columnspan = 10, ipadx = 6, ipady = 8)
dis_entry.focus()

#mygtukų ruošimas

btn7 = ttk.Button(dk, text = '7', width = 5, command = lambda:press(7))
btn7.grid(row = 1, column = 0, ipady = 4, ipadx = 2)

btn8 = ttk.Button(dk, text = '8', width = 5, command = lambda:press(8))
btn8.grid(row = 1, column = 1, ipady = 4, ipadx = 2)

btn9 = ttk.Button(dk, text = '9', width = 5, command = lambda:press(9))
btn9.grid(row = 1, column = 2, ipady = 4, ipadx = 2)

btnminus = ttk.Button(dk, text = '-', width = 8, command = lambda:press('-'))
btnminus.grid(row = 1, column = 3, ipady = 3, ipadx = 2)

btnkart = ttk.Button(dk, text = '*', width = 8, command = lambda:press('*'))
btnkart.grid(row = 1, column = 4, ipady = 3, ipadx = 2)

btn4 = ttk.Button(dk, text = '4', width = 5, command = lambda:press(4))
btn4.grid(row = 2, column = 0, ipady = 4, ipadx = 2)

btn5 = ttk.Button(dk, text = '5', width = 5, command = lambda:press(5))
btn5.grid(row = 2, column = 1, ipady = 4, ipadx = 2)

btn6 = ttk.Button(dk, text = '6', width = 5, command = lambda:press(6))
btn6.grid(row = 2, column = 2, ipady = 4, ipadx = 3)

btnplus = ttk.Button(dk, text = '+', width = 5, command = lambda:press('+'))
btnplus.grid(row = 2, column = 3, ipady = 4, ipadx = 10)

btndal = ttk.Button(dk, text = '/', width = 5, command = lambda:press('/'))
btndal.grid(row = 2, column = 4, ipady = 4, ipadx = 10)

btnequal = ttk.Button(dk, text = 'Enter', width = 5, command = equalpress)
btnequal.grid(row = 3, column = 4, ipady = 4, ipadx = 10)

btn0 = ttk.Button(dk, text = '0', width = 5, command = lambda:press(0))
btn0.grid(row = 3, column = 3, ipady = 4, ipadx = 10)

btn3 = ttk.Button(dk, text = '3', width = 5, command = lambda:press(3))
btn3.grid(row = 3, column = 2, ipady = 4, ipadx = 2)

btn2 = ttk.Button(dk, text = '2', width = 5, command = lambda:press(2))
btn2.grid(row = 3, column = 1, ipady = 4, ipadx = 2)

btn1 = ttk.Button(dk, text = '1', width = 5, command = lambda:press(1))
btn1.grid(row = 3, column = 0, ipady = 4, ipadx = 2)

btnclr = ttk.Button(dk, text = 'CE', width = 5, command = clear)
btnclr.grid(row = 4, column = 0, ipady = 4, ipadx = 2)

# btnmat = ttk.Button(dk, text = 'Matsum', width = 5, command = matrixsum)
# btnmat.grid(row = 4, column = 4, ipady = 4, ipadx = 6)
#
# btnmat = ttk.Button(dk, text = 'Matmin', width = 5, command = matrixmin)
# btnmat.grid(row = 4, column = 3, ipady = 4, ipadx = 6)

btnkl = ttk.Button(dk, text = '(', width = 5, command = lambda:press('('))
btnkl.grid(row = 4, column = 1, ipady = 4, ipadx = 2)

btnlk = ttk.Button(dk, text = ')', width = 5, command = lambda:press(')'))
btnlk.grid(row = 4, column = 2, ipady = 4, ipadx = 2)

dk.mainloop()