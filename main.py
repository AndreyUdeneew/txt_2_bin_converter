# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import struct
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
from tkinter.filedialog import *
import os

def converter():
    # value=[]
    input_filename = filedialog.askopenfilename(parent=window)
    fileDir = os.path.split(input_filename)[0]
    print(fileDir)
    print(input_filename)
    output_filename = fileDir + '/output2FLASH_bin.bin'
    # read file as string:
    f = open(input_filename, 'r')
    mytxt = f.read()
    f.close()
    # print(mytxt)
    values = mytxt.split(",")
    # for word in mytxt.split(' '):
    #     values = str(values)
    #     values = re.sub(r'\n', '', values)
    #     values = re.sub(r'\]', '', values)
    #     values = re.sub(r'\[', '', values)
    #     values = re.sub(r'\[', '', values)
    int_txt = []

    for i in range(len(values)):
        int_txt.append(int((values[i]), base=16))

    with open(output_filename, 'wb') as fbinary:
        # pickle.dump(int_txt, fbinary)
        for i in range(len(values)):
            fbinary.write(int.to_bytes(int_txt[i],1,byteorder='big'))
        fbinary.close()
    text0.insert(INSERT, 'Готово')
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('300x100')
    window.title("txt_2_bin_converter")

    text0 = Text(width=7, height=1)
    text0.grid(column=1, row=1, sticky=(W))
    # text0.pack()

    btn0 = Button(window, text="Выбор файла для преобразования", command=converter)
    btn0.grid(column=0, row=1)

    window.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
