from employee import Employee
from office import Office

e1 = Employee(1, "Hossam", 1000, "Happy", 80)
e2 = Employee(2, "Ali", 800, "Fine", 90)

office = Office("Tech Office")
office.hire(e1)
office.hire(e2)

print("All employees:", [emp.name for emp in office.get_all_employees()])

office.deduct(1, 50)
office.reward(2, 100)

office.check_lateness(1, moveHour=8, distance=20, velocity=40)

office.fire(2)
print("Total employees:", Office.no_of_employees)
Office.change_emp_num(10)
