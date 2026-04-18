
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



