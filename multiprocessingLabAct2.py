from multiprocessing import Process, Queue
import ipywidgets as widgets
from IPython.display import display
import time

def compute_gwa_process(pid, grades, queue):
    gwa = sum(grades) / len(grades)
    time.sleep(1)
    queue.put(f"Process {pid}: GWA = {gwa:.2f}")

subject_count = widgets.IntText(value=3, description="Subjects:")
grades_box = widgets.VBox()
grade_inputs = []

