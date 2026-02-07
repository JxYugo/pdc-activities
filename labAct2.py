import threading
import time
from multiprocessing import Process, Queue
import sys

def input_grades():
    grades = []
    print("Enter grades one by one (type 'done' to finish):")
    while True:
        inp = input("Grade: ")
        if inp.lower() == 'done':
            break
        try:
            val = float(inp)
            grades.append(val)
        except ValueError:
            print("Invalid input. Please enter a numeric grade or 'done'.")
    return grades

def compute_gwa_thread(grade, idx):
    gwa = grade
    print(f"[Thread-{idx}] Calculated GWA for grade {grade}: {gwa}")
