import random
import time
import random
import psutil
import multiprocessing

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Function to measure memory usage
def measure_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss

# Function to measure execution time
def measure_execution_time(arr):
    start_time = time.time()
    merge_sort(arr)
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

    print(f"Size: {size}, Variation: {variation}, Execution Time (ms): {execution_time:.2f}, Memory Usage Before Sorting: {before_memory}, Memory Usage After Sorting: {after_memory}")

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