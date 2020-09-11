from tkinter import *
from PIL import ImageTk, Image
from typing import List
import tkinter.font as font


def display():
    a = (int(year.get())) / 100
    b = a / 4
    c = 2 - a + b
    e = 365.25 * (int((year.get())) + 4716)
    f = 30.6001 * (int((month.get())) + 1)
    jd = (c + (int(date.get())) + e + f) - 1524.5

    days_since_new = jd - 2451549.5
    new_moons = days_since_new / 29.53
    number_dec = new_moons - int(new_moons)
    days_into_cycle = int(number_dec * 29.53)

    if days_into_cycle == 0:
        result.set("Moon Cycle: New Moon (15 Days Till Full Moon)")
    elif days_into_cycle > 0 and days_into_cycle < 7:
        result.set("Moon Cycle: Waxing Crescent (11 Days Till Full Moon)")
    elif days_into_cycle == 7:
        result.set("Moon Cycle: First Quarter (8 Days Till Full Moon)")
    elif days_into_cycle > 7 and days_into_cycle < 15:
        result.set("Moon Cycle: Waxing Gibbous (4 Days Till Full Moon)")
    elif days_into_cycle == 15:
        result.set("Moon Cycle: Full Moon")
    elif days_into_cycle > 15 and days_into_cycle < 22:
        result.set("Moon Cycle: Waxing Gibbous (26 Days Till Full Moon)")
    elif days_into_cycle == 22:
        result.set("Moon Cycle: Third Quarter (22 Days Till Full Moon)")
    elif days_into_cycle > 22 and days_into_cycle < 28:
        result.set("Moon Cycle: Waning Crescent (18 Days Till Full Moon)")
    elif days_into_cycle == 29:
        result.set("Moon Cycle: New Moon (15 Days Till Full Moon)")


screen = Tk()
screen.geometry("700x1000")
screen.configure(bg='gray3')

myFont = font.Font(size=15)

screen.title("Moon Phase Calculator")

Label(text="", bg='gray3').pack()
Label(text="", bg='gray3').pack()

title = Label(text="MOON PHASE CALCULATOR", bg='IndianRed1')
title['font']=myFont
title.pack()
Label(text="", bg='gray3').pack()
Label(text="", bg='gray3').pack()

Options: List[str] = ['Choose Date', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
date = StringVar(screen)
date.set(Options[0])

OM1 = OptionMenu(screen, date, *Options)
OM1.configure(width=15, height=0, bd=1, bg='white')
OM1['font']=myFont
OM1.pack()

Label(text="", bg='gray3').pack()

Options: List[str] = ['Choose Month', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
month = StringVar(screen)
month.set(Options[0])

OM1 = OptionMenu(screen, month, *Options)
OM1.configure(width=15, height=0, bd=1, bg='white')
OM1['font']=myFont
OM1.pack()

Label(text="", bg='gray3').pack()
choose = Label(text="Choose Year", fg='white', bg='gray3')
choose['font']=myFont
choose.pack()
year = StringVar(screen)
SpinBox1 = Spinbox(screen,width=17, from_=2020, to=2050, increment=1, textvariable=year, bd=1)
SpinBox1['font']=myFont
SpinBox1.pack()

Label(text="", bg='gray3').pack()
Label(text="", bg='gray3').pack()

check = Button(text="Check", command=display, bg='RosyBrown1')
check['font']=myFont
check.pack()

Label(text="", bg='gray3').pack()

result = StringVar()
answer = Label(text="", textvariable=result, bg='gray3', fg="indianred1")
answer['font']=myFont
answer.pack()
Label(text="", bg='gray3').pack()
Label(text="", bg='gray3').pack()


def show_image():

    canvas = Canvas(screen, width=570, height=220, bg='gray3', highlightthickness=0)
    canvas.pack()

    img = Image.open("moonphases (2).png")
    img = img.resize((570, 220), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(290, 80, image=img)
    screen.mainloop()


if __name__ == '__main__':
    show_image()

Label(text="", bg='gray3').pack()
