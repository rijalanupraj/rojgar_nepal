import tkinter as tk
from back_end.connection import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from model.job import Job


class CompanyEditJob(tk.Frame):
    def __init__(self, master):
        master.root.title('Dashboard')
        self.mastery = master
        self.dbconnect = DbConnection()
        self.company_username = str(self.mastery.get_current_user()[0])

        self.job_id_var = StringVar()
        self.job_title_var = StringVar()
        self.job_salary_var = StringVar()
        self.job_qualification_var = StringVar()

        # Initializing a frame.
        tk.Frame.__init__(self, master.root, highlightbackground="#f3ecc2", highlightcolor="#f3ecc2",
                          highlightthickness=1,
                          width=1280, height=1000, bd=2, pady=0, padx=10)

        # <============================================== Overall Frame ===============================================>

        overall_frame = tk.Frame(self, bd=4, relief=tk.RIDGE, bg="#898220")
        overall_frame.place(x=10, y=10, width=1200, height=900)

        title = tk.Label(overall_frame, text="Rojgar Nepal", bd=10, relief=tk.GROOVE,
                         font=("times new roman", 40, "bold"), bg="blue", fg="white")
        title.place(x=0, y=0, width=1200)
        edit_heading = tk.Label(overall_frame, text="Make changes to the existing jobs.",
                                     font=("Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        edit_heading.place(x=10, y=190, width=700)
        # <============================================== Navbar ======================================================>

        tk.Button(overall_frame, text="Profile", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyDashboard'), font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=70, y=100, width=200)
        tk.Button(overall_frame, text="Add Jobs", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyAddJob'), font=("Helvetica", 20), bg='orange', fg='white',
                  bd=5).place(x=280, y=100, width=200)
        tk.Button(overall_frame, text="Edit Jobs", state=tk.DISABLED, relief=tk.SUNKEN, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=490, y=100, width=200)
        tk.Button(overall_frame, text="Applicants", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyApplicants'), font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=700, y=100, width=200)
        tk.Button(overall_frame, text="Logout", relief=tk.RAISED, command=self.logout, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=910, y=100, width=200)

        # <==================Table Frame===============================================================================>

        Table_Frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="pink")
        Table_Frame.place(x=10, y=300, width=700, height=500)

        scroll_x = tk.Scrollbar(Table_Frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(Table_Frame, orient=tk.VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame, columns=("id", "title", "des", "salary", "qual"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.Job_table.xview)
        scroll_y.config(command=self.Job_table.yview)
        self.Job_table.heading("id", text="Job Id")
        self.Job_table.heading("title", text="Job Title")
        self.Job_table.heading("des", text="Description")
        self.Job_table.heading("salary", text="Salary")
        self.Job_table.heading("qual", text="Min. Qualification")
        self.Job_table['show'] = 'headings'
        self.Job_table.column("id", width=30)
        self.Job_table.column("title", width=100)
        self.Job_table.column("des", width=150)
        self.Job_table.column("salary", width=70)
        self.Job_table.column("qual", width=130)
        self.Job_table.pack(fill=tk.BOTH, expand=1)
        self.Job_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # <==================Edit Frame================================================================================>

        Edit_Frame = tk.Frame(overall_frame, bd=4, relief=RIDGE, bg="pink")
        Edit_Frame.place(x=720, y=200, width=450, height=600)

        m_title = tk.Label(Edit_Frame, text="Edit Job", bg="pink", fg="blue", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_id = tk.Label(Edit_Frame, text="Job Id", bg="pink", fg="blue", font=("times new roman", 15, "bold"))
        lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_id = tk.Entry(Edit_Frame, state='readonly', textvariable=self.job_id_var,
                          font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_title = tk.Label(Edit_Frame, text="Job Title", bg="pink", fg="blue", font=("times new roman", 15, "bold"))
        lbl_title.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_title = tk.Entry(Edit_Frame, textvariable=self.job_title_var, font=("times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
        txt_title.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_description = tk.Label(Edit_Frame, text="Description", bg="pink", fg="blue",
                                   font=("times new roman", 15, "bold"))
        lbl_description.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.text_description = Text(Edit_Frame, width=30, height=4, font=("", 10))
        self.text_description.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_salary = Label(Edit_Frame, text="Salary", bg="pink", fg="blue", font=("times new roman", 15, "bold"))
        lbl_salary.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_salary = Entry(Edit_Frame, textvariable=self.job_salary_var, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        txt_salary.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_job_qualification = Label(Edit_Frame, text="Qualification", bg="pink", fg="blue",
                                      font=("times new roman", 15, "bold"))
        lbl_job_qualification.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_job_qualification = Entry(Edit_Frame, textvariable=self.job_qualification_var,
                                      font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_job_qualification.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        tk.Button(Edit_Frame, text="Save Job", font=("Helvetica", 20), bg='green', fg='white',
                  command=self.save_edit_job, bd=5).grid(row=7, column=1, pady=10, padx=20, sticky="w", columnspan=2)
        tk.Button(Edit_Frame, text="Delete Job", font=("Helvetica", 20), bg='red', fg='white',
                  command=self.delete_job, bd=5).grid(row=8, column=1, pady=10, padx=20, sticky="w", columnspan=2)

    def logout(self):
        """
        Redirect the user to the login page.
        """
        result = messagebox.askyesno("Logout", "Are you sure you want to logout")
        if result:
            self.mastery.switch_frame('loginWindow')

    def fetch_data(self):
        """
        Fetch the existing job of the company from the database
        """

        query = f"SELECT id from company WHERE username='{self.company_username}'"
        company_id = self.dbconnect.select(query)[0][0]
        query = f"SELECT id,title,description,salary,minQualification FROM job WHERE companyId='{company_id}'"
        all_company_job = self.dbconnect.select(query)
        if len(all_company_job) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for data in all_company_job:
                self.Job_table.insert('', tk.END, values=data)

    def get_cursor(self, ev):
        cursor_row = self.Job_table.focus()
        contents = self.Job_table.item(cursor_row)
        row = contents['values']
        self.job_id_var.set(row[0])
        self.job_title_var.set(row[1])
        self.text_description.delete("1.0", END)
        self.text_description.insert(END, row[2])
        self.job_salary_var.set(row[3])
        self.job_qualification_var.set(row[4])

    def save_edit_job(self):
        """
        Updates the existing job in the system.
        """
        id = self.job_id_var.get()
        title = self.job_title_var.get()
        description = self.text_description.get('1.0', END)
        salary = self.job_salary_var.get()
        qualification = self.job_qualification_var.get()
        if id == '' or title == '' or self.text_description.compare("end-1c", "==",
                                                                    "1.0") or salary == '' or qualification == '':
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
            job_ref = Job(title, description, salary, qualification, '')
            job_ref.set_id(id)
            query = 'UPDATE job set `title`=%s,`description`=%s,`salary`=%s,`minQualification`=%s WHERE id=%s;'
            values = (
                job_ref.get_title(), job_ref.get_description(), job_ref.get_salary(), job_ref.get_min_qualification(),
                int(job_ref.get_id()))
            result = messagebox.askyesno("Edit Job", "You will edit this job.Are you sure you want to continue")
            if result:
                self.dbconnect.update(query, values)
                self.mastery.switch_frame('CompanyEditJob')

    def delete_job(self):
        """
        Deletes the job from the system.
        """
        id = self.job_id_var.get()
        if id == '':
            messagebox.showerror("Empty Job Id Field", "Select the job which you want to delete")
        else:
            query = 'DELETE from job WHERE id=%s;'
            values = (self.job_id_var.get(),)
            result = messagebox.askyesno("Delete Job",
                                         "You are going to delete this job.Are you sure you want to continue")
            if result:
                self.dbconnect.delete(query, values)
                self.mastery.switch_frame('CompanyEditJob')
