Lab Act 2:

1. Which approach demonstrates true parallelism in Python? Explain.
Based on our observations, multiprocessing demonstrates true parallelism. Each process runs independently and can utilize a separate CPU core, allowing multiple grades to be computed at the same time. In contrast, multithreading runs all threads within a single process, and although multiple threads are created, the GWA outputs often appear sequential. This behavior occurs because Python threads are limited by the Global Interpreter Lock (GIL), which prevents true parallel execution.

2. Compare execution times between multithreading and multiprocessing.
Multithreading is faster for small tasks because it has lower overhead. Multiprocessing is faster for large tasks because it uses multiple CPU cores and runs tasks in true parallel.

3. Can Python handle true parallelism using threads? Why or why not?
No. Python threads cannot achieve true parallelism for CPU-bound tasks because of the Global Interpreter Lock or GIL, which allows only one thread to execute at a time per process.

4. What happens if you input a large number of grades (e.g., 1000)? Which
method is faster and why?
Multiprocessing is faster because it distributes the workload across multiple CPU cores. Multithreading is slower due to the GIL limiting execution to one thread at a time.

5. Which method is better for CPU-bound tasks and which for I/O-bound
tasks? - In CPU-bound tasks like computing GWA, the Multiprocessing is better. In our code, each grade calculation is independent, and using multiple processes allows the CPU to handle multiple calculations simultaneously. This improves performance significantly when the number of grades is high. On the otherhand, I/O-bound tasks like reading user input or printing results, Multithreading works well. Threads can perform other tasks while waiting for user input or I/O operations. In our code, threads allowed the program to print results as soon as each grade was processed without blocking the rest of the execution.

6. How did your group apply creative coding or algorithmic solutions in this
lab? To appy creative coding, first is we designed the code to take user input dynamically instead of using a fixed list of grades. Second, we used thread and process indexes in the print statements (Thread-1, Process-1) to clearly track which grade was being processed by which thread or process. We also implemented a Queue for multiprocessing to ensure outputs were printed properly without overlapping. Lastly, we measured execution time for both methods using the time module to compare performance.

Lab Act 3:

1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
- Task Parallelism runs different tasks at the same time on the same data. In the lab, this is shown using ThreadPoolExecutor, where SSS, PhilHealth, Pag-IBIG, and Tax are computed concurrently for one employee. The workload is divided by deduction type. This improves efficiency because independent deductions are calculated simultaneously instead of one after another.
- Data Parallelism runs the same task at the same time on different data. In the lab, this is shown using ProcessPoolExecutor, where the same payroll function is applied to multiple employees. The workload is divided by employee. This approach is effective for large datasets because each process works independently on separate employee records.

2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.
- submit() schedules a task and returns a Future object that holds the result. It provides more control because we can retrieve results individually and monitor task completion.
- map() runs the same function on multiple inputs concurrently and returns results in order. It is simpler when applying one function to multiple inputs without manually handling Future objects.
- A Future represents a task result that can be retrieved later using .result(). It acts as a placeholder for a value that becomes available after computation finishes.
- The with statement ensures the Executor starts and shuts down properly, preventing resource leaks. It automatically manages resources and calls shutdown() when done.

Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?
-ThreadPoolExecutor uses threads that share the same memory and are controlled by the GIL or Global Interpreter Lock. Because of the GIL, only one thread executes Python code at a time. True parallelism does not occur for CPU-bound tasks, even on multiple cores. However, it works well for I/O-bound tasks because threads can switch while waiting for input/output operations.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior.
-ProcessPoolExecutor uses separate processes, each with its own memory and GIL. This allows multiple processes to run simultaneously on different CPU cores. Because the GIL is not shared, true parallelism is achieved. This makes it ideal for CPU-intensive tasks like payroll computation.

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
-ProcessPoolExecutor scales better because it uses multiple CPU cores and avoids GIL limitations. Each employee’s payroll can be processed independently, making it efficient for large workloads. ThreadPoolExecutor is less scalable for CPU-bound tasks due to the GIL. However, threads are lighter and consume less memory compared to processes.

6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
 A Filipino company like Jollibee Foods Corporation processes payroll for thousands of employees nationwide.

= Task Parallelism (ThreadPoolExecutor):
For one employee, deductions such as SSS, PhilHealth, Pag-IBIG, and Withholding Tax are computed at the same time using threads. The workload is divided by deduction type. This reduces processing time per employee.

= Data Parallelism (ProcessPoolExecutor):
Payroll for many employees is computed simultaneously using multiple processes, where each process handles one employee. The workload is divided by employee. This significantly improves overall payroll processing speed for large companies.

= ThreadPoolExecutor improves speed for multiple deductions, while ProcessPoolExecutor improves scalability for large numbers of employees.
