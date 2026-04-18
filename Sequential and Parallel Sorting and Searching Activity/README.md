
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



