import sys
from tkinter import *
import tkinter.ttk as ttk

def set_Tk_var():
    global che41
    che41 = IntVar()
    global che42
    che42 = IntVar()
    global che43
    che43 = IntVar()
    global radio_var
    radio_var = IntVar()
    global entry_string
    entry_string = StringVar()
    global text_string
    text_string = StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import web_scraper
    web_scraper.vp_start_gui()

