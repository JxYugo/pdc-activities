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
