def bonus_time(salary, bonus):
    dolar = "$"
    salary_bonus = salary * 10
    salary_dolar = str(salary_bonus)
    salary_good = dolar + salary_dolar
    normal_salary = str(salary)
    dolar_salary = dolar + normal_salary 
    if bonus == True: 
        return salary_good
    elif bonus ==  False:
        return dolar_salary

