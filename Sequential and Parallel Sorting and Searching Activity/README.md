
# Sequential and Parallel Sorting and Searching

## Activity Overview:

This project compares the performance of sequential and parallel implementations of:

- Merge Sort (sorting)
- Linear Search (searching)

The goal is to analyze how parallel processing affects performance across different dataset sizes and configurations.

## System Design
### Datasets

Three dataset sizes were used:

- Small: 1,000 elements
- Medium: 100,000 elements
- Large: 1,000,000 elements

Each size includes:

- Random dataset
- Sorted dataset
- Reverse sorted dataset

### Sorting Algorithm

#### Sequential Merge Sort
A standard recursive merge sort was implemented.

#### Parallel Merge Sort
- Dataset was divided into chunks
- Each chunk sorted using multiple processes (ProcessPoolExecutor)
- Results merged into a final sorted list

### Searching Algorithm

#### Sequential Linear Search
Iterates through the dataset one element at a time

#### Parallel Linear Search
Dataset divided into chunks
Each process searches independently
Results combined using a queue

## Demo

<img width="1608" height="722" alt="implementation" src="https://github.com/user-attachments/assets/0b418420-763c-4e4b-9ce4-f9ca13a0d660" />

## Observations and Key Insights

### Observations

#### Sequential VS Parallel Sort
- Parallel merge sort performs worse on small datasets
- Performance becomes comparable or better on large datasets
- Sorted datasets sometimes reduce performance gain due to reduced workload complexity

#### Sequential VS Parallel Search
- Sequential search is consistently faster across all dataset sizes
- Parallel search shows significant overhead (~0.1s) regardless of dataset size
- No meaningful speedup is observed

### Key Insights

#### Sequential VS Parallel Sort
- Parallel processing improves performance only when the dataset is large enough to offset multiprocessing overhead.

#### Sequential VS Parallel Search
- Linear search does not benefit from parallelization because the cost of process management outweighs the simplicity of the operation.

# Reflections:



### Jison, Remar B. - Reflection



### Arao, Hugh Humphrey S. - Reflection

In this activity, I observed that sequential and parallel execution differ mainly in how tasks are processed. Sequential algorithms follow a single, step-by-step flow, while parallel algorithms divide the dataset into smaller parts and process them simultaneously using multiple processes. This makes parallel execution more complex due to coordination, but it allows better utilization of system resources.

When analyzing performance across different dataset sizes, I found that sequential algorithms performed better on small datasets because they have minimal overhead. However, as the dataset size increased, parallel algorithms became more competitive and sometimes faster, especially in sorting tasks. This shows that parallelism is more effective when the workload is large enough to justify splitting the computation.

During implementation, One challenge we encountered was understanding why the parallel search was slower than the sequential search. Initially, this was confusing and unexpected. Later on, we realized that the slowdown was caused by the overhead from partitioning the data and creating additional processes, which outweighed the benefits of parallelization.

A key insight I gained is that parallel algorithms introduce overhead such as process creation, communication, and synchronization. These factors can significantly impact performance, especially for smaller datasets. If not handled properly, synchronization and merging steps can also lead to incorrect results or inefficiencies.

### Yugo, James Xander A. - Reflection

During the implementation of both sequential and parallel algorithms, I observed clear differences in their performance and behavior. For merge sort, the parallel version started off slower than the sequential one when using small datasets due to the overhead of creating processes and dividing the data. However, as the dataset size increased, the parallel version became more better and sometimes slightly faster in some cases, but still it is sometimes slower, it is inconsistent too. For linear search, the sequential version consistently outperformed the parallel version across all dataset sizes. Since linear search is a simple and lightweight operation, the overhead from multiprocessing, such as process creation and inter-process communication, made the parallel version slower.

In terms of performance across dataset sizes, I noticed that increasing the size had a greater effect on sequential algorithms, especially for merge sort, where execution time increased noticeably. Parallel merge sort sometimes handled larger datasets better because the work was divided among multiple processes. However, this improvement was not observed in linear search, where the time difference remained low for sequential execution but consistently high for parallel due to overhead.

One of the main challenges I encountered was trying to make the parallel linear search perform better, but it is actually in a normal behavior.

Through this project, I gained a better understanding of overhead and synchronization. I realized that parallel algorithms introduce additional costs that are not present in sequential execution. These include process startup time, memory usage, and communication between processes. If the task itself is not computationally intensive, these overhead costs can outweigh any potential speedup. Synchronization also plays a role, especially when combining results from different processes, which can add delays.

Overall, parallelism was beneficial in situations where the task involved heavy computation and large datasets, such as merge sort. However, it was unnecessary for simpler tasks like linear search. This project helped me understand that choosing between sequential and parallel approaches depends on the nature of the problem, and not all algorithms will benefit from parallel execution.

Overall, parallelism was beneficial when working with large datasets, particularly for sorting where the workload could be effectively divided. However, for smaller datasets and simple operations like linear search, parallel execution was unnecessary and even slower due to overhead. This activity showed that choosing between sequential and parallel approaches depends on balancing workload size and system costs.

### Ampuan, Ayyah M. - Reflection
In this project, I saw clear differences between sequential and parallel execution for merge sort and linear search. Sequential code was simpler and more predictable, while parallel code required splitting data, managing processes, and merging results, which made it more complex.

Performance also depended on dataset size. For small datasets, sequential execution was often faster because the overhead of creating processes and combining results slowed down the parallel version. For larger datasets, especially in merge sort, parallelism showed better speedup because the workload was heavy enough to use multiple CPU cores effectively.

One challenge we faced was improving the parallel linear search. We were confused about how to make it more efficient, and despite our efforts, we could not achieve significant improvement due to process overhead and communication costs.

Overall, I learned that parallelism is only beneficial for large, heavy tasks. For small or simple operations, sequential execution is often faster and easier to implement.

### Abdulkarim, Hakima S. - Reflection 

From what I observed in our implementation, the difference between sequential and parallel execution becomes clearer depending on the dataset size. When I tested smaller datasets, the sequential version actually performed better because it runs directly without extra steps. The parallel version, although designed to be faster, had additional overhead like creating processes and managing communication between them. But when I moved to larger datasets, that’s where parallel execution started to make more sense. The workload was divided into chunks, so multiple processes could handle parts of the task at the same time, which improved overall performance.

Another thing I noticed is how performance changes based on the type and size of the data. For merge sort, whether the dataset was random, sorted, or reverse sorted didn’t really change much in terms of execution time since the algorithm follows the same pattern. However, for linear search, the results were more situational. In the sequential version, the position of the target matters a lot, but in the parallel version, the search becomes faster on average because different parts of the dataset are checked at the same time. Still, implementing the parallel versions was not that easy. I had to deal with issues like splitting the data properly, making sure processes return the correct results, and handling queues, which made debugging more complicated.

Overall, this activity helped me understand that parallelism is not always automatically better. There are trade-offs, especially with overhead and synchronization. If the dataset is small, the extra work from parallel processing can actually slow things down instead of helping. But for larger datasets or heavier tasks, parallelism becomes more useful and efficient. This made me realize that choosing between sequential and parallel approaches depends on the situation, not just the idea that parallel is faster.
