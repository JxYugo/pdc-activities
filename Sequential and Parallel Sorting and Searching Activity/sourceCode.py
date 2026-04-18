# Importing Dependencies
import random
import time
import concurrent.futures
import pandas as pd
import matplotlib.pyplot as plt
import os
from multiprocessing import Process, Queue

# Dataset Creation Function
import random

# Functions
def create_dataset(size, max_value):
    return [random.randint(1, max_value) for _ in range(size)]

def create_sorted_dataset(size, max_value):
    return sorted([random.randint(1, max_value) for _ in range(size)])

def create_reverse_sorted_dataset(size, max_value):
    return sorted([random.randint(1, max_value) for _ in range(size)], reverse=True)

# Creating Datasets
smallDataset = create_dataset(1000, 100)
mediumDataset = create_dataset(100000, 100)
largeDataset = create_dataset(1000000, 100)

# Special Cases: Already Sorted
small_sorted = create_sorted_dataset(1000, 100)
medium_sorted = create_sorted_dataset(100000, 100)
large_sorted = create_sorted_dataset(1000000, 100)

# Special Cases: Reverse Sorted
small_reverse = create_reverse_sorted_dataset(1000, 100)
medium_reverse = create_reverse_sorted_dataset(100000, 100)
large_reverse = create_reverse_sorted_dataset(1000000, 100)

# Validating Dataset Contents

def preview(data, n=10):
    return "[" + ", ".join(map(str, data[:n])) + ", ...]"

# Sequential Merge Sort Functions
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)

# Parallel Merge Sort Functions
def parallel_merge_sort(data):
    if len(data) <= 1:
        return data

    max_workers = 4

    chunk_size = len(data) // max_workers
    if chunk_size == 0:
        return merge_sort(data)

    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        sorted_chunks = list(executor.map(merge_sort, chunks))

    while len(sorted_chunks) > 1:
        new_chunks = []

        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                new_chunks.append(merge(sorted_chunks[i], sorted_chunks[i + 1]))
            else:
                new_chunks.append(sorted_chunks[i])

        sorted_chunks = new_chunks

    return sorted_chunks[0]

# Sequential Linear Search Functions

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Parallel Linear Search Functions

def worker(sub_data, target, q, offset):
    for i, value in enumerate(sub_data):
        if value == target:
            q.put(offset + i)
            return
    q.put(-1)

def parallel_linear_search(data, target):
    number_processes = 4
    chunk_size = len(data) // number_processes

    q = Queue()
    processes = []

    for i in range(number_processes):
        start = i * chunk_size
        end = len(data) if i == number_processes - 1 else (i + 1) * chunk_size

        p = Process(target=worker, args=(data[start:end], target, q, start))
        processes.append(p)
        p.start()

    results = [q.get() for _ in processes]

    for p in processes:
        p.join()

    valid = [r for r in results if r != -1]
    return min(valid) if valid else -1

# Outputs:

# Validating Contents

print("Showing first 10 integers: (random dataset)")
print("Small:", preview(smallDataset))
print("Medium:", preview(mediumDataset))
print("Large:", preview(largeDataset))

print("\nShowing first 10 integers: (sorted dataset)")
print("Small:", preview(small_sorted))
print("Medium:", preview(medium_sorted))
print("Large:", preview(large_sorted))

print("\nShowing first 10 integers: (reverse sorted dataset)")
print("Small:", preview(small_reverse))
print("Medium:", preview(medium_reverse))
print("Large:", preview(large_reverse))

# Validating Size

print("\nShowing dataset size: (random)")
print("Small:", len(smallDataset))
print("Medium:", len(mediumDataset))
print("Large:", len(largeDataset))

print("\nShowing dataset size: (sorted)")
print("Small:", len(small_sorted))
print("Medium:", len(medium_sorted))
print("Large:", len(large_sorted))

print("\nShowing dataset size: (reverse sorted)")
print("Small:", len(small_reverse))
print("Medium:", len(medium_reverse))
print("Large:", len(large_reverse))

print("\n")
print("=" * 50)
print("\n")

# Running and Comparison (Sorting)

datasets = {
  "Small": smallDataset,
  "Medium": mediumDataset,
  "Large": largeDataset,
  "Small Sorted": small_sorted,
  "Medium Sorted": medium_sorted,
  "Large Sorted": large_sorted,
  "Small Reverse Sorted": small_reverse,
  "Medium Reverse Sorted": medium_reverse,
  "Large Reverse Sorted": large_reverse
  }

