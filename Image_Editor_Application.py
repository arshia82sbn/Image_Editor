#define the library
import tkinter as tk
from tkinter import filedialog , colorchooser
from PIL import Image, ImageTk ,ImageFilter , ImageOps
from tkinter import ttk

#define the add image function
def add_image():
    global file_path
    #define the variable to store the path of the image
    file_path = filedialog.askopenfilename(initialdir=r"C:\Users\Arshia\OneDrive\Documents\programming\python trian\GUI project\picture")
    image = Image.open(file_path)
    
    # Get the size of the canvas
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Resize the image to fit the canvas size
    image = image.resize((canvas_width, canvas_height), Image.LANCZOS)
    
    # Update the canvas size
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image  # Save a reference to avoid garbage collection
    canvas.create_image(0, 0, image=image, anchor="nw")
  
#define the draw function for drawing the line
def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')

#define the function for changing the color
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="select pen color")[1]

#define the function for chaning the size
def change_size(size):
    global pen_size
    pen_size = size

#define the clear order
def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0 ,0,image=canvas.image , anchor = "nw")

#define the apply filter on picture
def apply_filter(filter):
    image = Image.open(file_path)
    width , height = int(image.width / 2) , int(image.height / 2)
    image = image.resize((width, height) , Image.LANCZOS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0,0,image=image,anchor = "nw")
    

#main window
root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="white")

#define the pen setting
pen_color = "#000000"
pen_size = 5
file_path = r""

#make frame for toolbox
left_frame = tk.Frame(root, width=200, height=600, bg="#47CDD2")
left_frame.pack(side="left", fill="y")

#button for getting the image
image_button = tk.Button(left_frame, text="Add Image", bg="#FFFFFF", command=add_image)
image_button.pack(pady=15)

#button for changing the color
color_button = tk.Button(left_frame , text="Change pen color", command= change_color , bg="#FFFFFF")
color_button.pack(pady= 5)

#button for changing the size  of the pen
pen_size_frame = tk.Frame(left_frame, bg="#FFFFFF")
pen_size_frame.pack(pady=5)

#pen size changer ,small size
pen_size_1 = tk.Radiobutton(pen_size_frame , text= "Small", value=3 ,command= lambda:change_size(3) , bg="#FFFFFF")
pen_size_1.pack(side= 'left')
pen_size_1.select()

#pen size changer ,medium size
pen_size_2 = tk.Radiobutton(pen_size_frame , text="Medium" , value= 5 ,command= lambda:change_size(5), bg="#FFFFFF")
pen_size_2.pack(side="left")
pen_size_2.select()

#pen size changer, big size
pen_size_3 = tk.Radiobutton(pen_size_frame , text="Large" , value= 7 ,command= lambda:change_size(7), bg="#FFFFFF")
pen_size_3.pack(side='left')
pen_size_3.select()

#clear button
clear_button = tk.Button(left_frame, text="clear" , command= clear_canvas , bg="#FF9797")
clear_button.pack(pady=10)

#filter button
filter_label = tk.Label(left_frame,text="Select Filter",bg="#FFFFFF")
filter_label.pack()

#filter combobox
filter_combobox = ttk.Combobox(left_frame,values=["Black and White" , "blur" , "Emboss" , "Sharpen" , "smooth"])
filter_combobox.pack()

#filter bind
filter_combobox.bind("<<ComboboxSelected>>",lambda event: apply_filter(filter_combobox.get()))

#canvas
canvas = tk.Canvas(root, width=750, height=600)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

#loop for window
root.mainloop()
