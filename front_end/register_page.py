import tkinter as tk
from back_end.connection import *
from tkinter import messagebox
from model.user import User
from model.company import Company

class RegisterWindow(tk.Frame):
    def __init__(self, master):
        self.mastery = master
        master.root.title('Company Login')
        self.dbconnect = DbConnection()

        # Initialzing a frame.
        tk.Frame.__init__(self, master.root, highlightbackground="#f3ecc2", highlightcolor="#f3dcc2",
                          highlightthickness=1,
                          width=1280, height=1000, bd=2, pady=0, padx=10)

        # <============================================== Overall Frame ===============================================>

        overall_frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg="#898220")
        overall_frame.place(x=10, y=10, width=1200, height=900)

        title = tk.Label(overall_frame, text="Rojgar Nepal", bd=10, relief=tk.GROOVE, font=(
            "times new roman", 40, "bold"), bg="blue", fg="white")
        title.place(x=0, y=0, width=1200)
        title = tk.Label(overall_frame, text="Register Page", bd=10, relief=tk.RAISED, font=(
            "times new roman", 30, "bold"), bg="orange", fg="black")
        title.place(x=400, y=90, width=400)

        # <============================================== User Register Frame =========================================>

        user_register_frame = tk.Frame(
            overall_frame, bd=4, relief=tk.RIDGE, bg="#EDF0F5")
        user_register_frame.place(x=10, y=190, width=550, height=580)

        # To display the Heading of the Frame.
        login_heading = tk.Label(user_register_frame, text="User Register", font=(
            "Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        login_heading.grid(row=1, column=0, pady=(5, 5), columnspan=2)

        # Variable where font is asssigned.
        entry_widget_width = 30
        entry_widget_font = ("Helvetica")
        entry_widget_ipday = 15
        label_widget_font = ("Helvetica", 20)

        # Label and entry for taking username and password and other details.
        tk.Label(user_register_frame, text="Name", justify=tk.LEFT,
                 font=label_widget_font).grid(row=3, column=0, pady=(0, 4))
        self.user_register_name_entry = tk.Entry(
            user_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.user_register_name_entry.grid(
            row=3, column=1, pady=(0, 2), ipady=entry_widget_ipday)

        tk.Label(user_register_frame, text="Username", justify=tk.LEFT,
                 font=label_widget_font).grid(row=4, column=0, pady=(0, 4))
        self.user_register_username_entry = tk.Entry(
            user_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.user_register_username_entry.grid(
            row=4, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(user_register_frame, text="Phone Number", justify=tk.LEFT,
                 font=label_widget_font).grid(row=5, column=0, pady=(0, 4))
        self.user_register_phonenumber_entry = tk.Entry(
            user_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.user_register_phonenumber_entry.grid(
            row=5, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(user_register_frame, text="Address", justify=tk.LEFT,
                 font=label_widget_font).grid(row=6, column=0, pady=(0, 4))
        self.user_register_address_entry = tk.Entry(
            user_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.user_register_address_entry.grid(
            row=6, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(user_register_frame, text="Password", justify=tk.LEFT,
                 font=label_widget_font).grid(row=7, column=0, pady=(0, 4))
        self.user_register_password_entry = tk.Entry(
            user_register_frame, show='*', width=entry_widget_width, font=entry_widget_font)
        self.user_register_password_entry.grid(
            row=7, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(user_register_frame, text="Confirm Password", justify=tk.LEFT,
                 font=label_widget_font).grid(row=8, column=0, pady=(0, 4))
        self.user_register_confirm_password_entry = tk.Entry(
            user_register_frame, show='*', width=entry_widget_width, font=entry_widget_font)
        self.user_register_confirm_password_entry.grid(
            row=8, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        # This button will call 'reset_button_clicked' which will reset the values of the entry field.
        tk.Button(user_register_frame, text="Reset", font=("Helvetica", 17),
                  command=self.user_reset_button_clicked, bd=5).grid(row=12, column=1, pady=(10, 0))

        # This button when clicked call a fuction named 'register_button_clicked')
        tk.Button(user_register_frame, text="Reigster", font=("Helvetica", 20), bg='green', fg='white',
                  command=self.user_register_button_clicked, bd=5).grid(row=12, column=0, pady=(10, 0))

        # <============================================== Company Register Frame ======================================>

        company_register_frame = tk.Frame(
            overall_frame, bd=4, relief=tk.RIDGE, bg="#EDF0F5")
        company_register_frame.place(x=600, y=190, width=550, height=580)

        register_heading = tk.Label(company_register_frame, text="Company/Office Register", font=(
            "Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        register_heading.grid(row=1, column=0, pady=(5, 25), columnspan=2)

        # Label and Entry for filling user information in register page.

        tk.Label(company_register_frame, text="Company Name", justify=tk.LEFT,
                 font=label_widget_font).grid(row=3, column=0, pady=(0, 4))
        self.company_register_name_entry = tk.Entry(
            company_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.company_register_name_entry.grid(
            row=3, column=1, pady=(0, 2), ipady=entry_widget_ipday)

        tk.Label(company_register_frame, text="Username", justify=tk.LEFT,
                 font=label_widget_font).grid(row=4, column=0, pady=(0, 4))
        self.company_register_username_entry = tk.Entry(
            company_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.company_register_username_entry.grid(
            row=4, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(company_register_frame, text="Phone Number", justify=tk.LEFT,
                 font=label_widget_font).grid(row=5, column=0, pady=(0, 4))
        self.company_register_phonenumber_entry = tk.Entry(
            company_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.company_register_phonenumber_entry.grid(
            row=5, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(company_register_frame, text="Address", justify=tk.LEFT,
                 font=label_widget_font).grid(row=6, column=0, pady=(0, 4))
        self.company_register_address_entry = tk.Entry(
            company_register_frame, width=entry_widget_width, font=entry_widget_font)
        self.company_register_address_entry.grid(
            row=6, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(company_register_frame, text="Password", justify=tk.LEFT,
                 font=label_widget_font).grid(row=7, column=0, pady=(0, 4))
        self.company_register_password_entry = tk.Entry(
            company_register_frame, show='*', width=entry_widget_width, font=entry_widget_font)
        self.company_register_password_entry.grid(
            row=7, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(company_register_frame, text="Confirm Password", justify=tk.LEFT,
                 font=label_widget_font).grid(row=8, column=0, pady=(0, 4))
        self.company_register_confirm_password_entry = tk.Entry(
            company_register_frame, show='*', width=entry_widget_width, font=entry_widget_font)
        self.company_register_confirm_password_entry.grid(
            row=8, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        # This button will call 'reset_button_clicked' which will reset the values of the entry field.
        tk.Button(company_register_frame, text="Reset", font=("Helvetica", 17),
                  command=self.company_reset_button_clicked, bd=5).grid(row=12, column=1, pady=(10, 0))

        # This button when clicked call a fuction named 'register_button_clicked')
        tk.Button(company_register_frame, text="Reigster", font=("Helvetica", 20), bg='green', fg='white',
                  command=self.company_register_button_clicked, bd=5).grid(row=12, column=0, pady=(10, 0))

        tk.Button(overall_frame, text="Login Here ▶▶▶", font=("Helvetica", 20), bg='red', fg='white',
                  command=lambda: self.mastery.switch_frame('loginWindow'), bd=5).place(x=400, y=800, width=400)

    def user_register_button_clicked(self):
        """
        Checks the entry field after the register button is clicked.
        checks username in database if already used shows error.
        If all the entry are valid insert the data in database.
        """

        # Getting the value of each entry.
        # Username is not case sensitive
        name_current_user = self.user_register_name_entry.get()
        username_current_user = self.user_register_username_entry.get().lower()
        address_current_user = self.user_register_address_entry.get()
        password_current_user = self.user_register_password_entry.get()
        confirmation_password_current_user = self.user_register_confirm_password_entry.get()
        phonenumber_current_user = self.user_register_phonenumber_entry.get()

        # Taking the username of all user in one list and password in another list.
        query = "SELECT username from user"
        all_user_username_list = self.dbconnect.select(query)
        system_username_list = []
        for users in all_user_username_list:
            for user in users:
                system_username_list.append(user)
        # Checking the value before registration.

        # The value of entry cannot be empty.
        if username_current_user == '' or password_current_user == '' or name_current_user == '':
            messagebox.showerror("Empty Fields ", "You can\'t leave it empty")
        elif address_current_user == '' or confirmation_password_current_user == '' or phonenumber_current_user == '':
            messagebox.showerror("Empty Fields ", "You can\'t leave it empty")
        # Checking if the username,firstname,lastname has only alphabets only.
        # first name and last name can have space but username cannot have.
        elif not username_current_user.isalpha() or not all(x.isalpha() or x.isspace() for x in name_current_user):
            messagebox.showerror("Invalid Input", "Name and Username can only have alphabets")

        # #Username must be unique so checking in the list of username.
        elif username_current_user in system_username_list:
            messagebox.showerror("Invalid Username", 'Username already taken')

        # The phone number must be 10 numeric digit
        elif (not len(phonenumber_current_user) == 10) or (not phonenumber_current_user.isdigit()):
            messagebox.showerror("Invalid Phone Number", "Phone Number should be 10 numeric digit")
        elif len(name_current_user) > 99:
            messagebox.showerror("Invalid Name", "Name can only have upto 99 characters")
        elif len(username_current_user) > 44:
            messagebox.showerror("Invalid Username", "Username can be upto 44 characters only.")
        elif len(password_current_user) > 44:
            messagebox.showerror("Invalid Password", "Password can be only upto 44 characters.")
        # Checking if the password and confirm password is same or not.
        elif password_current_user != confirmation_password_current_user:
            messagebox.showerror("Invalid Passwords", "Your password don\'t match")

        # If the above condition doesn't meet then only the user get registered.
        else:
            user_ref = User(name_current_user, username_current_user,
                            phonenumber_current_user, address_current_user, password_current_user)
            query = 'INSERT INTO user (`name`, `username`, `phone`,`address`,`password`) VALUES (%s,%s,%s,%s,%s);'
            values = (user_ref.get_name(), user_ref.get_username(
            ), user_ref.get_phone(), user_ref.get_address(), user_ref.get_password())
            self.dbconnect.insert(query, values)
            messagebox.showinfo('success', 'Registeration Successful. You can now login')
            self.mastery.switch_frame('loginWindow')

    def company_register_button_clicked(self):
        """
         Checks the entry field after the register button is clicked.
        checks username in database if already used shows error.
        If all the entry are valid insert the data in database.
        """
        # Getting the value of each entry.
        # Username is not case sensitive
        name_current_user = self.company_register_name_entry.get()
        username_current_user = self.company_register_username_entry.get().lower()
        address_current_user = self.company_register_address_entry.get()
        password_current_user = self.company_register_password_entry.get()
        confirmation_password_current_user = self.company_register_confirm_password_entry.get()
        phonenumber_current_user = self.company_register_phonenumber_entry.get()

        # Taking the username of all user in one list and password in another list.
        query = "SELECT username from company"
        all_company_username_list = self.dbconnect.select(query)
        system_username_list = []
        for users in all_company_username_list:
            for user in users:
                system_username_list.append(user)

        # #Checking the value before registration.

        # The value of entry cannot be empty.
        if username_current_user == '' or password_current_user == '' or name_current_user == '':
            messagebox.showerror("Empty Fields ", "You can\'t leave it empty")
        elif address_current_user == '' or confirmation_password_current_user == '' or phonenumber_current_user == '':
            messagebox.showerror("Empty Fields ", "You can\'t leave it empty")

        # Checking if the username,firstname,lastname has only alphabets only.
        # first name and last name can have space but username cannot have.
        elif not username_current_user.isalpha() :
            messagebox.showerror("Invalid Input", "Name and Username can only have alphabets")

        # #Username must be unique so checking in the list of username.
        elif username_current_user in system_username_list:
            messagebox.showerror("Invalid Username", 'Username already taken')

        # The phone number must be 10 numeric digit
        elif (not len(phonenumber_current_user) == 10) or (not phonenumber_current_user.isdigit()):
            messagebox.showerror("Invalid Phone Number", "Phone Number should be 10 numeric digit")
        elif len(name_current_user) > 240:
            messagebox.showerror("Invalid Name", "Company Name can only have upto 240 characters")
        elif len(username_current_user) > 44:
            messagebox.showerror("Invalid Username", "Username can be upto 44 characters only.")
        elif len(password_current_user) > 44:
            messagebox.showerror("Invalid Password", "Password can be only upto 44 characters.")
        # Checking if the password and confirm password is same or not.
        elif password_current_user != confirmation_password_current_user:
            messagebox.showerror("Invalid Passwords", "Your password don\'t match")

        # If the above condition doesn't meet then only the user get registered.
        else:
            user_ref = Company(name_current_user, username_current_user,
                               phonenumber_current_user, address_current_user, password_current_user)
            query = 'INSERT INTO company (`name`, `username`, `phone`,`address`,`password`) VALUES (%s,%s,%s,%s,%s);'
            values = (user_ref.get_name(), user_ref.get_username(
            ), user_ref.get_phone(), user_ref.get_address(), user_ref.get_password())
            self.dbconnect.insert(query, values)
            messagebox.showinfo('success', 'Registeration Successful. You can now login')
            self.mastery.switch_frame('loginWindow')

    # When this function is called all the data in entry will be reset.
    def user_reset_button_clicked(self):
        """
        Deletes all the existing values in entry box.
        """
        self.user_register_name_entry.delete(0, 'end')
        self.user_register_username_entry.delete(0, 'end')
        self.user_register_address_entry.delete(0, 'end')
        self.user_register_password_entry.delete(0, 'end')
        self.user_register_confirm_password_entry.delete(0, 'end')
        self.user_register_phonenumber_entry.delete(0, 'end')


    def company_reset_button_clicked(self):
        """
        Deletes all the existing values in entry box.
        """
        self.company_register_name_entry.delete(0, 'end')
        self.company_register_username_entry.delete(0, 'end')
        self.company_register_address_entry.delete(0, 'end')
        self.company_register_password_entry.delete(0, 'end')
        self.company_register_confirm_password_entry.delete(0, 'end')
        self.company_register_phonenumber_entry.delete(0, 'end')


