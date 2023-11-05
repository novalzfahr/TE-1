import random
import time
import random
import psutil
import multiprocessing

def calculate_block_size(n):
    ratio = 10 / 26
    exponent = 0
    while (2 ** (exponent + 1)) <= n:
        exponent += 1
    block_size = 2 ** (ratio * exponent)
    return int(block_size)


def two_pivot_block_partition(A, low, high, B):
    # Initialize the pivot values
    p = A[low]
    q = A[high]
    block = [0] * B
    i = low + 1
    j = low + 1
    k = low + 1
    num_p = 0
    num_q = 0

    while k < high:
        t = min(B, high - k)

        for c in range(t):
            block[num_q] = c
            num_q += int(q >= A[k + c])

        for c in range(num_q):
            A[j + c], A[k + block[c]] = A[k + block[c]], A[j + c]

        k += t

        for c in range(num_q):
            block[num_p] = c
            num_p += int(p > A[j + c])

        for c in range(num_p):
            A[i], A[j + block[c]] = A[j + block[c]], A[i]
            i += 1

        j += num_q
        num_p = 0
        num_q = 0

    A[i - 1], A[low] = A[low], A[i - 1]
    A[j], A[high] = A[high], A[j]

    return i - 1, j

def two_pivot_block_quicksort(A, low, high):
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()

        if high <= low:
            continue
        # Make sure that the initial pivot is smaller than the second pivot.
        if A[low] > A[high]:
            A[low], A[high] = A[high], A[low]

        block_size = calculate_block_size(high - low + 1)
        i, j = two_pivot_block_partition(A, low, high, block_size)

        stack.append((low, i - 1))
        stack.append((i, j - 1))
        stack.append((j + 1, high))

# Function to measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss

# Function to measure execution time
def measure_execution_time(arr):
    start_time = time.time()
    two_pivot_block_quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def run_sorting_process(size, variation):    
    if variation == 'random':
        arr = random.sample(range(size), size)
    elif variation == 'sorted':
        arr = list(range(size))
    elif variation == 'reversed':
        arr = list(range(size, 0, -1))

    # Measure memory usage before sorting
    before_memory = measure_memory_usage()

    # Measure execution time
    execution_time = measure_execution_time(arr)

    # Measure memory usage after sorting
    after_memory = measure_memory_usage()

    print(f"Size: {size}, Variation: {variation}, Execution Time (ms):{execution_time:.2f}, Memory Usage Before Sorting: {before_memory}, Memory Usage After Sorting: {after_memory}")

if __name__ == '__main__':
    # Define dataset sizes and variations
    size_dataset = [2**9, 2**13, 2**16]
    variations = ['sorted', 'random', 'reversed']

    for size in size_dataset:
        for variation in variations:
            process = multiprocessing.Process(target=run_sorting_process, args=(size, variation))
            process.start()
            process.join()  # Wait for the process to finish

            # Terminate the process to release memory
            process.terminate()
            process.join()