sort_results = []

print("Sorting")

for name, data in datasets.items():
  print(f"\n--- {name} Dataset ---")

  start = time.time()
  seq = merge_sort(data)
  seq_time = time.time() - start

  start = time.time()
  par = parallel_merge_sort(data)
  par_time = time.time() - start

  print("Sorted Correctly:", seq == par)
  print(f"Sequential Time: {seq_time:.4f} sec")
  print(f"Parallel Time:   {par_time:.4f} sec")

  sort_results.append((name, seq_time, par_time))

print("\n")
print("=" * 50)
print("\n")

# Speedup ratio table (Sorting):

table = []

for name, seq_time, par_time in sort_results:
  speedup = seq_time / par_time if par_time > 0 else 0
  table.append([name, seq_time, par_time, speedup])

df = pd.DataFrame(table, columns=[
  "Dataset",
  "Sequential (s)",
  "Parallel (s)",
  "Speedup (x)"
])

print("\nSpeedup Ratio Table\n")
print(df)

print("\n")
print("=" * 50)
print("\n")

# Comparison Graphs (Sorting):

# Time Comparison:
plt.figure(figsize=(12,6))

plt.plot(df["Dataset"], df["Sequential (s)"], marker='o', label="Sequential")
plt.plot(df["Dataset"], df["Parallel (s)"], marker='o', label="Parallel")

plt.xticks(rotation=45)
plt.title("Sequential vs Parallel Merge Sort Time")
plt.xlabel("Dataset")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

print("\n")
print("=" * 50)
print("\n")


# Speedup Ratio Comparison:
plt.figure(figsize=(12,6))

plt.plot(df["Dataset"], df["Speedup (x)"], marker='o', color='green')
plt.axhline(y=1, color='red', linestyle='--', label="No Speedup (1x)")

plt.xticks(rotation=45)
plt.title("Speedup Ratio Sequential vs Parallel")
plt.xlabel("Dataset")
plt.ylabel("Speedup")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

print("\n")
print("=" * 50)
print("\n")

# Running and Comparison (Searching)

search_results = []

print("Searching")

for name, data in datasets.items():
    print(f"\n--- {name} Dataset ---")

    target = data[len(data)//2]

    start = time.time()
    seq = linear_search(data, target)
    seq_time = time.time() - start

    start = time.time()
    par = parallel_linear_search(data, target)
    par_time = time.time() - start

    print(f"Target Value: {target}")
    print(f"Sequential Found Index: {seq}")
    print(f"Parallel Found Index:   {par}")

    print(f"Sequential Time: {seq_time:.6f}")
    print(f"Parallel Time:   {par_time:.6f}")

    search_results.append((name, seq_time, par_time))

print("\n")
print("=" * 50)
print("\n")

# Speedup Ratio Table (Searching)

search_table = []

for name, seq_time, par_time in search_results:
    speedup = seq_time / par_time if par_time > 0 else 0
    search_table.append([name, seq_time, par_time, speedup])

search_df = pd.DataFrame(search_table, columns=[
    "Dataset",
    "Sequential (s)",
    "Parallel (s)",
    "Speedup (x)"
])

print("\nLinear Search Speedup Ratio Table\n")
print(search_df)

print("\n")
print("=" * 50)
print("\n")

# Comparison Graphs (Searching):

plt.figure(figsize=(12,6))

plt.plot(search_df["Dataset"], search_df["Sequential (s)"], marker='o', label="Sequential")
plt.plot(search_df["Dataset"], search_df["Parallel (s)"], marker='o', label="Parallel")

# Time Comparison:

plt.xticks(rotation=45)
plt.title("Sequential vs Parallel Linear Search Time")
plt.xlabel("Dataset")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

print("\n")
print("=" * 50)
print("\n")

# Speedup Ratio Comparison:
plt.figure(figsize=(12,6))

plt.plot(search_df["Dataset"], search_df["Speedup (x)"], marker='o', color='green')
plt.axhline(y=1, color='red', linestyle='--', label="No Speedup (1x)")

plt.xticks(rotation=45)
plt.title("Speedup Ratio: Sequential vs Parallel Linear Search")
plt.xlabel("Dataset")
plt.ylabel("Speedup (x)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

print("\n")
print("=" * 50)
print("\n")
