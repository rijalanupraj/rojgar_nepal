import tkinter as tk
from tkinter import ttk
from back_end.connection import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os


class loginWindow(tk.Frame):
    def __init__(self, master):
        master.root.title('User Login')
        self.mastery = master
        self.account_type_var = tk.StringVar()
        self.dbconnect = DbConnection()

        # Initializing a frame.
        tk.Frame.__init__(self, master.root, highlightbackground="#f3ecc2", highlightcolor="#f3ecc2",
                          highlightthickness=1,
                          width=1280, height=1000, bd=2, pady=0, padx=10)

        # <============================================== Overall Frame ===============================================>

        overall_frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg="#898220")
        overall_frame.place(x=10, y=10, width=1200, height=900)

        title = tk.Label(overall_frame, text="Rojgar Nepal", bd=10, relief=tk.GROOVE, font=(
            "times new roman", 40, "bold"), bg="blue", fg="white")
        title.place(x=0, y=0, width=1200)
        title = tk.Label(overall_frame, text="Login Page", bd=10, relief=tk.RAISED, font=(
            "times new roman", 30, "bold"), bg="orange", fg="black")
        title.place(x=400, y=90, width=400)

        # <============================================== Login Frame =================================================>

        login_frame = tk.Frame(overall_frame, bd=4,
                               relief=tk.RIDGE, bg="#EDF0F5")
        login_frame.place(x=10, y=190, width=650, height=580)

        # To display the Heading of the Frame.
        login_heading = tk.Label(login_frame, text="Sign In", font=(
            "Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        login_heading.grid(row=1, column=0, pady=(5, 5), columnspan=2)

        # Variable where font is assigned.
        font_for_label_entry = ("Helvetica", 20, 'bold')

        # Label and entry for taking username and password.
        tk.Label(login_frame, text="Username", font=font_for_label_entry,
                 justify=tk.LEFT, bg="#EDF0F5", fg='Black').grid(row=2, column=0)
        self.login_username_entry = tk.Entry(
            login_frame, width=20, font=font_for_label_entry)
        self.login_username_entry.grid(
            row=2, column=1, ipady=10, pady=(0, 10), columnspan=2)
        tk.Label(login_frame, text="Password", font=font_for_label_entry,
                 justify=tk.LEFT, bg="#EDF0F5", fg='Black').grid(row=4, column=0)
        self.login_password_entry = tk.Entry(
            login_frame, show='*', width=20, font=font_for_label_entry)
        self.login_password_entry.grid(row=4, column=1, ipady=10, columnspan=2)

        tk.Label(login_frame, text="Account Type", font=font_for_label_entry,
                 justify=tk.LEFT, bg="#EDF0F5", fg='Black').grid(row=6, padx=10, column=0)
        combo_account_type = ttk.Combobox(login_frame, textvariable=self.account_type_var, font=(
            "times new roman", 12, "bold"), state="readonly")
        combo_account_type['values'] = ("User Login", "Company Login")
        combo_account_type.grid(row=6, column=1, ipady=10, pady=(10, 0))

        # Button for Login or navigating to create account page.
        self.login_button = tk.Button(login_frame, text="Sign In", font=("Helvetica", 25, 'bold'), bg='green',
                                      fg='white', command=lambda: self.login_button_clicked(master), bd=5)
        self.login_button.grid(row=8, column=0, pady=(10, 0), columnspan=2)

        # <============================================== Image Frame ===============================================>

        image_frame = tk.Frame(
            overall_frame, bd=4, relief=tk.RIDGE, bg="#EDF0F5")
        image_frame.place(x=700, y=190, width=450, height=580)

        register_heading = tk.Label(image_frame, text="What is Roger Nepal", font=(
            "Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        register_heading.grid(row=1, column=0, pady=(5, 25), columnspan=2)

        file = os.path.join(os.getcwd(), "images/man_job.jpg")
        img = Image.open(file)
        img = img.resize((440, 570), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(image_frame, image=img)
        panel.image = img
        panel.grid(row=1, column=0)

        # Button to navigate to register window
        tk.Button(overall_frame, text="Create an account Here ▶▶▶", font=("Helvetica", 20), bg='red', fg='white',
                  command=lambda :self.mastery.switch_frame('RegisterWindow'), bd=5).place(x=400, y=800, width=400)

    def login_button_clicked(self, master):
        """
        Check the username and password of the user.
        If it is correct directs to dashboard.
        Else show the error to the user.
        """
        did_it_match = False
        # Taking the username and password from entry form.
        # The username is not case sensitive.
        username_current_login_user = str(
            self.login_username_entry.get()).lower()
        password_current_login_user = str(self.login_password_entry.get())

        # If the username entry box or password entry box is empty the label will display "empty field"
        if username_current_login_user == '' or password_current_login_user == '':
            messagebox.showerror("Empty Field", "Enter Username and Password")
        elif self.account_type_var.get() == '':
            messagebox.showerror("Account Type", "Account Type should be either user or company")
        else:
            if self.account_type_var.get() == 'User Login':
                query = "SELECT username,password from user"
                existing_username_password = self.dbconnect.select(query)
            elif self.account_type_var.get() == 'Company Login':
                query = "SELECT username,password from company"
                existing_username_password = self.dbconnect.select(query)

            # Using for loop to check whether the password and username is current or not.
            for user, password in existing_username_password:
                if username_current_login_user == user and password_current_login_user == password:
                    did_it_match = True
                    break

            # If it matches the user will go to dashboard else invalid credentials will be displayed.
            if did_it_match:
                if self.account_type_var.get() == 'User Login':
                    self.mastery.assign_current_user(
                        username_current_login_user, 'user')
                    self.mastery.switch_frame('UserDashboard')
                else:
                    self.mastery.assign_current_user(
                        username_current_login_user, 'company')
                    self.mastery.switch_frame('CompanyDashboard')

            else:
                messagebox.showerror("Invalid Credentials", "Invalid Username & Password")

