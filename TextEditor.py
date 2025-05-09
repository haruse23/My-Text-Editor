# Importing Required Modules/Submodules (Libraries)
from customtkinter import *
from tkinter import *
from tkinter import font

# Set a string filename to none
filename = ''

# Define functions, First File menu command functions, then listbox command functions
def openFile(event=None):
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def saveFile(event=None):
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveasFile(event=None):
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    f.write(t.rstrip())
 
def newFile(event=None):
    global filename
    filename='Untitled'
    text.delete(0.0, END)

def font_chooser(e):
    our_font.configure(family=font_listbox.get(font_listbox.curselection()))


def fontsize_chooser(e):
    our_font.configure(size=fontsize_listbox.get(fontsize_listbox.curselection()))


def fontstyle_chooser(e):
    style = fontstyle_listbox.get(fontstyle_listbox.curselection()).lower()

    if style == 'regular':
        our_font.configure(weight='normal', slant='roman', underline = 0, overstrike = 0)
    if style == 'bold':
        our_font.configure(weight='bold')
    if style == 'italic':
        our_font.configure(slant='italic')
    if style == 'bold/italic':
        our_font.configure(weight='bold', slant='italic')
    if style == 'underline':
        our_font.configure(underline= 1)
    if style == 'strike':
        our_font.configure(overstrike= 1)


def fontcolor_chooser(e):
    text.config(fg=fontcolor_listbox.get(fontcolor_listbox.curselection()).lower())

def textboxcolor_chooser(e):
    text.config(bg=textboxcolor_listbox.get(textboxcolor_listbox.curselection()).lower())

# Insert a Point in Undo Stack
def on_key(event):
    text.edit_separator()  







# Setting Application Theme to Dark
set_appearance_mode('DARK')

# Start of Code (Starting Function)
window = CTk()

# Window Geometry and Title
window.geometry("1200x900")
window.title("Omar's Text Editor")

# Textbox Frame
frame = Frame(window, width=1200, height=750)
frame.pack()

# Stop Frame from Expanding
frame.pack_propagate(False)

#Declaring the used font and the textbox (flexible textbox)
our_font = CTkFont(family='Helvetica', size=32)

text = Text(frame, undo=True, font=our_font, width=60, height=20)
text.pack(fill='both', expand=False)

#Key Binding the on_key function to Key Release (Any Key)
window.bind("<KeyRelease>", on_key)

# Redo Keyboard Shortcut
window.bind("<Control-Shift-Z>", lambda event: text.edit_redo())



#Creating File Menu
menubar = Menu(window)
filemenu = Menu(menubar)

# Adding commands to file menu and binding each command to a keyboard shortcut
filemenu.add_command(label='New    Ctrl+N', command=newFile)
window.bind('<Control-n>', newFile)

filemenu.add_command(label='Open    Ctrl+O', command=openFile)
window.bind('<Control-o>', openFile)

filemenu.add_command(label='Save    Ctrl+S', command=saveFile)
window.bind('<Control-s>', saveFile)

filemenu.add_command(label='Save As...    Ctrl+Shift+S', command=saveasFile)
window.bind('<Control-Shift-S>', saveasFile)

filemenu.add_separator()

filemenu.add_command(label='Quit', command=window.quit)

menubar.add_cascade(label='File', menu=filemenu)



# Creating a Bottom Frame to contain the labels and listboxes
bottom_frame = CTkFrame(window)
bottom_frame.pack(side='bottom', fill='x', padx=10, pady=10)


# Making Listboxes flexible
for i in range(5):  
    bottom_frame.columnconfigure(i, weight=1)
    bottom_frame.rowconfigure(i, weight=1)



# Defining Labels
font_label = CTkLabel(bottom_frame, text='Choose Font', font=('Helvetica', 14))
font_label.grid(row=0, column= 0, padx=10)


size_label = CTkLabel(bottom_frame, text='Choose Size', font=('Helvetica', 14))
size_label.grid(row=0, column= 1)

style_label = CTkLabel(bottom_frame, text='Choose Style', font=('Helvetica', 14))
style_label.grid(row=0, column= 2, padx=10)

color_label = CTkLabel(bottom_frame, text='Choose Color', font=('Helvetica', 14))
color_label.grid(row=0, column=3, padx=10)

color_label = CTkLabel(bottom_frame, text='Textbox Color', font=('Helvetica', 14))
color_label.grid(row=0, column=4, padx=10)





# Defining Listboxes
font_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=40, height=5)
font_listbox.grid(row=1, column=0, padx=10, sticky='nsew')

fontsize_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=40, height=5)
fontsize_listbox.grid(row=1, column=1, sticky='nsew')

fontstyle_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=40, height=5)
fontstyle_listbox.grid(row=1, column=2, padx=10, sticky='nsew')

fontcolor_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=40, height=5)
fontcolor_listbox.grid(row=1, column=3, padx=10, sticky='nsew')

textboxcolor_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=40, height=5)
textboxcolor_listbox.grid(row=1, column=4, padx=10, sticky='nsew')



# Font List
for f in font.families():
    font_listbox.insert('end', f)

# Font Size List
font_sizes = [8,10,12,20,24,50,60,100]
for size in font_sizes:
    fontsize_listbox.insert('end', size)

# Font Style List
font_styles = ['Regular', 'Bold', 'Italic', 'Bold/Italic', 'Underline', 'Strike']
for style in font_styles:
    fontstyle_listbox.insert('end', style)

#Font Color List
font_colors = ['Red', 'Blue', 'White', 'Black', 'Green', 'Orange', 'Yellow']
for color in font_colors:
    fontcolor_listbox.insert('end', color)

#Textbox Color List
textbox_colors = ['Red', 'Blue', 'White', 'Green', 'Orange', 'Yellow', 'Black']
for color in font_colors:
    textboxcolor_listbox.insert('end', color)


# Binding Listboxes' Commands to Functions on Left Mouse Button Release
font_listbox.bind('<ButtonRelease-1>', font_chooser)
fontsize_listbox.bind('<ButtonRelease-1>', fontsize_chooser)
fontstyle_listbox.bind('<ButtonRelease-1>', fontstyle_chooser)
fontcolor_listbox.bind('<ButtonRelease-1>', fontcolor_chooser)
textboxcolor_listbox.bind('<ButtonRelease-1>', textboxcolor_chooser)




window.config(menu=menubar)

# End of Code (Ending Function)
window.mainloop()