import tkinter as tk
from tkinter import ttk
from back_end.connection import *
from tkinter import messagebox
from model.job_application import JobApplication


class UserJob(tk.Frame):
    def __init__(self, master):
        master.root.title('User Dashboard')
        self.mastery = master

        self.user_username = str(self.mastery.get_current_user()[0])

        self.job_id_var = tk.StringVar()
        self.job_title_var = tk.StringVar()
        self.job_salary_var = tk.StringVar()
        self.job_qualification_var = tk.StringVar()
        self.job_company_name_var = tk.StringVar()
        self.search_by = tk.StringVar()
        self.search_text = tk.StringVar()

        self.dbconnect = DbConnection()
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

        # <============================================== Navbar =====================================================>

        tk.Button(overall_frame, text="Profile", command=lambda: master.switch_frame('UserDashboard'), relief=tk.RAISED,
                  font=("Helvetica", 20), bg='orange', fg='white',
                  bd=5).place(x=70, y=100, width=200)
        tk.Button(overall_frame, text="Jobs", state=tk.DISABLED, relief=tk.SUNKEN, font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=280, y=100, width=200)
        tk.Button(overall_frame, text="Logout", relief=tk.RAISED, command=self.logout, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=490, y=100, width=200)

        # <============================================== Detail Frame ================================================>

        Detail_Frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="pink")
        Detail_Frame.place(x=10, y=200, width=1150, height=60)

        lbl_search = tk.Label(Detail_Frame, text="Search By", bg="pink", fg="Blue",
                              font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("times new roman", 12, "bold"),
                                    state="readonly")
        combo_search['values'] = ("Job Title", "Company Name")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_Search = tk.Entry(Detail_Frame, textvariable=self.search_text, width=50,
                              font=("times new roman", 10, "bold"), bd=5, relief=tk.GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = tk.Button(Detail_Frame, text="Search", width=15, command=self.search)
        searchbtn.grid(row=0, column=4, padx=10, pady=5, sticky="W")

        showallbtn = tk.Button(Detail_Frame, text="Clear Search", width=15, command=self.fetch_data)
        showallbtn.grid(row=0, column=6, padx=10, pady=5, sticky="W")
        # <============================================== Table Frame =================================================>

        Table_Frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="pink")
        Table_Frame.place(x=10, y=300, width=700, height=550)

        scroll_x = tk.Scrollbar(Table_Frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(Table_Frame, orient=tk.VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame, columns=("id", "title", "des", "salary", "qual", "company"),
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
        self.Job_table.heading("company", text="Company Name")
        self.Job_table['show'] = 'headings'
        self.Job_table.column("id", width=30)
        self.Job_table.column("title", width=100)
        self.Job_table.column("des", width=150)
        self.Job_table.column("salary", width=70)
        self.Job_table.column("qual", width=130)
        self.Job_table.column("company", width=130)

        self.Job_table.pack(fill=tk.BOTH, expand=1)
        self.Job_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # <============================================== Apply Frame =================================================>

        Apply_Frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="pink")
        Apply_Frame.place(x=720, y=300, width=450, height=550)

        m_title = tk.Label(Apply_Frame, text="Apply Job", bg="pink", fg="blue", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_id = tk.Label(Apply_Frame, text="Job Id", bg="pink", fg="blue", font=("times new roman", 15, "bold"))
        lbl_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_id = tk.Entry(Apply_Frame, state='readonly', textvariable=self.job_id_var,
                          font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_id.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_title = tk.Label(Apply_Frame, text="Job Title", bg="pink", fg="blue", font=("times new roman", 15, "bold"))
        lbl_title.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_title = tk.Entry(Apply_Frame, state='readonly', textvariable=self.job_title_var,
                             font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_title.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_description = tk.Label(Apply_Frame, text="Description", bg="pink", fg="blue",
                                   font=("times new roman", 15, "bold"))
        lbl_description.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.text_description = tk.Text(Apply_Frame, state='disabled', width=30, height=4, font=("", 10))
        self.text_description.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_salary = tk.Label(Apply_Frame, text="Salary", bg="pink", fg="blue", font=("times new roman", 15, "bold"))
        lbl_salary.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_salary = tk.Entry(Apply_Frame, state='readonly', textvariable=self.job_salary_var,
                              font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_salary.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_job_qualification = tk.Label(Apply_Frame, text="Qualification", bg="pink", fg="blue",
                                         font=("times new roman", 15, "bold"))
        lbl_job_qualification.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_job_qualification = tk.Entry(Apply_Frame, state='readonly', textvariable=self.job_qualification_var,
                                         font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_job_qualification.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_company = tk.Label(Apply_Frame, text="Company Name", bg="pink", fg="blue",
                               font=("times new roman", 15, "bold"))
        lbl_company.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_company = tk.Entry(Apply_Frame, state='readonly', textvariable=self.job_company_name_var,
                               font=("times new roman", 15, "bold"), bd=5, relief=tk.GROOVE)
        txt_company.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        tk.Button(Apply_Frame, text="Apply this Job", font=("Helvetica", 20), bg='green', fg='white',
                  command=self.apply_job, bd=5).grid(row=8
                                                     , column=1, pady=10, padx=20, sticky="w", columnspan=2)

    def fetch_data(self):
        """
        Fetch all the job from the database provide user in tree view.
        """
        query = f"SELECT j.id,j.title,j.description,j.salary,j.minQualification,c.name FROM job AS j INNER JOIN " \
                f"company AS c ON j.companyId= c.id "
        self.all_jobs = self.dbconnect.select(query)
        if len(self.all_jobs) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for data in self.all_jobs:
                self.Job_table.insert('', tk.END, values=data)
        self.search_by.set('')
        self.search_text.set('')

    def get_cursor(self, ev):
        """
        Get the information of the cursor of the user in the table.
        And allow user to apply for the job in next tab.
        """
        cursor_row = self.Job_table.focus()
        contents = self.Job_table.item(cursor_row)
        row = contents['values']
        self.text_description.configure(state='normal')
        self.job_id_var.set(row[0])
        self.job_title_var.set(row[1])
        self.text_description.delete("1.0", tk.END)
        self.text_description.insert(tk.END, row[2])
        self.job_salary_var.set(row[3])
        self.job_qualification_var.set(row[4])
        self.job_company_name_var.set(row[5])
        self.text_description.configure(state='disabled')

    def logout(self):
        """
        Allows user to return to login page.
        """
        result = messagebox.askyesno("Logout", "Are you sure you want to logout")
        if result:
            self.mastery.switch_frame('loginWindow')

    def apply_job(self):
        """
        User apply for a certain job and the information is stored in database.
        """
        if self.job_id_var.get() == '':
            messagebox.showerror("showerror", "First Select a job from the table")
        else:
            query = f"SELECT id from user WHERE username='{self.user_username}'"
            user_id = self.dbconnect.select(query)[0][0]
            query = "SELECT jobId,userId from job_application"
            previous_jobs = self.dbconnect.select(query)
            job_application_ref = JobApplication(int(self.job_id_var.get()), int(user_id))
            applied = False
            for job in previous_jobs:
                if job[0] == job_application_ref.get_job_id() and job[1] == job_application_ref.get_user_id():
                    applied = True
                    break
            if applied:
                messagebox.showinfo('success', 'You have already applied for this job.Have some patience')
                result = False
            else:
                result = messagebox.askyesno("Apply", "Are you sure you want to apply for this job")
            if result:
                query = "SELECT jobId,userId from job_application"
                previous_jobs = self.dbconnect.select(query)
                job_application_ref = JobApplication(int(self.job_id_var.get()), int(user_id))
                query = 'INSERT INTO job_application (`jobId`, `userId`) VALUES (%s,%s);'
                values = (job_application_ref.get_job_id(), job_application_ref.get_user_id())
                self.dbconnect.insert(query, values)
                messagebox.showinfo('success', 'You application has been submitted. You will be notified soon')
                self.mastery.switch_frame('UserJob')

    def search(self):
        """
        User can search job from the database.
        """
        if self.search_by.get() == '' or self.search_text.get() == '':
            messagebox.showerror('Error', 'You cannot leave search field empty')
            return None
        query = "SELECT j.id,j.title,j.description,j.salary,j.minQualification,c.name FROM job AS j INNER JOIN " \
                "company AS c ON j.companyId= c.id "
        all_jobs = self.dbconnect.select(query)
        search_by = self.search_by.get()
        search_data = UserJob.searching_algo(all_jobs, search_by, self.search_text.get())
        if len(search_data) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for data in search_data:
                self.Job_table.insert('', tk.END, values=data)
        else:
            messagebox.showerror('Error', 'Not data found.')

    @classmethod
    def searching_algo(cls, data, search_by, search_text):
        """
        Searching algorithm is used to search the job.
        Data is 2d list.
        search_text is the text entered by user to search.
        """
        if search_by == 'Job Title':
            index = 1
        elif search_by == 'Company Name':
            index = 5
        search_data = []
        for job in data:
            if job[index].lower() == search_text.lower():
                search_data.append(job)
        return search_data
