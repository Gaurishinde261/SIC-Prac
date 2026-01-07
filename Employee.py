#name =1234567

class Employee:
    def __init__(self, eid, ename, salary):
        self.eid = eid
        self.ename = ename
        self.salary = salary

    def __str__(self):
        return f"Name: {self.ename}\nID: {self.eid}\nSalary: {self.salary}"


