from Tkinter import *
from PIL import Image, ImageTk

class Carriers():
    def __init__(self,e):
        self.__c = "C:/"
        self.__e = e

    def get_c(self):
        return self.__c

    def set_e(self, str):
        self.__e = str

    def get_e(self):
        return self.__e

    def __del__(self):
        print("Updating...")

carriers = Carriers("\n")

def handler_push():
    carriers.set_e("E:/")
    output.delete("0.0", "end")
    output.insert("1.0", str(carriers.get_c()))
    output.insert("1.3", str(carriers.get_e()))

def handler_pull():
    carriers.set_e("")
    output.delete("0.0", "end")
    output.insert("1.0", str(carriers.get_c()))
    output.insert("1.3", str(carriers.get_e()))

root = Tk()
root.geometry("400x420")
root.title("Disc Graphical Pattern")

frame1 = Frame(root)
frame1.grid()

image1 = Image.open("floppy.png")
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("computer_block.png")
photo2 = ImageTk.PhotoImage(image2)

labelp = Label(image=photo1)
labelp.image = (frame1, photo1)
labelp.grid(row=1,column=1)

labelc = Label(image=photo2)
labelc.image = (frame1, photo2)
labelc.grid(row=1,column=3)

label_carriers_list = Label(text="Current carriers:")
label_carriers_list.grid(row=3,column=1, pady=25)

output = Text(bg="lightblue", font="Arial 9", width=45, height=3)
output.grid(row=4, columnspan=4)

output.insert("0.0", carriers.get_c())

button_push = Button(text="Push ---->", command=handler_push)
button_push.grid(row=1,column=2)
button_push = Button(text="Pull <----", command=handler_pull)
button_push.grid(row=2,column=2)

root.mainloop()