# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
import os
import numpy as np
from os import path


def converter():
    input_filename = filedialog.askopenfilename(parent=window)
    fileDir = os.path.split(input_filename)[0]
    print("wtf")
    print(fileDir)
    print("wtf")
    # filename = "C:/Users/Stasy/Desktop/test.txt"
    # input_filename=fileDir+'/output2FLASH_bin.txt'
    output_filename = fileDir + '/output2FLASH_bin.txt'
    # read file as string:
    f = open(input_filename, 'r')
    mytxt = f.read()
    print("wtf")
    print("\r\n")

    # change text into binary mode:
    binarytxt = int(mytxt,16)
    hex_txt = hex(binarytxt)
    # print(hex_txt)
    # print()
    # print(mytxt)
    # binarytxt = str.encode(txt)
    # save the bytes object
    with open(output_filename, 'wb') as fbinary:
        fbinary.write(hex_txt)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('300x100')
    window.title("txt_2_bin_converter")

    # lbl0 = Label(window, text="Выбор полноэкранных картинок")
    # lbl0.grid(column=0, row=1)

    text0 = Text(width=7, height=1)
    text0.grid(column=1, row=1, sticky=(W))
    # text0.pack()

    btn0 = Button(window, text="Выбор файла для преобразования", command=converter)
    btn0.grid(column=0, row=1)

    window.mainloop()
    print_hi('byeCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
