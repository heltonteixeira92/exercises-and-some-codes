import multiprocessing
import concurrent.futures  # available in python 3.2 and above
import time

names = ['bob', 'jane', 'joe', 'sue', 'tom', 'tim']


def print_name(name):
    time.sleep(1)
    print(name)


start = time.time()

# method No 1
# in this metod it take 6 seconds to complete the task
# result = list(map(print_name, names))

# method No 2
# in this method it take 2 seconds to complete the task
# pool = multiprocessing.Pool(processes=1)
# result = pool.map(print_name, names)

# method No 3
# in this method it take 1 seconds to complete the task
with concurrent.futures.ThreadPoolExecutor() as executor:
    result = executor.map(print_name, names)

end = time.time()

print(f'Finished in {end - start:.2f} seconds')
