from time import sleep
from tqdm import tqdm
from ex08.Loading import ft_tqdm

print("My TQDM:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

print("Original TQDM:")
for elem in tqdm(range(333)):
    sleep(0.005)
print()

print("My TQDM:")
for elem in ft_tqdm(range(1000)):
    sleep(0.0005)
print()

print("Original TQDM:")
for elem in tqdm(range(1000)):
    sleep(0.0005)
print()

print("My TQDM:")
for elem in ft_tqdm(range(3)):
    sleep(1)
print()

print("Original TQDM:")
for elem in tqdm(range(3)):
    sleep(1)
print()

print("My TQDM:")
for elem in ft_tqdm(range(-1)):
    sleep(1)
print()

print("Original TQDM:")
for elem in tqdm(range(-1)):
    sleep(1)
print()

print("My TQDM:")
for elem in ft_tqdm(range(-100, 0, -1)):
    sleep(1)
print()

print("Original TQDM:")
for elem in tqdm(range(-100, 0, -1)):
    sleep(1)
print()