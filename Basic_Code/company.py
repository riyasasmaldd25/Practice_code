from employee import Employee, SalaryEmployee, HoulyEmployee, contractEmployee, ComissionEmployee

class company:
    def __init__(self):
        self.employees = []

    def add_employee(self,new_employee):
        self.employees.append(new_employee)

    def display_input(self):
        print('current Employee:\n')
        for i in self.employees:
            print (i.fname,i.lname)
        print('-------------------------------')

    def pay_employees(self):
        print('Paying Employees\n')
        
        for i in self.employees:
            print('Paycheck for: ',i.fname,i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')


def main():
    my_company = company()

    employee1 = SalaryEmployee('riya','sass',50000)
    employee2 = HoulyEmployee('sam','kans',30,90)
    employee3 = contractEmployee('bob','kans',7, 900)
    employee4 = ComissionEmployee('ram','pari', 3000, 5 ,200)
    
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)
    my_company.add_employee(employee4)

    my_company.display_input()
    my_company.pay_employees()

main()