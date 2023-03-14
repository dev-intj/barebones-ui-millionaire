from tkinter import *
import pygame
from PIL import Image, ImageTk

# setting up tkinter
pygame.init
root = Tk()
# window title
root.title("Who wants to be a Millionaire")
# dimensions
root.geometry('1280x720+0+0')
# background
root.configure(background='black')

# setting up screens

# helper variables
bd = 0  # I did 0 cause I would have to account borders in every frame build up
height = 720
width = 1280

main_width = 900
sidebar_width = width-main_width

# main screen
ROOT = Frame(root, bg="gray", bd=bd, width=width, height=height)
ROOT.grid(row=0, column=0)

MAIN = Frame(ROOT, bg="gray", bd=bd, width=main_width, height=height)
MAIN.grid(row=0, column=0)

MAINLogo = Frame(MAIN, bd=bd, bg="purple",
                 width=main_width, height=height/4 * 2)
MAINLogo.grid(row=0, column=0)

MAINquestions = Frame(MAIN, bg="yellow", bd=bd,
                      width=main_width, height=height/4 * 2)
MAINquestions.grid(row=1, column=0)


BackgroundImage = PhotoImage(file='assets/center.png')

LogoCenter = Button(MAINLogo, bd=bd, image=BackgroundImage,
                    bg="black", width=main_width, height=height/4 * 2)
LogoCenter.grid()

# sidebar screen (help options and prizes)

SIDEBAR = Frame(ROOT, bg="red", bd=bd, width=sidebar_width, height=height)
SIDEBAR.grid(row=0, column=1)

# options ( I don't know why its so complicated. )

options_width = sidebar_width / 4

options_height_full = height/4 * 1

options_height = 50

SIDEBARoptions = Frame(SIDEBAR, bg="red", bd=bd,
                       width=sidebar_width, height=height/4 * 1)
SIDEBARoptions.grid(row=0, column=0)

SIDEBARoptions5050 = Frame(SIDEBARoptions, bg="green", bd=bd,
                           width=options_width, height=options_height_full)

SIDEBARoptionsATA = Frame(SIDEBARoptions, bg="yellow", bd=bd,
                          width=options_width, height=options_height_full)
SIDEBARoptionsPAF = Frame(SIDEBARoptions, bg="red", bd=bd,
                          width=options_width, height=options_height_full)

# there is no way this is so complicated, i must be doing something wrong
SIDEBARoptions.rowconfigure(0, minsize=height/4 * 1)

SIDEBARoptions5050.grid(row=0, column=1)
SIDEBARoptionsATA.grid(row=0, column=2)
SIDEBARoptionsPAF.grid(row=0, column=3)

Classic5050Image = Image.open('assets/Classic5050.png')

ClassicATAImage = Image.open('assets/ClassicATA.png')

ClassicPAFImage = Image.open('assets/ClassicPAF.png')

resize_image5050 = Classic5050Image.resize((62, 48))
resize_imageATA = ClassicATAImage.resize((62, 48))
resize_imagePAF = ClassicPAFImage.resize((62, 48))


Classic5050I = ImageTk.PhotoImage(resize_image5050)

ClassicATAI = ImageTk.PhotoImage(resize_imageATA)

ClassicPAFI = ImageTk.PhotoImage(resize_imagePAF)


Classic5050 = Button(SIDEBARoptions5050, bd=bd, bg="red",
                     image=Classic5050I, width=options_width, height=options_height)

ClassicATA = Button(SIDEBARoptionsATA, bd=bd, bg="red",
                    image=ClassicATAI, width=options_width, height=options_height)

ClassicPAF = Button(SIDEBARoptionsPAF, bd=bd, bg="red",
                    image=ClassicPAFI, width=options_width, height=options_height)

Classic5050.grid()
ClassicATA.grid()
ClassicPAF.grid()


# prizes
SIDEBARprizes = Frame(SIDEBAR, bg="blue", bd=bd,
                      width=sidebar_width, height=height/4 * 3)
SIDEBARprizes.grid(row=1, column=0)


# run graphical interface on loop
root.mainloop()
