from tkinter import Canvas, Tk

# set the color variable
RECTANGLE_COLOR = "#D9D9D9"
color = "#F86263"
count = 0
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1,
              x1+radius, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


def on_next_click():
    print("Next button clicked")
    # change color of rectangle blocks
    global count
    if count == 0:
        canvas.itemconfig(rectangle3, fill=RECTANGLE_COLOR)
        canvas.itemconfig(rectangle4, fill=RECTANGLE_COLOR)
        x1, y1, x2, y2 = canvas.coords(rectangle2)
        midpoint = (y1 + y2) / 2
        canvas.create_text(150.0,360.0,anchor="nw",text="~  The process 100kb will be allocated to 128kb\n      with 28kb internal fragmentation\n \n\n",fill="#000000",font=("Inter Regular", 24 * -1))
        canvas.create_rectangle(x1, y1, x2, midpoint, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y1+10,anchor="nw",text="28kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x2, y2, x1, midpoint-20, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint-10,anchor="nw",text="100kb",fill="#000000",font=("Inter", 20 * -1))
        count+=1
    elif count == 1:
        canvas.itemconfig(rectangle3, fill=RECTANGLE_COLOR)
        canvas.itemconfig(rectangle4, fill=RECTANGLE_COLOR)
        x1, y1, x2, y2 = canvas.coords(rectangle2)
        midpoint = (y1 + y2) / 2
        canvas.create_rectangle(x1, y1, x2, midpoint, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y1+10,anchor="nw",text="28kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x2, y2, x1, midpoint-20, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint-10,anchor="nw",text="100kb",fill="#000000",font=("Inter", 20 * -1))

        x_1, y_1, x_2, y_2 = canvas.coords(rectangle5)
        midpoint1 = (y_1 + y_2) / 2
        canvas.create_text(150.0,480.0,anchor="nw",text="~  The process 530kb will be allocated to 1024kb\n      with 496kb internal fragmentation\n \n\n",fill="#000000",font=("Inter Regular", 24 * -1))
        canvas.create_rectangle(x_1, y_1, x_2, midpoint1, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y_1+10,anchor="nw",text="496kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x_2, y_2, x_1, midpoint1-20, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint1-10,anchor="nw",text="530kb",fill="#000000",font=("Inter", 20 * -1))
        count+=1

    elif count == 2:
        canvas.itemconfig(rectangle3, fill=RECTANGLE_COLOR)
        canvas.itemconfig(rectangle4, fill=RECTANGLE_COLOR)
        x1, y1, x2, y2 = canvas.coords(rectangle2)
        midpoint = (y1 + y2) / 2
        canvas.create_rectangle(x1, y1, x2, midpoint, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y1+10,anchor="nw",text="28kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x2, y2, x1, midpoint-20, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint-10,anchor="nw",text="100kb",fill="#000000",font=("Inter", 20 * -1))

        x_1, y_1, x_2, y_2 = canvas.coords(rectangle5)
        midpoint1 = (y_1 + y_2) / 2
        canvas.create_rectangle(x_1, y_1, x_2, midpoint1, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y_1+10,anchor="nw",text="496kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x_2, y_2, x_1, midpoint1-40, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint1-10,anchor="nw",text="530kb",fill="#000000",font=("Inter", 20 * -1))

        x_31, y_31, x_32, y_32 = canvas.coords(rectangle4)
        midpoint31 = (y_31 + y_32) / 2
        canvas.create_text(150.0,600.0,anchor="nw",text="~  The process 300kb will be allocated to 516kb\n      with 216kb internal fragmentation\n \n\n",fill="#000000",font=("Inter Regular", 24 * -1))
        canvas.create_rectangle(x_31, y_31, x_32, midpoint31, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y_31+10,anchor="nw",text="216kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x_32, y_32, x_31, midpoint31-20, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint31-10,anchor="nw",text="300kb",fill="#000000",font=("Inter", 20 * -1))
        count+=1
    
    elif count == 3:
        canvas.itemconfig(rectangle3, fill=RECTANGLE_COLOR)
        canvas.itemconfig(rectangle4, fill=RECTANGLE_COLOR)
        x1, y1, x2, y2 = canvas.coords(rectangle2)
        midpoint = (y1 + y2) / 2
        canvas.create_rectangle(x1, y1, x2, midpoint, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y1+10,anchor="nw",text="28kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x2, y2, x1, midpoint-20, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint-10,anchor="nw",text="100kb",fill="#000000",font=("Inter", 20 * -1))

        x_1, y_1, x_2, y_2 = canvas.coords(rectangle5)
        midpoint1 = (y_1 + y_2) / 2
        canvas.create_rectangle(x_1, y_1, x_2, midpoint1, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y_1+10,anchor="nw",text="496kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x_2, y_2, x_1, midpoint1-40, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint1-10,anchor="nw",text="530kb",fill="#000000",font=("Inter", 20 * -1))

        x_31, y_31, x_32, y_32 = canvas.coords(rectangle4)
        midpoint31 = (y_31 + y_32) / 2
        canvas.create_rectangle(x_31, y_31, x_32, midpoint31, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y_31+10,anchor="nw",text="216kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x_32, y_32, x_31, midpoint31-20, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint31-10,anchor="nw",text="300kb",fill="#000000",font=("Inter", 20 * -1))

        x_41, y_41, x_42, y_42 = canvas.coords(rectangle3)
        midpoint41 = (y_41 + y_42) / 2
        canvas.create_text(150.0,710.0,anchor="nw",text="~  The process 200kb will be allocated to 256kb\n      with 56kb internal fragmentation\n \n\n",fill="#000000",font=("Inter Regular", 24 * -1))
        canvas.create_rectangle(x_41, y_41, x_42, midpoint41, fill=RECTANGLE_COLOR, outline="")
        canvas.create_text(1108.0,y_41+5,anchor="nw",text="56kb",fill="#000000",font=("Inter", 20 * -1))
        canvas.create_rectangle(x_42, y_42, x_41, midpoint41-50, fill="#F86263", outline="")
        canvas.create_text(1108.0,midpoint41-10,anchor="nw",text="200kb",fill="#000000",font=("Inter", 20 * -1))
        count+=1
    

window = Tk()
window.geometry("780x600")
window.configure(bg="#FFFFFF")
canvas = Canvas(window,bg="#FFFFFF",height=1024,width=1440,bd=0,highlightthickness=0,relief="ridge")
canvas.place(x=0, y=0)
canvas.create_text(120.0,47.0,anchor="nw",text="First Fit Management",fill="#000000",font=("Inter Bold", 20 * -1))
canvas.create_text(70.0,98.0,anchor="nw",text="Lets say the process request queue as follows:\n\n\n\n\n\n",fill="#000000",font=("Inter Medium", 15 * -1))
rectangle1 = create_rounded_rectangle(canvas,29.0,510.0,120.0,580.0,40,fill=RECTANGLE_COLOR,outline="")
rectangle2 = canvas.create_rectangle(450.0,480.0,700.0,550.0,fill=RECTANGLE_COLOR,outline="")
rectangle3 = canvas.create_rectangle(450.0,300.0,700.0,786.0,fill=RECTANGLE_COLOR,outline="")
rectangle4 = canvas.create_rectangle(450.0,200.0,1365.0,617.0,fill=RECTANGLE_COLOR,outline="")
rectangle5 = canvas.create_rectangle(450.0,100.0,1365.0,388.0,fill=RECTANGLE_COLOR,outline="")
next_button = canvas.create_text(30.0,530.0,anchor="nw",text="   NEXT",fill="#000000",font=("Inter Medium", 15 * -1), tags="next_button")
canvas.create_text(1108.0,223.0,anchor="nw",text="1024kb",fill="#000000",font=("Inter", 20 * -1))
# canvas.create_text(1108.0,183.0,anchor="nw",text="1024kb",fill="#000000",font=("Inter", 20 * -1))
canvas.create_text(1108.0,644.0,anchor="nw",text="256kb",fill="#000000",font=("Inter", 20 * -1))
canvas.create_text(1108.0,427.0,anchor="nw",text="516kb",fill="#000000",font=("Inter", 20 * -1))
canvas.create_text(1108.0,813.0,anchor="nw",text="128kb",fill="#000000",font=("Inter", 20 * -1))
canvas.create_text(120.0,100.0,anchor="nw",text="\n\n{100kb,530kb,300kb,200kb}",fill="#000000",font=("Inter Medium", 15 * -1))
canvas.tag_bind("next_button", "<Button-1>", lambda event: on_next_click())
window.mainloop()
