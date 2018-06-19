import sys
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as tkMessageBox
import tkinter.ttk as ttk
import _support
import PIL
from PIL import Image ,ImageTk
import os

import model_1 as model

sys.path.append("C:/Users/islam/Desktop/web_scraping_by_image/web_scraping")   
from final_2 import scraper
# import commands
top = None
image_path = ""
selected_image = None
def start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    _support.set_Tk_var()
    global top
    top = Web_Scraper_Manager (root)
    _support.init(root, top)
    root.mainloop()

w = None
def create_Web_Scraper_Manager(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    _support.set_Tk_var()
    top = Web_Scraper_Manager (w)
    _support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Web_Scraper_Manager():
    global w
    w.destroy()
    w = None

def radio_text_command():
    top.Entry2.configure(state="disabled")
    top.Entry1.configure(state="normal")
    top.Button1.configure(state="disabled")

def radio_image_command():
    top.Entry1.configure(state="disabled")
    top.Entry2.configure(state="readonly")
    top.Button1.configure(state="normal")

def button_open_command():
    image_path = askopenfilename(initialdir = "/",title = "Select image file to detect obj.",filetypes = (("image files","*.jpg *.jpeg *.png"),))
    _support.entry_string.set(image_path)
    ######### image resizing #########
    # open as a PIL image object
    pil_image = Image.open(image_path)
    # get the size of the original image
    width_org, height_org = pil_image.size
    factor = 1
    canv_w , canv_h = top.Canvas1.winfo_width(), top.Canvas1.winfo_height()
    if width_org < height_org:
        factor = float(canv_w/width_org)
    else:
        factor = float(canv_h/height_org)

    width = int(width_org * factor)
    height = int(height_org * factor)
    # use one of these filter options to resize the image:
    # Image.NEAREST     use nearest neighbour
    # Image.BILINEAR    linear interpolation in a 2x2 environment
    # Image.BICUBIC     cubic spline interpolation in a 4x4 environment
    # Image.ANTIALIAS   best down-sizing filter
    global pil_image2
    pil_image2 = pil_image.resize((width, height), Image.ANTIALIAS)   

    # convert PIL image object to Tkinter PhotoImage object
    global tk_image
    tk_image = ImageTk.PhotoImage(pil_image2)
    top.Canvas1.create_image(5, 10, image=tk_image,anchor=NW)

    

def button_scrap_command():
    print(_support.radio_var.get())  #testing  
    # radio_var:   1--Scrap by image   2--scrap by text

    if(_support.radio_var.get()==1): #image
        try: #open image file -- apply api detection -- showimage updated -- start scarping
            new_image , string_list = model.detect_from_image(pil_image2)
            print(string_list)
            tk_image = ImageTk.PhotoImage(new_image)
            top.Canvas1.create_image(5, 10, image=tk_image,anchor=NW)
            top.Canvas1.update()
        except Exception as e:
            tkMessageBox.showerror("no image found", "the file selected not found .. or not a valid image !\n")
            print(e)

        final_items = list()
        for item in string_list:
            if item not in final_items:
                final_items.append(item)

        print(final_items)
        scrap = scraper()
        for item in final_items:
            if(_support.che43.get()):
                scrap.newEggScrap(item)
            if(_support.che42.get()):
                scrap.souqScrap(item)
            if(_support.che41.get()):
                scrap.aliExpressScrap(item)
            final_list = scrap.get_files()
            print(final_list)
            for file in final_list:
                top.Listbox1.insert(END, file)
        print('DONE')

    else:            #text
        #start scraping
        scrap = scraper()
        s = _support.text_string.get().rstrip()
        if(_support.che43.get()):
            scrap.newEggScrap(s)
        if(_support.che42.get()):
            scrap.souqScrap(s)
        if(_support.che41.get()):
            scrap.aliExpressScrap(s)
        final_list = scrap.get_files()
        #final_list = ['islam','alien','moon'] #for testing :)
        print(final_list)
        for file in final_list:
            top.Listbox1.insert(END, file)
        print('DONE')
    

def Listbox_onselect(self):
    path_t = top.Listbox1.get(ANCHOR)
    print(path_t)  
    os.startfile(path_t)





class Web_Scraper_Manager(object):
    def __init__(self, top=1):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("859x805+347+125")
        top.title("Web Scraper Manager")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.04, rely=0.04, height=24, width=178)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Scarp By Text input''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.04, rely=0.09, height=35, width=188)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Scrap By Image input''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.27, rely=0.04,height=31, relwidth=0.67)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(state="disabled")
        self.Entry1.configure(textvariable = _support.text_string)
        _support.text_string.set("write...")

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.27, rely=0.09,height=31, relwidth=0.61)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(state="readonly")
        self.Entry2.configure(textvariable = _support.entry_string)
        _support.entry_string.set("click open and choose image...")        

        self.Button1 = Button(top)
        self.Button1.place(relx=0.9, rely=0.09, height=31, width=43)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''open''')
        self.Button1.configure(command=button_open_command)

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.05, rely=0.15, relheight=0.51, relwidth=0.9)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=773)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.05, rely=0.68, height=31, width=315)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font9)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Select Websites to Scrap (at least one) :''')

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.44, rely=0.68, relheight=0.05
                , relwidth=0.13)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font=font9)
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Ali Express''')
        self.Checkbutton1.select()
        self.Checkbutton1.configure(variable=_support.che41)

        self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.61, rely=0.68, relheight=0.05
                , relwidth=0.08)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(font=font9)
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Souq''')
        self.Checkbutton2.select()
        self.Checkbutton2.configure(variable=_support.che42)

        self.Checkbutton3 = Checkbutton(top)
        self.Checkbutton3.place(relx=0.73, rely=0.68, relheight=0.05
                , relwidth=0.12)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(activeforeground="#000000")
        self.Checkbutton3.configure(background="#d9d9d9")
        self.Checkbutton3.configure(disabledforeground="#a3a3a3")
        self.Checkbutton3.configure(font=font9)
        self.Checkbutton3.configure(foreground="#000000")
        self.Checkbutton3.configure(highlightbackground="#d9d9d9")
        self.Checkbutton3.configure(highlightcolor="black")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''NewEGG''')
        self.Checkbutton3.select()
        self.Checkbutton3.configure(variable=_support.che43)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.05, rely=0.75, height=31, width=347)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font9)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Output ( csv file for each object detected ) :''')

        self.menubar = Menu(top,font=font10,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.05, rely=0.8, relheight=0.1, relwidth=0.9)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font=font11)
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=774)
        self.Listbox1.config( selectmode = SINGLE )
        self.Listbox1.bind('<<ListboxSelect>>', Listbox_onselect)


        self.Button2 = Button(top)
        self.Button2.place(relx=0.73, rely=0.92, height=48, width=188)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Start Scraping''')
        self.Button2.configure(width=188)
        self.Button2.configure(command=button_scrap_command)

        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.05, rely=0.92, relheight=0.05
                , relwidth=0.18)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font9)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Scrap By Image''')
        self.Radiobutton1.configure(variable=_support.radio_var, value=1)
        self.Radiobutton1.configure(command=radio_image_command)
        self.Radiobutton1.select()

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.3, rely=0.92, relheight=0.05
                , relwidth=0.16)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font9)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Scrap By Text''')
        self.Radiobutton2.configure(variable=_support.radio_var, value=2)
        self.Radiobutton2.configure(command=radio_text_command)






if __name__ == '__main__':
    start_gui()


