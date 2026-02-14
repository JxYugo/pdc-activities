Lab Act 2:

1. Which approach demonstrates true parallelism in Python? Explain.
Based on our observations, multiprocessing demonstrates true parallelism. Each process runs independently and can utilize a separate CPU core, allowing multiple grades to be computed at the same time. In contrast, multithreading runs all threads within a single process, and although multiple threads are created, the GWA outputs often appear sequential. This behavior occurs because Python threads are limited by the Global Interpreter Lock (GIL), which prevents true parallel execution.

2. Compare execution times between multithreading and multiprocessing.

3. Can Python handle true parallelism using threads? Why or why not?

4. What happens if you input a large number of grades (e.g., 1000)? Which
method is faster and why?

5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks? - In CPU-bound tasks like computing GWA, the Multiprocessing is better. In our code, each grade calculation is independent, and using multiple processes allows the CPU to handle multiple calculations simultaneously. This improves performance significantly when the number of grades is high. On the otherhand, I/O-bound tasks like reading user input or printing results, Multithreading works well. Threads can perform other tasks while waiting for user input or I/O operations. In our code, threads allowed the program to print results as soon as each grade was processed without blocking the rest of the execution.

6. How did your group apply creative coding or algorithmic solutions in this
lab? To appy creative coding, first is we designed the code to take user input dynamically instead of using a fixed list of grades. Second, we used thread and process indexes in the print statements (Thread-1, Process-1) to clearly track which grade was being processed by which thread or process. We also implemented a Queue for multiprocessing to ensure outputs were printed properly without overlapping. Lastly, we measured execution time for both methods using the time module to compare performance.

Lab Act 3:

1. 
- Task Parallelism runs different tasks at the same time on the same data. In the lab, this is shown using ThreadPoolExecutor, where SSS, PhilHealth, Pag-IBIG, and Tax are computed concurrently for one employee. The workload is divided by deduction type.

- Data Parallelism runs the same task at the same time on different data. In the lab, this is shown using ProcessPoolExecutor, where the same payroll function is applied to multiple employees. The workload is divided by employee.

2. 
- submit() schedules a task and returns a Future object that holds the result.
- map() runs the same function on multiple inputs concurrently and returns results in order.
- A Future represents a task result that can be retrieved later using .result().
- The with statement ensures the Executor starts and shuts down properly, preventing resource leaks.

3. ThreadPoolExecutor uses threads that share the same memory and are controlled by the GIL or Global Interpreter Lock. Because of the GIL, only one thread executes Python code at a time. True parallelism does not occur for CPU-bound tasks, even on multiple cores.

4. ProcessPoolExecutor uses separate processes, each with its own memory and GIL. This allows multiple processes to run simultaneously on different CPU cores. Because the GIL is not shared, true parallelism is achieved.

5. ProcessPoolExecutor scales better because it uses multiple CPU cores and avoids GIL limitations. Each employee’s payroll can be processed independently, making it efficient for large workloads. ThreadPoolExecutor is less scalable for CPU-bound tasks due to the GIL.

6.  A Filipino company like Jollibee Foods Corporation processes payroll for thousands of employees nationwide.

= Task Parallelism (ThreadPoolExecutor):
For one employee, deductions such as SSS, PhilHealth, Pag-IBIG, and Withholding Tax are computed at the same time using threads. The workload is divided by deduction type.

= Data Parallelism (ProcessPoolExecutor):
Payroll for many employees is computed simultaneously using multiple processes, where each process handles one employee. The workload is divided by employee.

= ThreadPoolExecutor improves speed for multiple deductions, while ProcessPoolExecutor improves scalability for large numbers of employees.
