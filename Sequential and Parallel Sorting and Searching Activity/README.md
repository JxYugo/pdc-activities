
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

Implementing sequential and parallel algorithms revealed that parallel execution isn't inherently faster that its success heavily depends on dataset size. Like for small datasets (under 10,000 elements), sequential methods consistently outperformed parallel ones because the overhead of thread creation, task division, synchronization barriers, and result merging completely overshadowed any computational gains. However, once the datasets exceeded roughly 100,000–250,000 elements the parallel approaches began to pull ahead, occasionally delivering a 2–3x speedup on larger sets. This clear threshold taught me that parallelism only pays off when the raw computational work justifies the setup costs.

During implementation, we struggled with index management in the parallel merge phase, frequently encountering off-by-one errors that only surfaced with specific data sizes. We also had to experiment with thread counts, learning that simply adding more threads degrades performance due to context-switching overhead. Synchronization further introduced hidden costs; preventing race conditions during parallel search and coordinating the merge step added overhead that sometimes negated gains, especially when scattered memory access hurt cache efficiency.The parallelism proved highly beneficial for large-scale sorting and searching but was counterproductive for small datasets or sub-millisecond operations. This project reinforced that effective parallel programming isn't about maximizing concurrency, but strategically applying it where data volume and computational complexity genuinely justify the overhead.

# Arao, Hugh Humphrey S. - Reflection

In this activity, I observed that sequential and parallel execution differ mainly in how tasks are processed. Sequential algorithms follow a single, step-by-step flow, while parallel algorithms divide the dataset into smaller parts and process them simultaneously using multiple processes. This makes parallel execution more complex due to coordination, but it allows better utilization of system resources.

When analyzing performance across different dataset sizes, I found that sequential algorithms performed better on small datasets because they have minimal overhead. However, as the dataset size increased, parallel algorithms became more competitive and sometimes faster, especially in sorting tasks. This shows that parallelism is more effective when the workload is large enough to justify splitting the computation.

During implementation, I encountered several challenges, particularly in ensuring correctness in the parallel versions. For searching, I had to carefully manage offsets to return the correct global index. For sorting, merging multiple sorted chunks into a single correctly ordered list required additional logic. Managing processes and ensuring proper synchronization using queues also added complexity compared to the simpler sequential approach.

A key insight I gained is that parallel algorithms introduce overhead such as process creation, communication, and synchronization. These factors can significantly impact performance, especially for smaller datasets. If not handled properly, synchronization and merging steps can also lead to incorrect results or inefficiencies.

Overall, parallelism was beneficial when working with large datasets, particularly for sorting where the workload could be effectively divided. However, for smaller datasets and simple operations like linear search, parallel execution was unnecessary and even slower due to overhead. This activity showed that choosing between sequential and parallel approaches depends on balancing workload size and system costs.



