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
def run_multithreading(grades):
    print("\nStarting multithreading execution...")
    threads = []
    start = time.time()
    for i, grade in enumerate(grades):
        t = threading.Thread(target=compute_gwa_thread, args=(grade, i+1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.time()
    elapsed = end - start
    print(f"Multithreading execution time: {elapsed:.4f} seconds\n")
    return elapsed

def compute_gwa_process(grade, idx, queue):
    gwa = grade 
    output = f"[Process-{idx}] Calculated GWA for grade {grade}: {gwa}"
    queue.put(output)

