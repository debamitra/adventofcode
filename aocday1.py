
def find_digits(input_string, word_digit_map):
    digits = []
    for i in range(len(input_string)):
        if input_string[i].isdigit():
            digits.append(input_string[i])
        else:
            # Check for word match up to 5 letters
            for j in range(1, 6):
                if i + j <= len(input_string):
                    word = input_string[i:i+j].lower()
                    if word in word_digit_map:
                        digits.append(word_digit_map[word])
                        break  # Break the inner loop if a match is found
            
    return digits
sum = 0
with open('input.txt', 'r') as file:
    # Read and process each line
    for line in file:
        # Strip newline characters and any leading/trailing whitespace
        input_str = line.strip()
        word_to_digit = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4', 
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }
        extracted_digits = find_digits(input_str, word_to_digit)
        # Forming a two-digit number
        if extracted_digits:
            first_digit = extracted_digits[0]
            last_digit = extracted_digits[-1]
            two_digit_number = first_digit + last_digit if len(extracted_digits) > 1 else first_digit * 2
            two_digit_number_int = int(two_digit_number)
        else:
            two_digit_number_int = "No valid digits found in the input string."
            
        sum = sum + two_digit_number_int
    print(sum)

       