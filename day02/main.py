import os

dir_path = os.path.abspath(__file__)
dir_path = os.path.dirname(dir_path)

file_path = dir_path + '/test.txt'

def find_invalid_ids_A(r):
    sum_invalid_ids = 0

    values = r.split('-')
    start = int(values[0])
    end = int(values[1])

    for i in range(start, end + 1):
        id = str(i)
        length = len(id)
        if id[int(length/2):] == id[:int(length/2)]:
            sum_invalid_ids += i
    return sum_invalid_ids

def find_invalid_ids_B(r):
    sum_invalid_ids = 0

    values = r.split('-')
    start = int(values[0])
    end = int(values[1])

    for i in range(start, end + 1):
        s = str(i)
        n = len(s)
        invalid = False

        for size in range(1, n // 2 + 1):
            if n % size != 0:
                continue
            part = s[:size]
            if part * (n // size) == s:
                invalid = True
                break

        if invalid:
            sum_invalid_ids += i

    return sum_invalid_ids

# --- Part One ---
ranges = []
sum_invalid_ids = 0

with open(file_path, 'r', encoding='utf-8') as file:    
    line = file.readline()
    ranges = line.split(',');
    for r in ranges:
        sum_invalid_ids += find_invalid_ids_A(r)
      
    print(f"Answer Part One : {sum_invalid_ids}")

# --- Part Two ---
ranges = []
sum_invalid_ids = 0

with open(file_path, 'r', encoding='utf-8') as file:    
    line = file.readline()
    ranges = line.split(',');
    for r in ranges:
        sum_invalid_ids += find_invalid_ids_B(r)

    print(f"Answer Part Two : {sum_invalid_ids}")