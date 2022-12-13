class Subscriber():
    def __init__(self,email, name, DOB, gender):
        self.email = email
        self.name = name
        self.DOB = DOB
        self.gender = gender

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.DOB

    def get_gender(self):
        return self.gender