from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import controler
# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")
# create a functij to retrieve stuff


class UI:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("800x600")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)



        bg = ImageTk.PhotoImage(file="herons1.PNG")

        self.my_label = Label(self.root, image=bg)
        self.my_label.place(x=600, y=100)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Welcome to Herons")
        self.label.pack(pady=12, padx=20)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Full Name")
        self.entry1.pack(pady=12, padx=20)


        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Gender")
        self.entry2.pack(pady=12, padx=20)

        self.entry3 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Date of Birth")
        self.entry3.pack(pady=12, padx=20)

        self.entry4 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Email")
        self.entry4.pack(pady=12, padx=20)

        # flight information

        self.entry5 = customtkinter.CTkEntry(master=self.frame, placeholder_text="From")
        self.entry5.pack(pady=12, padx=20)


        self.entry6 = customtkinter.CTkEntry(master=self.frame, placeholder_text="To")
        #entry6.pack(pady=12, padx=20, side=customtkinter.LEFT)
        self.entry6.pack(pady=12, padx=20)

        self.entry7 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Depart")
        self.entry7.pack(pady=12, padx=20)

        self.entry8 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Return")
        self.entry8.pack(pady=12, padx=20)

        self.button = customtkinter.CTkButton(master=self.frame, text="Subscribe", command=lambda: self.startapp())
        self.button.pack(pady=12, padx=20)

        self.root.mainloop()

    def startapp(self):
        nameInput = self.entry1.get()
        genderInput = self.entry2.get()
        dobInput = self.entry3.get()
        emailInput = self.entry4.get()
        fromInput = self.entry5.get()
        toInput = self.entry6.get()
        departInput = self.entry7.get()
        returnInput = self.entry8.get()
        sub_info = [nameInput, genderInput, dobInput, emailInput,
              fromInput, toInput, departInput, returnInput]
        controler.WebScraper.connect_to_chrome(sub_info)
        #print(sub_info)


UI()