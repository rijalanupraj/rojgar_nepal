class JobApplication:
    def __init__(self, job_id, user_id):
        self.id = ''
        self.job_id = job_id
        self.user_id = user_id

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_job_id(self, job_id):
        self.job_id = job_id

    def get_job_id(self):
        return self.job_id
