####### Day 3: Gear Ratios ##########
symbols = { '#', '+', '*', '$', '-', '/' ,  '=', '%', '&', '@', '!', ':', ';', '(', ')', '[', ']', '{', '}', '~', '|', '<', '>', '^', '_', '`', '?'}
matrix = []

def check_for_adjacent_symbols(matrix, i, j):
    rows, cols = len(matrix), len(matrix[0])
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                if matrix[ni][nj] in symbols:
                    return True
    return False

def find_numbers_with_adjacent_symbols(matrix):
    sum_of_numbers = 0
    for i in range(len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j].isdigit():
                start = j
                while j < len(matrix[i]) and matrix[i][j].isdigit():
                    j += 1
                number = int(''.join(matrix[i][start:j]))
                if any(check_for_adjacent_symbols(matrix, i, k) for k in range(start, j)):
                    sum_of_numbers += number
            else:
                j += 1
    return sum_of_numbers



with open('input3.txt','r') as file:
  
    for line in file:
        input_str = line.strip()
        
        matrix.append([char for char in input_str])
       

sum_with_symbols = find_numbers_with_adjacent_symbols(matrix)

    
print("Sum of numbers with adjacent symbols:", sum_with_symbols)






