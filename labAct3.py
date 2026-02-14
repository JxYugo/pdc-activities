


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
