import random
from two_pivot_block_quicksort import *

# Uji coba memakai dataset sendiri
sample_datasets = {
    "small_size_sorted": list(range(10)),
    "small_size_random": random.sample(range(10 ), 10),
    "small_size_reversed": list(range(9, -1, -1)),
    "medium_size_sorted": list(range(20)),
    "medium_size_random": random.sample(range(20), 20),
    "medium_size_reversed": list(range(19, -1, -1)),
    "large_size_sorted": list(range(30)),
    "large_size_random": random.sample(range(30), 30),
    "large_size_reversed": list(range(29, -1, -1))
}

print("Before two pivot block quick sort:")
for key, data in sample_datasets.items():
    print(f"{key}: {data}")

print("\nResults after two pivot block quick sort:")
for key, data in sample_datasets.items():
    sorted_data = data.copy()
    two_pivot_block_quicksort(sorted_data, 0, len(sorted_data) -1)
    print(f"{key}: {sorted_data}")