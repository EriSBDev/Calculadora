from tkinter import *
from tkinter import ttk

# funções


def clear():
    global value_typed
    value_typed = ''
    get_result.set('0')


def calc():
    global value_typed
    try:
        result = (f'{eval(value_typed):.2f}')
        result_float = float(result)
        if result_float.is_integer():
            result = str(int(result_float))
        get_result.set(result)

    except SyntaxError:
        value_typed = "Erro de sintaxe!"


def entry_value(event):
    global value_typed
    value_typed = value_typed + str(event)
    get_result.set(value_typed)


# globais
value_typed = ''

# cores
cor1 = '#ff9d00'    # laranja
cor2 = '#ede3d3'    # laranja claro
black = '#000000'   # preto
white = '#ffffff'   # branco

# janela principal
janela = Tk()
janela.title('EriCalc')
janela.config(bg=black)

# frame visor
frame_tela = Frame(janela)
frame_tela.pack()

# frame body
frame_body = Frame(janela)
frame_body.config(relief='solid', )
frame_body.pack()

frame_body.columnconfigure(0, weight=1)
frame_body.rowconfigure(0, weight=1)

# label visor
get_result = StringVar()
visor_label = Label(frame_tela, textvariable=get_result, font=('Helvetica 20'), bg=cor2, anchor='e',
                    width=14, height=2, padx=7, relief='solid')
visor_label.grid(row=0, column=0)

# creating buttons and positions
height_buttons = 2
width_majority_buttons = 5
width_bigger_buttons = 11
horizontal_spacing_buttons = 1/3
vertical_spacing_buttons = 1/3
font_buttons = "Helvetica 13 bold"

b_1 = Button(frame_body, command=clear, text='C', width=width_bigger_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_1.grid(row=0, column=0, columnspan=2,
         padx=horizontal_spacing_buttons, pady=vertical_spacing_buttons)

b_2 = Button(frame_body, command=lambda: entry_value('%'), text='Resto',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_2.grid(row=0, column=2, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_3 = Button(frame_body, command=lambda: entry_value('/'), text='/',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_3.grid(row=0, column=3, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_4 = Button(frame_body, command=lambda: entry_value('7'), text='7',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_4.grid(row=1, column=0, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_5 = Button(frame_body, command=lambda: entry_value('8'), text='8',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_5.grid(row=1, column=1, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_6 = Button(frame_body, command=lambda: entry_value('9'), text='9',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_6.grid(row=1, column=2, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_7 = Button(frame_body, command=lambda: entry_value('*'), text='*',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_7.grid(row=1, column=3, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_8 = Button(frame_body, command=lambda: entry_value('4'), text='4',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_8.grid(row=2, column=0, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_9 = Button(frame_body, command=lambda: entry_value('5'), text='5',
             width=width_majority_buttons, height=height_buttons, bg=cor1,
             font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_9.grid(row=2, column=1, padx=horizontal_spacing_buttons,
         pady=vertical_spacing_buttons)

b_10 = Button(frame_body, command=lambda: entry_value('6'), text='6',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_10.grid(row=2, column=2, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

b_11 = Button(frame_body, command=lambda: entry_value('-'), text='-',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_11.grid(row=2, column=3, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

b_12 = Button(frame_body, command=lambda: entry_value('1'), text='1',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_12.grid(row=3, column=0, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

b_13 = Button(frame_body, command=lambda: entry_value('2'), text='2',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_13.grid(row=3, column=1, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

b_14 = Button(frame_body, command=lambda: entry_value('3'), text='3',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_14.grid(row=3, column=2, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

b_15 = Button(frame_body, command=lambda: entry_value('+'), text='+',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_15.grid(row=3, column=3, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

b_16 = Button(frame_body, command=lambda: entry_value('0'), text='0',
              width=width_bigger_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_16.grid(row=4, column=0, columnspan=2,
          padx=horizontal_spacing_buttons, pady=vertical_spacing_buttons)

b_17 = Button(frame_body, command=lambda: entry_value('.'), text='.',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_17.grid(row=4, column=2, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

b_18 = Button(frame_body, command=calc, text='=',
              width=width_majority_buttons, height=height_buttons, bg=cor1,
              font=(font_buttons), relief=RAISED, overrelief=RIDGE)
b_18.grid(row=4, column=3, padx=horizontal_spacing_buttons,
          pady=vertical_spacing_buttons)

janela.mainloop()
print('teste')
