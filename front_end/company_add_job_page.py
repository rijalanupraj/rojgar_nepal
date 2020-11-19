import tkinter as tk
from back_end.connection import *
from model.company import Company
from tkinter import *
from tkinter import messagebox
from model.job import Job
from PIL import ImageTk, Image
import os


class CompanyAddJob(tk.Frame):
    def __init__(self, master):
        master.root.title('Dashboard')
        self.mastery = master
        self.dbconnect = DbConnection()
        self.company_username = str(self.mastery.get_current_user()[0])

        # Initializing a frame.
        tk.Frame.__init__(self, master.root, highlightbackground="#f3ecc2", highlightcolor="#f3ecc2",
                          highlightthickness=1,
                          width=1280, height=1000, bd=2, pady=0, padx=10)

        # <============================================== Company Data Extraction =====================================>
        self.user_username, self.account_type = self.mastery.get_current_user()
        query = f"SELECT * from company where username='{self.user_username}'"
        company_information = self.dbconnect.select(query)
        self.company_ref = Company(company_information[0][1], company_information[0][2], company_information[0][3],
                                   company_information[0][4], company_information[0][5])
        self.company_ref.set_id(company_information[0][0])

        # <============================================== Overall Frame ===============================================>

        overall_frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg="#898220")
        overall_frame.place(x=10, y=10, width=1200, height=900)

        title = tk.Label(overall_frame, text="Rojgar Nepal", bd=10, relief=tk.GROOVE,
                         font=("times new roman", 40, "bold"), bg="blue", fg="white")
        title.place(x=0, y=0, width=1200)

        # <============================================== Navbar ======================================================>

        tk.Button(overall_frame, text="Profile", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyDashboard'), font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=70, y=100, width=200)
        tk.Button(overall_frame, text="Add Jobs", state=tk.DISABLED, relief=tk.SUNKEN, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=280, y=100, width=200)
        tk.Button(overall_frame, text="Edit Jobs", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyEditJob'), font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=490, y=100, width=200)
        tk.Button(overall_frame, text="Applicants", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyApplicants'), font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=700, y=100, width=200)
        tk.Button(overall_frame, text="Logout", relief=tk.RAISED, command=self.logout,
                  font=("Helvetica", 20), bg='orange', fg='white',
                  bd=5).place(x=910, y=100, width=200)

        # <============================================== Content =====================================================>

        content_frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="#EDF0F5")
        content_frame.place(x=10, y=190, width=600, height=650)

        content_heading = tk.Label(content_frame, text="Add New Job", font=("Helvetica", 25, 'bold'), fg='White',
                                   bg='#eebb4d', width=20, height=2)
        content_heading.grid(row=1, column=0, pady=(5, 5), columnspan=2)

        entry_widget_width = 30
        entry_widget_font = ("Helvetica")
        entry_widget_ipday = 15
        label_widget_font = ("Helvetica", 20)

        tk.Label(content_frame, text="Job Title", font=label_widget_font).grid(row=3, column=0, pady=(0, 4))
        self.title_entry = tk.Entry(content_frame, width=entry_widget_width, font=entry_widget_font)
        self.title_entry.grid(row=3, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(content_frame, text="Job Description", font=label_widget_font).grid(row=4, column=0, pady=(0, 4))
        self.description_entry = tk.Entry(content_frame, width=entry_widget_width, font=entry_widget_font)
        self.description_entry.grid(row=4, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(content_frame, text="Salary (in Rs)", font=label_widget_font).grid(row=5, column=0, pady=(0, 4))
        self.salary_entry = tk.Entry(content_frame, width=entry_widget_width, font=entry_widget_font)
        self.salary_entry.grid(row=5, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Label(content_frame, text="Min Qualification", font=label_widget_font).grid(row=6, column=0, pady=(0, 4))
        self.qualification_entry = tk.Entry(content_frame, width=entry_widget_width, font=entry_widget_font)
        self.qualification_entry.grid(row=6, column=1, pady=(0, 4), ipady=entry_widget_ipday)

        tk.Button(content_frame, text="Add Job", font=("Helvetica", 20), bg='green', fg='white',
                  command=self.add_job, bd=5).grid(row=15, column=1, pady=(10, 0), columnspan=3)

        # <============================================== Image Frame ===============================================>

        image_frame = tk.Frame(
            overall_frame, bd=4, relief=tk.RIDGE, bg="#EDF0F5")
        image_frame.place(x=700, y=190, width=450, height=650)

        register_heading = tk.Label(image_frame, text="What is Roger Nepal", font=(
            "Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        register_heading.grid(row=1, column=0, pady=(5, 25), columnspan=2)

        file = os.path.join(os.getcwd(), "images/company_hire.png")
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

    def add_job(self):
        """
        Company adds new job to the system.
        """
        title = self.title_entry.get()
        description = self.description_entry.get()
        salary = self.salary_entry.get()
        qualification = self.qualification_entry.get()

        if title == '' or description == '' or salary == '' or qualification == '':
            messagebox.showerror("showerror", "Empty field")
        elif not salary.isdigit():
            messagebox.showerror("showerror", "Salary should be in number")
        elif len(title) > 150:
            messagebox.showerror("showerror", "Only 150 character allowed in title")
        elif len(description) > 250:
            messagebox.showerror("showerror", "Only 250 characters allowed in description")
        elif len(salary) > 9:
            messagebox.showerror("showerror", "Only upto 9 digits allowed")
        elif len(qualification) > 250:
            messagebox.showerror("showerror", "Only 250 characters allowed in qualification")
        else:
            query = f"SELECT id from company WHERE username='{self.company_username}'"
            company_id = self.dbconnect.select(query)[0][0]
            job_ref = Job(title, description, salary, qualification, company_id)
            query = 'INSERT INTO job (`title`, `description`, `salary`,`minQualification`,`companyId`) VALUES (%s,%s,' \
                    '%s,%s,%s); '
            values = (
                job_ref.get_title(), job_ref.get_description(), job_ref.get_salary(), job_ref.get_min_qualification(),
                int(job_ref.get_company_id()))
            self.dbconnect.insert(query, values)
            messagebox.showinfo('success', 'Job Added')
            self.mastery.switch_frame('CompanyEditJob')
