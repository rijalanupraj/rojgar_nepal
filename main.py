from tkinter import *
from front_end.login_page import loginWindow
from front_end.register_page import RegisterWindow
from front_end.user_dashboard import UserDashboard
from front_end.user_job_page import UserJob
from front_end.company_dashboard import CompanyDashboard
from front_end.company_add_job_page import CompanyAddJob
from front_end.company_edit_job_page import CompanyEditJob
from front_end.company_applicants_page import CompanyApplicants

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Rojgar Nepal")

        self.root.geometry("1500x900+50+50")
        self.root._frame = None
        self.switch_frame('loginWindow')
        self.root.configure(background='#54596d')

        # Making menu bar in the program as to close or to navigate to other window.
        menubar = Menu()

        # pulldown menu created and added to the menu bar
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=self.filemenu)

        # more pulldown menu
        openmenu = Menu(menubar, tearoff=0)
        openmenu.add_command(label="Login", command=lambda: self.switch_frame('loginWindow'))
        openmenu.add_command(label="Register", command=lambda: self.switch_frame('RegisterWindow'))
        menubar.add_cascade(label="Open", menu=openmenu)

        # Assigning in the menubar in the menu.Doing this will make menu appear.
        self.root.config(menu=menubar)

    def switch_frame(self, type=''):
        """
        This function switches the frame.
        """
        if type == '':
            frame_class = loginWindow
        elif type == 'RegisterWindow':
            frame_class = RegisterWindow
        elif type == 'loginWindow':
            frame_class = loginWindow
        elif type == 'UserDashboard':
            frame_class = UserDashboard
        elif type == 'UserJob':
            frame_class = UserJob
        elif type == 'CompanyDashboard':
            frame_class = CompanyDashboard
        elif type == 'CompanyAddJob':
            frame_class = CompanyAddJob
        elif type == 'CompanyEditJob':
            frame_class = CompanyEditJob
        elif type == 'CompanyApplicants':
            frame_class = CompanyApplicants

        new_frame = frame_class(self)
        # It will check for frame, if frame already exist it will delete it & display another frame.
        if self.root._frame is not None:
            self.root._frame.destroy()
        self.root._frame = new_frame
        self.root._frame.pack()

    def assign_current_user(self, username, type):
        """
        This function assign username and type in the global variables after the user logs in.
        It can be used to identify the user in further processes.
        """
        global USERNAME
        global TYPE
        USERNAME = username
        TYPE = type

    def get_current_user(self):
        """
        This function return username and type of the current user.
        """
        return USERNAME, TYPE


if __name__ == "__main__":
    root = Tk()
    obs = Main(root)
    root.mainloop()
