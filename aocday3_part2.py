####### Day 3: Gear Ratios ##########
symbols = { '#', '+', '*', '$', '-', '/' ,  '=', '%', '&', '@', '!', ':', ';', '~', '|', '<', '>', '^', '_', '`', '?'}
matrix = []

def check_for_adjacent_numbers(matrix, i, j):
    rows, cols = len(matrix), len(matrix[0])
    temp = set()  # Using a set to avoid duplicates
    processed_cells = set()  # Track cells that are already part of a number

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in processed_cells:
                if matrix[ni][nj].isdigit():
                    number = get_full_number_from_position(matrix[ni], nj)
                    temp.add(int(number))

                    # Mark all cells of this number as processed
                    left, right = nj, nj
                    while left >= 0 and matrix[ni][left].isdigit():
                        processed_cells.add((ni, left))
                        left -= 1
                    while right < cols and matrix[ni][right].isdigit():
                        processed_cells.add((ni, right))
                        right += 1

    if len(temp) == 2:
        return list(temp)
    else:
        return False
    


def get_full_number_from_position(array, position):
    def is_digit(s):
        return s.isdigit()

    def extract_full_number(array, start):
        # Extract number to the left
        number = ''
        i = start
        while i >= 0 and is_digit(array[i]):
            number = array[i] + number
            i -= 1

        # Extract number to the right (excluding the start position)
        i = start + 1
        while i < len(array) and is_digit(array[i]):
            number += array[i]
            i += 1

        return number

    if position < 0 or position >= len(array):
        return None  # Position out of bounds

    if is_digit(array[position]):
        return extract_full_number(array, position)
    else:
        return None




def find_gears(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] in symbols:
            
                temp = check_for_adjacent_numbers(matrix, i, j)
                if temp:
                    sum = sum + (temp[0] * temp[1])
                    
         
    return sum
             

with open('input3.txt','r') as file:
    # create matrix
    for line in file:
        input_str = line.strip()
        matrix.append([char for char in input_str])

       

sum_of_gear_ratios = find_gears(matrix)

    
print("Sum ", sum_of_gear_ratios)






