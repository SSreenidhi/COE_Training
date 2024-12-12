def calculate_gross_salary(basic_salary):
    if basic_salary < 10000:
        hra = 0.67 * basic_salary
        da = 0.73 * basic_salary
    elif 10000 <= basic_salary <= 20000:
        hra = 0.69 * basic_salary
        da = 0.76 * basic_salary
    else:
        hra = 0.73 * basic_salary
        da = 0.89 * basic_salary

    gross_salary = hra + da + basic_salary
    return gross_salary

basic_salary = float(input("Enter basic salary: "))
gross_salary = calculate_gross_salary(basic_salary)
print("Gross Salary: ", gross_salary)
















