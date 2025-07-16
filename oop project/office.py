from employee import Employee

class Office:
    no_of_employees=0
    def __init__(self,name):
        self.name=name
        self.employees:list[Employee]=[]

    def hire(self,employee:Employee):
        self.employees.append(employee)
        Office.no_of_employees+=1
        print(f'{employee.name} has been hired in {self.name}')

    def get_all_employees(self):
        return self.employees
    

    def get_employee_with_id(self,id):
        for emp in self.employees:
            if emp.id==id:
                return emp
            else:
                print('Not Found')

    def fire(self,id):
        emp = self.get_employee_with_id(id)
        if emp:
            self.employees.remove(emp)
            Office.no_of_employees-=1
            print(f'{emp.name} has been fired')
        else:
            print('Not Found')

    
    def deduct(self,id,deduction):
        emp=self.get_employee_with_id(id)
        emp.money-=deduction
        print(f"{emp.name} deducted {deduction}. New balance: {emp.money}")

    def reward(self, emp_id, reward):
        emp = self.get_employee_with_id(emp_id)
        emp.money += reward
        print(f"{emp.name} rewarded {reward}. New balance: {emp.money}")


    def check_lateness(self, id, moveHour, distance, velocity):
        is_late = Office.calculate_lateness(9,moveHour,distance,velocity)
        emp=self.get_employee_with_id(id)
        if is_late:
            emp.money-=10
            print(f"{emp.name} is late. Deducted 10. New balance: {emp.money}")
        else:
            emp.money+=10
            print(f"{emp.name} is on time. Rewarded 10. New balance: {emp.money}")
    
        

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrival_time=moveHour + (distance/velocity)
        return arrival_time > targetHour   
    

    @classmethod
    def change_emp_num(cls,num):
        cls.no_of_employees=num
        print(f"Employees number changed to {num}")