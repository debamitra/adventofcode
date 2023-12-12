import re

limit_red = 12
limit_green = 13
limit_blue = 14
game_id_total = 0

with open('input1.txt', 'r') as file:
    # Read and process each line
    for line in file:
        # Strip newline characters and any leading/trailing whitespace
        input_str = line.strip()

        # Extracting the game ID
        game_id_match = re.search(r"Game (\d+):", input_str)
        game_id = int(game_id_match.group(1)) if game_id_match else None
        print(game_id)

        # Extracting the counts for each color
        color_counts_raw = re.findall(r"(\d+) (blue|green|red)", input_str)
        print(color_counts_raw)
        # Initializing variables to track the max count for each color
        max_blue = max_green = max_red = 0

        # Iterating over the counts to find the maximum for each color
        for count, color in color_counts_raw:
            count = int(count)
            if color == "blue" and count > max_blue:
                max_blue = count
            elif color == "green" and count > max_green:
                max_green = count
            elif color == "red" and count > max_red:
                max_red = count

        power = max_blue * max_green * max_red
        game_id_total = power + game_id_total

        # # Is game possible
        # if max_blue <= limit_blue and max_green <= limit_green and max_red <= limit_red:
        #      game_id_total = game_id_total + game_id
        
    print(game_id_total)
     


    