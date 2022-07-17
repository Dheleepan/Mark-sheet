# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import * 
import pyautogui
import datetime
import os, io
import easyocr
import json
from PIL import Image, ImageTk
cont = 0
cont1 = 0
directory = r'C:\Users\Dheleepan\Desktop\this\vision\snipss'   
total_file= []
for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
        total_file.append(filename) 
# creates a Tk() object
root = Tk()

root.title("Image viewer application using python")
root.resizable(0, 0)
# create frame
frame=Frame(root, width=600, height=500, bg='white', relief=GROOVE, bd=2)
frame.pack(side= LEFT,padx=10, pady=10)

images = []
# create thumbanials of all images
for j in total_file:
    img1 = Image.open(j)
    img1.thumbnail((1200, 1100))
    # open images to use with labels
    image1 = ImageTk.PhotoImage(img1)

    # create list of images
    images.append(image1)
# configure the image to the Label in frame
  
# sets the geometry of main 
# root window
root.geometry("1900x1050")

#bg = PhotoImage(file = "bg.png")
  
# Show image using label
#label1 = Label( root, image = bg)
#label1.place(x = 190, y = 150)

# function to open a new window 
# on a button click
region_list = []
def snip():

    
    class Application():
        def __init__(self, master):
            self.master = master
            self.rect = None
            self.x = self.y = 0
            self.start_x = None
            self.start_y = None
            self.curX = None
            self.curY = None

            #root.configure(background = 'red')
            #root.attributes("-transparentcolor","red")

            root.attributes("-transparent", "blue")
            root.geometry('300x40+1400+200')  # set new geometry
            #root.geometry('1925x1050')
            root.title('Snipper')
            self.menu_frame = Frame(master, width= 800, height=800, bg='white', relief=GROOVE, bd=2)
            self.menu_frame = Frame(master, bg='white', )
            self.menu_frame.pack(fill=BOTH, expand=YES)

            self.buttonBar = Frame(self.menu_frame,bg="white")
            self.buttonBar.pack(fill=BOTH,expand=YES)

            self.snipButton = Button(self.buttonBar, width=3, command=self.createScreenCanvas, background="black",text =" Snip ", fg='white', font=('ariel 15 bold'))
            self.snipButton.pack(expand=YES)

            self.master_screen = Toplevel(root)
            self.master_screen.withdraw()
            self.master_screen.attributes("-transparent", "blue")
            self.picture_frame = Frame(self.master_screen, background = "blue")
            self.picture_frame.pack(fill=BOTH, expand=YES)
        
        def takeBoundedScreenShot(self, x1, y1, x2, y2):
            a =[x1,y1,x2,y2]
            region_list.append(a)
            im = pyautogui.screenshot(region=(x1, y1, x2, y2))
            x = datetime.datetime.now()
            fileName = x.strftime("%f")
            im.save(fileName + ".png")
            
            
            directory = r'C:\Users\Dheleepan\Desktop\this\vision\snipss'
            for filename in os.listdir(directory):
                if filename.endswith('.png'):
                    remove_file = filename
                    ocr(filename)
                    os.remove(fileName + ".png")
            

            

        def createScreenCanvas(self):
            self.master_screen.deiconify()
            root.withdraw()

            self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="grey11")
            self.screenCanvas.pack(fill=BOTH, expand=YES)

            self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
            self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
            self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)

            self.master_screen.attributes('-fullscreen', True)
            self.master_screen.attributes('-alpha', .3)
            self.master_screen.lift()
            self.master_screen.attributes("-topmost", True)

        def on_button_release(self, event):

            if self.start_x <= self.curX and self.start_y <= self.curY:
                
                self.takeBoundedScreenShot(self.start_x, self.start_y, self.curX - self.start_x, self.curY - self.start_y)

            elif self.start_x >= self.curX and self.start_y <= self.curY:
                
                self.takeBoundedScreenShot(self.curX, self.start_y, self.start_x - self.curX, self.curY - self.start_y)

            elif self.start_x <= self.curX and self.start_y >= self.curY:
               
                self.takeBoundedScreenShot(self.start_x, self.curY, self.curX - self.start_x, self.start_y - self.curY)

            elif self.start_x >= self.curX and self.start_y >= self.curY:
                self.takeBoundedScreenShot(self.curX, self.curY, self.start_x - self.curX, self.start_y - self.curY)

            self.recPosition()            

            self.exitScreenshotMode()
            return event

        def exitScreenshotMode(self):
            self.screenCanvas.destroy()
            self.master_screen.withdraw()
            root.deiconify()

        def exit_application(self):
            print(self.region_list)
            print("Application exit")
            root.quit()

        def on_button_press(self, event):
            # save mouse drag start position
            self.start_x = self.screenCanvas.canvasx(event.x)
            self.start_y = self.screenCanvas.canvasy(event.y)

            self.rect = self.screenCanvas.create_rectangle(self.x, self.y, 1, 1, outline='red', width=3, fill="blue")

        def on_move_press(self, event):
            self.curX, self.curY = (event.x, event.y)
            # expand rectangle as you drag the mouse
            self.screenCanvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)


        def recPosition(self):
            '''print(self.start_x)
            print(self.start_y)
            print(self.curX)
            print(self.curY)

            print(self.region_list)'''



        



    root = Tk()
    app = Application(root)
    root.mainloop()




