stock = [('APPL', 200),('GOOG',400),('MSFT', 100)]

for items in stock:
    print(items)

for ticker, price in stock:
    print(f"Ticker: {ticker} and Price: {price}")

#practice

work_hours = [('Abby', 100),('Billy', 400),('Cassie',800)]

#who has the most hours

def employee_check(work):
    max_hours = 0
    employee_of_month = ''

    for name, hours in work:
        if hours > max_hours:
            max_hours = hours
            employee_of_month = name
        else:
            pass
    
    return (employee_of_month, hours)


employee,hours = employee_check(work_hours)
print(f"{employee} is the employee of the month with {hours} hours!")

print(type(hours))