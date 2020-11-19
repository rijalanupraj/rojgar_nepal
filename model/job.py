class Job:
    def __init__(self, title, description, salary, min_qualification, company_id):
        self.id = ''
        self.title = title
        self.description = description
        self.salary = salary
        self.min_qualification = min_qualification
        self.company_id = company_id

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_min_qualification(self, min_qualification):
        self.min_qualification = min_qualification

    def get_min_qualification(self):
        return self.min_qualification

    def set_company_id(self, company_id):
        self.company_id = company_id

    def get_company_id(self):
        return self.company_id
