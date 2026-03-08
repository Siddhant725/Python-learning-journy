def get_payroll_total(employee_list):
    total = 0
    for employee in employee_list:
        pay = calculate_pay(employee)
        print(f"{employee['name']} earned ${pay}")
        total += pay
    return total

def calculate_pay(employee):
    payment = employee['hours_worked'] * employee['hourly_rate']
    return payment

employees = [
    {'name': 'Alice', 'hours_worked': 40, 'hourly_rate': 15},
    {'name': 'Bob', 'hours_worked': 35, 'hourly_rate': 20},
    {'name': 'Charlie', 'hours_worked': 30, 'hourly_rate': 25}
]

total_payroll = get_payroll_total(employees)
print(f'Total payroll: ${total_payroll}')