import threading
import time

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

SSS_RATE = 0.045
PHILHEALTH_RATE = 0.025
PAGIBIG_RATE = 0.02
TAX_RATE = 0.10

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

## Deduction and Payroll Functions
def compute_sss(salary):
    print(f"SSS computed by {threading.current_thread().name}")
    return salary * SSS_RATE

def compute_philhealth(salary):
    print(f"PhilHealth computed by {threading.current_thread().name}")
    return salary * PHILHEALTH_RATE

def compute_pagibig(salary):
    print(f"PagIBIG computed by {threading.current_thread().name}")
    return salary * PAGIBIG_RATE

def compute_tax(salary):
    print(f"Tax computed by {threading.current_thread().name}")
    return salary * TAX_RATE
    
def compute_payroll(employee):
    name, salary = employee

    sss = salary * SSS_RATE
    philhealth = salary * PHILHEALTH_RATE
    pagibig = salary * PAGIBIG_RATE
    tax = salary * TAX_RATE

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    return name, salary, total_deduction, net_salary

# Thread Parallelism

print("Thread Pooling")

start = time.time()

for name, salary in employees:
    print(f"\nProcessing Employee: {name}")

    with ThreadPoolExecutor() as executor:
        future_sss = executor.submit(compute_sss, salary)
        future_philhealth = executor.submit(compute_philhealth, salary)
        future_pagibig = executor.submit(compute_pagibig, salary)
        future_tax = executor.submit(compute_tax, salary)

        sss = future_sss.result()
        philhealth = future_philhealth.result()
        pagibig = future_pagibig.result()
        tax = future_tax.result()

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    print("Salary:", salary)
    print("SSS:", sss)
    print("PhilHealth:", philhealth)
    print("PagIBIG:", pagibig)
    print("Tax:", tax)
    print("Total Deduction:", total_deduction)
    print("Net Salary:", net_salary)
    print("-" * 30)

end = time.time()

print("\nExecution Time:", end - start)
start = time.time()

# Process Parallelism

print("\nProcess Pooling\n")

with ProcessPoolExecutor() as executor:
    results = executor.map(compute_payroll, employees)

print("Payroll Results:\n")

for name, salary, deduction, net in results:
    print(f"Employee: {name}")
    print(f"Gross Salary: {salary}")
    print(f"Total Deduction: {deduction}")
    print(f"Net Salary: {net}")
    print("-" * 30)

end = time.time()

print("Execution Time:", end - start)