global i
i = 0
image_label = Label(frame, image=images[i])
image_label.pack(padx=10)
# create functions to display
# previous an next images
Label(root, text = "Student_name",bg='orange', fg='black', font=('ariel 15 bold')).place(x= 870, y= 100)
Label(root, text = "Subject",bg='grey', fg='black', font=('ariel 15 bold')).place(x= 1050, y= 170)
Label(root, text = "mark",bg='grey', fg='black', font=('ariel 15 bold')).place(x= 1300, y= 170)
Label(root, text = '(1).', fg='black', font=('ariel 15 bold')).place(x= 970, y= 240)
Label(root, text = '(2).', fg='black', font=('ariel 15 bold')).place(x= 970, y= 290)
Label(root, text = '(3).', fg='black', font=('ariel 15 bold')).place(x= 970, y= 340)
Label(root, text = '(4).', fg='black', font=('ariel 15 bold')).place(x= 970, y= 390)
Label(root, text = '(5).', fg='black', font=('ariel 15 bold')).place(x= 970, y= 440)
Label(root, text = '(6).', fg='black', font=('ariel 15 bold')).place(x= 970, y= 490)


student_name = Entry(root)
subject_1 = Entry(root)
mark_1 = Entry(root)
subject_2 = Entry(root)
mark_2 = Entry(root)
subject_3 = Entry(root)
mark_3 = Entry(root)
subject_4 = Entry(root)
mark_4 = Entry(root)
subject_5 = Entry(root)
mark_5 = Entry(root)
subject_6 = Entry(root)
mark_6 = Entry(root)

   


student_name.place(x =1080 , y =110)
subject_1.place(x =1010 , y= 250)
mark_1.place(x =1260 , y= 250)
subject_2.place(x =1010 , y= 300)
mark_2.place(x =1260 , y= 300)
subject_3.place(x =1010 , y= 350)
mark_3.place(x =1260 , y= 350)
subject_4.place(x =1010 , y= 400)
mark_4.place(x =1260 , y= 400)
subject_5.place(x =1010 , y= 450)
mark_5.place(x =1260 , y= 450)
subject_6.place(x =1010 , y= 500)
mark_6.place(x =1260 , y= 500)

l=[student_name,subject_1,mark_1,subject_2,mark_2,subject_3,mark_3,subject_4,mark_4,subject_5,mark_5,subject_6,mark_6]
all_list = []
def ocr(filename):
    global cont
    directory = r'C:\Users\Dheleepan\Desktop\this\vision\snipss'
    for file in os.listdir(directory):
        if file == filename:
            reader = easyocr.Reader(['en'])
            im = Image.open(filename)
            bounds = reader.readtext(filename)
            for i in bounds:
                l[cont].insert(0,i[1].upper())
                all_list.append(i[1])
                cont += 1

