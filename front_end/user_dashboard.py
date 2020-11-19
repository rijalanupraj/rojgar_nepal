import tkinter as tk
from back_end.connection import *
from model.user import User
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

class UserDashboard(tk.Frame):
    def __init__(self, master):
        master.root.title('User Dashboard')
        self.mastery = master
        self.dbconnect = DbConnection()

        self.user_name_entry = StringVar()
        self.user_username_entry = StringVar()
        self.user_phonenumber_entry = StringVar()
        self.user_address_entry = StringVar()
        self.user_confirm_password_entry = StringVar()
        self.user_password_entry = StringVar()

        # Initializing a frame.
        tk.Frame.__init__(self, master.root, highlightbackground="#f3ecc2", highlightcolor="#f3ecc2",
                          highlightthickness=1,
                          width=1280, height=1000, bd=2, pady=0, padx=10)

        # <============================================== User Data Extraction ========================================>
        self.user_username, self.account_type = self.mastery.get_current_user()
        query = f"SELECT * from user where username='{self.user_username}'"
        user_information = self.dbconnect.select(query)
        self.user_ref = User(user_information[0][1], user_information[0][2], user_information[0][3],
                             user_information[0][4], user_information[0][5])
        self.user_ref.set_id(user_information[0][0])

        # <============================================== Overall Frame ===============================================>

        overall_frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg="#898220")
        overall_frame.place(x=10, y=10, width=1200, height=900)

        title = tk.Label(overall_frame, text="Rojgar Nepal", bd=10, relief=tk.GROOVE,
                         font=("times new roman", 40, "bold"), bg="blue", fg="white")
        title.place(x=0, y=0, width=1200)

        # <============================================== Navbar ======================================================>

        tk.Button(overall_frame, text="Profile", state=tk.DISABLED, relief=tk.SUNKEN, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=70, y=100, width=200)
        tk.Button(overall_frame, text="Jobs", relief=tk.RAISED, command=lambda: master.switch_frame('UserJob'),
                  font=("Helvetica", 20), bg='orange', fg='white',
                  bd=5).place(x=280, y=100, width=200)
        tk.Button(overall_frame, text="Logout", relief=tk.RAISED, command=self.logout, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=490, y=100, width=200)
        # <============================================== Edit your info ==============================================>

        profile_frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="#EDF0F5")
        profile_frame.place(x=10, y=190, width=600, height=650)

        entry_widget_width = 30
        entry_widget_font = ("Helvetica")
        entry_widget_ipday = 15
        label_widget_font = ("Helvetica", 20)

        profile_heading = tk.Label(profile_frame, text="Your Information", font=("Helvetica", 25, 'bold'), fg='White',
                                   bg='#eebb4d', width=20, height=2)
        profile_heading.grid(row=1, column=0, pady=(5, 5), columnspan=2)

        tk.Label(profile_frame, text="Name", font=label_widget_font).grid(row=3, column=0, pady=(0, 4))
        self.name_entry = tk.Entry(profile_frame, state='readonly', textvariable=self.user_name_entry,
                                   width=entry_widget_width, font=entry_widget_font)
        self.name_entry.grid(row=3, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(profile_frame, text="Username", font=label_widget_font).grid(row=4, column=0, pady=(0, 4))
        self.username_entry = tk.Entry(profile_frame, state='readonly', textvariable=self.user_username_entry,
                                       width=entry_widget_width, font=entry_widget_font)
        self.username_entry.grid(row=4, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(profile_frame, text="Phone Number", font=label_widget_font).grid(row=5, column=0, pady=(0, 4))
        self.phonenumber_entry = tk.Entry(profile_frame, state='readonly', textvariable=self.user_phonenumber_entry,
                                          width=entry_widget_width, font=entry_widget_font)
        self.phonenumber_entry.grid(row=5, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(profile_frame, text="Address", font=label_widget_font).grid(row=6, column=0, pady=(0, 4))
        self.address_entry = tk.Entry(profile_frame, state='readonly', textvariable=self.user_address_entry,
                                      width=entry_widget_width, font=entry_widget_font)
        self.address_entry.grid(row=6, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        self.password_label = tk.Label(profile_frame, text="Password", font=label_widget_font)
        self.password_entry = tk.Entry(profile_frame, textvariable=self.user_password_entry, show='*',
                                       width=entry_widget_width, font=entry_widget_font)

        self.confirm_password_label = tk.Label(profile_frame, text="Confirm Password", font=label_widget_font)
        self.confirm_password_entry = tk.Entry(profile_frame, textvariable=self.user_confirm_password_entry, show='*',
                                               width=entry_widget_width, font=entry_widget_font)

        self.edit_button = tk.Button(profile_frame, text="Edit", font=("Helvetica", 20), bg='green', fg='white',
                                     command=self.edit_button_clicked, bd=5).grid(row=12, column=0, pady=(10, 0))

        self.update_button = tk.Button(profile_frame, text="Update", font=("Helvetica", 20), bg='green', fg='white',
                                       command=self.update_button_clicked, bd=5)

        tk.Button(profile_frame, text="Delete this account", font=("Helvetica", 20), bg='red', fg='white',
                  command=self.delete_account, bd=5).grid(row=15, column=1, pady=(10, 0), columnspan=5)

        self.user_name_entry.set(self.user_ref.get_name())
        self.user_username_entry.set(self.user_ref.get_username())
        self.user_phonenumber_entry.set(self.user_ref.get_phone())
        self.user_address_entry.set(self.user_ref.get_address())

        # <============================================== Image Frame ===============================================>

        image_frame = tk.Frame(
            overall_frame, bd=4, relief=tk.RIDGE, bg="#EDF0F5")
        image_frame.place(x=700, y=190, width=450, height=650)

        register_heading = tk.Label(image_frame, text="What is Roger Nepal", font=(
            "Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        register_heading.grid(row=1, column=0, pady=(5, 25), columnspan=2)

        file = os.path.join(os.getcwd(), "images/job_in_hand.png")
        img = Image.open(file)
        img = img.resize((440, 640), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(image_frame, image=img)
        panel.image = img
        panel.grid(row=1, column=0)

    def logout(self):
        """
        Redirect the user to the login page.
        """
        result = messagebox.askyesno("Logout", "Are you sure you want to logout")
        if result:
            self.mastery.switch_frame('loginWindow')

    def edit_button_clicked(self):
        """
        Let the user to edit their details
        """
        entry_widget_ipday = 15
        self.password_label.grid(row=7, column=0, pady=(0, 4))
        self.confirm_password_label.grid(row=8, column=0, pady=(0, 4))
        self.password_entry.grid(row=7, column=1, pady=(0, 4), ipady=entry_widget_ipday)
        self.confirm_password_entry.grid(row=8, column=1, pady=(0, 4), ipady=entry_widget_ipday)
        self.name_entry['state'] = 'normal'
        self.username_entry['state'] = 'normal'
        self.phonenumber_entry['state'] = 'normal'
        self.address_entry['state'] = 'normal'

        self.update_button.grid(row=12, column=1, pady=(10, 0))

    def update_button_clicked(self):
        """
        Check the entry box and if all the information are valid it will update the database.
        """
        # Getting the value of each entry.
        name_current_user = self.user_name_entry.get()
        username_current_user = self.user_username_entry.get().lower()
        address_current_user = self.user_address_entry.get()
        password_current_user = self.user_password_entry.get()
        confirmation_password_current_user = self.user_confirm_password_entry.get()
        phonenumber_current_user = self.user_phonenumber_entry.get()

        # Taking the username of all user in one list.
        query = "SELECT username from user"
        all_user_username_list = self.dbconnect.select(query)
        system_username_list = []
        for users in all_user_username_list:
            for user in users:
                system_username_list.append(user)
        system_username_list.remove(self.user_ref.get_username())

        # #Checking the value before registration.

        # The value of entry cannot be empty.
        if username_current_user == '' or password_current_user == '' or name_current_user == '':
            messagebox.showerror("showerror", "Empty field")
        elif address_current_user == '' or confirmation_password_current_user == '' or phonenumber_current_user == '':
            messagebox.showerror("showerror", "Empty field")
        # Checking if the username,firstname,lastname has only alphabets only.
        # first name and last name can have space but username cannot have.
        elif not username_current_user.isalpha() or not all(x.isalpha() or x.isspace() for x in name_current_user):
            messagebox.showerror("showerror", "Name and Username can only have alphabets")

        # #Username must be unique so checking in the list of username.
        elif username_current_user in system_username_list:
            messagebox.showerror("showerror", "Username already taken")

        # The phone number must be 10 numeric digit
        elif (not len(phonenumber_current_user) == 10) or (not phonenumber_current_user.isdigit()):
            messagebox.showerror("showerror", "Phone Number should be 10 numeric digit")

        # Checking if the password and confirm password is same or not.
        elif password_current_user != confirmation_password_current_user:
            messagebox.showerror("showerror", "Your password don\'t match")

        else:
            user_ref = User(name_current_user, username_current_user, phonenumber_current_user, address_current_user,
                            password_current_user)
            query = "UPDATE user set `name`=%s,`username`=%s,`phone`=%s,`address`=%s,`password`=%s where id=%s;"
            values = (user_ref.get_name(), user_ref.get_username(), user_ref.get_phone(), user_ref.get_address(),
                      user_ref.get_password(), self.user_ref.get_id())
            self.dbconnect.insert(query, values)
            messagebox.showinfo('success', 'Your information is updated')
            self.mastery.switch_frame('UserDashboard')

    def delete_account(self):
        """
        Delete the user from the database permanently if user wants to.
        """
        result = messagebox.askyesno("Delete account", "All your data will be lost.Are you sure?")
        if result:
            query = "DELETE from user WHERE id=%s"
            values = (self.user_ref.get_id(),)
            self.dbconnect.delete(query, values)
            self.mastery.switch_frame('loginWindow')
