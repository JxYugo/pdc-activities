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
