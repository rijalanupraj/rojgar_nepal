import tkinter as tk
from tkinter import ttk
from back_end.connection import *
from tkinter import messagebox

class CompanyApplicants(tk.Frame):
    def __init__(self, master):
        master.root.title('Dashboard')
        self.mastery = master
        self.dbconnect = DbConnection()
        self.company_username = str(self.mastery.get_current_user()[0])

        self.sort_by = tk.StringVar()
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

        applicant_heading = tk.Label(overall_frame, text="People who have applied for your job",
                                     font=("Helvetica", 25, 'bold'), fg='White', bg='#eebb4d', width=20, height=2)
        applicant_heading.place(x=10, y=190, width=700)
        # <============================================== Navbar ======================================================>

        tk.Button(overall_frame, text="Profile", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyDashboard'), font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=70, y=100, width=200)
        tk.Button(overall_frame, text="Add Jobs", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyAddJob'), font=("Helvetica", 20), bg='orange', fg='white',
                  bd=5).place(x=280, y=100, width=200)
        tk.Button(overall_frame, text="Edit Jobs", relief=tk.RAISED,
                  command=lambda: master.switch_frame('CompanyEditJob'), font=("Helvetica", 20), bg='orange',
                  fg='white',
                  bd=5).place(x=490, y=100, width=200)
        tk.Button(overall_frame, text="Applicants", relief=tk.SUNKEN, state=tk.DISABLED, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=700, y=100, width=200)
        tk.Button(overall_frame, text="Logout", relief=tk.RAISED, command=self.logout, font=("Helvetica", 20),
                  bg='orange', fg='white',
                  bd=5).place(x=910, y=100, width=200)

        # <============================================== Sort Frame ==================================================>

        Sort_Frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="pink")
        Sort_Frame.place(x=10, y=300, width=1150, height=60)

        lbl_sort = tk.Label(Sort_Frame, text="Sort Applicants Name By ", bg="pink", fg="Blue", font=("times new roman", 15, "bold"))
        lbl_sort.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Sort_Frame, textvariable=self.sort_by, font=("times new roman", 12, "bold"),
                                    state="readonly")
        combo_search['values'] = ("Ascending Order", "Descending Order")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        sortbtn = tk.Button(Sort_Frame, text="Sort Now", width=15, command=self.sort_by_name, bg='green', fg='white')
        sortbtn.grid(row=0, column=6, padx=10, pady=5, sticky="W")

        # <============================================== Table Frame =================================================>

        Table_Frame = tk.Frame(overall_frame, bd=4, relief=tk.RIDGE, bg="pink")
        Table_Frame.place(x=10, y=400, width=1150, height=400)

        scroll_x = tk.Scrollbar(Table_Frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(Table_Frame, orient=tk.VERTICAL)
        self.Job_table = ttk.Treeview(Table_Frame,
                                      columns=("userid", "username", "phone", "address", "jobid", 'jobtitle'),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.config(command=self.Job_table.xview)
        scroll_y.config(command=self.Job_table.yview)
        self.Job_table.heading("userid", text="User's Id")
        self.Job_table.heading("username", text="User's Name")
        self.Job_table.heading("phone", text="User's Phone")
        self.Job_table.heading("address", text="User's Address")
        self.Job_table.heading("jobid", text="Applied Job ID")
        self.Job_table.heading("jobtitle", text="Applied Job Title")
        self.Job_table['show'] = 'headings'
        self.Job_table.column("userid", width=30)
        self.Job_table.column("username", width=70)
        self.Job_table.column("phone", width=70)
        self.Job_table.column("address", width=100)
        self.Job_table.column("jobid", width=30)
        self.Job_table.column("jobtitle", width=100)
        self.Job_table.pack(fill=tk.BOTH, expand=1)
        self.fetch_data()

    def logout(self):
        """
        Redirect the user to the login page.
        """
        result = messagebox.askyesno("Logout", "Are you sure you want to logout")
        if result:
            self.mastery.switch_frame('loginWindow')

    def fetch_data(self):
        """
        All the people who have applied for the company is fetched from the database.
        """
        query = f"SELECT id from company WHERE username='{self.company_username}'"
        company_id = self.dbconnect.select(query)[0][0]
        query = f"SELECT u.id,u.name,u.phone,u.address,j.id,j.title FROM job_application as a INNER JOIN job as j on " \
                f"j.id=a.jobId INNER JOIN user as u on a.userId=u.id WHERE j.companyId='{company_id}' "
        applied_jobs = self.dbconnect.select(query)
        if len(applied_jobs) != 0:
            self.Job_table.delete(*self.Job_table.get_children())
            for data in applied_jobs:
                self.Job_table.insert('', tk.END, values=data)

    def sort_by_name(self):
        """
        Sorting the the applicants name by either ascending order or descending order.
        """
        if self.sort_by.get() == '':
            messagebox.showerror("Empty Field", "Select Sort By")
        else:
            query = f"SELECT id from company WHERE username='{self.company_username}'"
            company_id = self.dbconnect.select(query)[0][0]
            query = f"SELECT u.id,u.name,u.phone,u.address,j.id,j.title FROM job_application as a INNER JOIN job as j " \
                    f"on j.id=a.jobId INNER JOIN user as u on a.userId=u.id WHERE j.companyId='{company_id}' "
            applied_jobs = self.dbconnect.select(query)
            jobs = []
            for j in applied_jobs:
                a = list(j)
                jobs.append(a)
            sorted_jobs = CompanyApplicants.selection_sort(jobs)
            if self.sort_by.get() == 'Descending Order':
                sorted_jobs = sorted_jobs[::-1]
            if len(sorted_jobs) != 0:
                self.Job_table.delete(*self.Job_table.get_children())
                for data in sorted_jobs:
                    self.Job_table.insert('', tk.END, values=data)

    @classmethod
    def selection_sort(cls, all_jobs):
        """ This sorting algorithm sort the applicant users by their name """
        for i in range(len(all_jobs)):

            min_index = i
            for j in range(i + 1, len(all_jobs)):
                if all_jobs[min_index][1] > all_jobs[j][1]:
                    min_index = j

            # Swap the found minimum element with
            # the first element         
            all_jobs[i], all_jobs[min_index] = all_jobs[min_index], all_jobs[i]

        return all_jobs