def save_changes():
    aa=student_name.get()
    bb=subject_1.get()
    cc=mark_1.get()
    dd=subject_2.get()
    ee=mark_2.get()
    ff=subject_3.get()
    gg=mark_3.get()
    hh=subject_4.get()
    ii=mark_4.get()
    jj=subject_5.get()
    kk=mark_5.get()
    ll=subject_6.get()
    mm=mark_6.get()
    print(aa)
    list_of_ = [aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm]
    print(list_of_)
    name_student = ''                
    sub_list =[]
    mark_list = []
    l = len(list_of_)
    for i in range(0,1):
        name_student = list_of_[i].upper().strip()
    for i in range(1,l,2):
        sub_list.append(list_of_[i].upper().strip())
    for i in range(2,l,2):
        mark_list.append(list_of_[i].upper().strip())

    res = {}
    for key in sub_list:
        for value in mark_list:
            res[key] = value
            mark_list.remove(value)
            break 

    res1 = {name_student:res}



    with open('mark.json', 'ab+') as f:
        f.seek(0,2)                               
        if f.tell() == 0 :
            #f.write('{'.encode())                        
            f.write(json.dumps(res1 , indent =5).encode())  
        else:
            f.seek(-1,2)           
            f.truncate()                         
            f.write(' , '.encode())              
            f.write(json.dumps(res1,indent = 5).encode())
            #f.write('}'.encode()) 
           





dub_list=[]
m=[student_name,subject_1,mark_1,subject_2,mark_2,subject_3,mark_3,subject_4,mark_4,subject_5,mark_5,subject_6,mark_6]
def ocr2(filename):
    global cont1
    directory = r'C:\Users\Dheleepan\Desktop\this\vision\snipss'
    for file in os.listdir(directory):
        if file == filename:
            reader = easyocr.Reader(['en'])
            im = Image.open(filename)
            bounds = reader.readtext(filename)
            for i in bounds:
                m[cont1].insert(0,i[1].upper())
                dub_list.append(i[1])
                cont1 += 1


def takeScreenShot( x1, y1, x2, y2):
    im = pyautogui.screenshot(region=(x1, y1, x2, y2))
    x = datetime.datetime.now()
    fileName = x.strftime("%f")
    im.save(fileName + ".png")
    fi = fileName + ".png"


    directory = r'C:\Users\Dheleepan\Desktop\this\vision\snipss'
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            remove_file = filename
            ocr2(filename)
            os.remove(fileName + ".png")



def next():
    global cont1
    cont = 0
    cont1 = 0
    dub_list.clear()

    student_name.delete('0',END)
    student_name.update()
    subject_1.delete('0', END)
    subject_1.update()
    mark_1.delete('0', END)
    mark_1.update()
    subject_2.delete('0', END)
    subject_2.update()
    mark_2.delete('0', END)
    mark_2.update()
    subject_3.delete('0', END)
    subject_3.update()
    mark_3.delete('0', END)
    mark_3.update()
    subject_4.delete('0', END)
    subject_4.update()
    mark_4.delete('0', END)
    mark_4.update()
    subject_5.delete('0', END)
    subject_5.update()
    mark_5.delete('0', END)
    mark_5.update()
    subject_6.delete('0', END)
    subject_6.update()
    mark_6.delete('0', END)
    mark_6.update()
    global i
    i = i + 1
    try:
        image_label.config(image=images[i])
        
    except:
        i = -1
        next()




def done():
    directory = r'C:\Users\Dheleepan\Desktop\this\vision\snipss'
    for file in os.listdir(directory):
        if file.endswith(".png"):
            os.remove(file)
    
    for i in region_list:
        x1 = i[0]
        y1 = i[1]
        x2 = i[2]
        y2 = i[3]
        takeScreenShot(x1,y1,x2,y2)


# a button widget which will open a 
# new window on button click
btn0 = Button(root,text ="Start Snipping", bg='black', fg='white', font=('ariel 15 bold'), relief=GROOVE,command = snip)
btn0.place(x =1700 ,y= 100)
btn4 = Button(root, text="process",bg='black', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=done)
btn4.place(x =1735 ,y= 300)
btn2 = Button(root, text="Next", width=8, bg='black', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=next)
btn2.place(x =1735 ,y= 200)
btn3 = Button(root, text="Exit", width=8, bg='black', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.place(x =1735 ,y= 500)
btn6 = Button(root, text="save", bg='black', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=save_changes)
btn6.place(x =1755 ,y= 400)


# mainloop, runs infinitely
root.mainloop()





        