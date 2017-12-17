def main():
    file_name = get_file_name()
    rowsi_colsi_wsl_wordsl = parse_file(file_name)

    num_of_rows = rowsi_colsi_wsl_wordsl[0]
    num_of_cols = rowsi_colsi_wsl_wordsl[1]
    word_search = rowsi_colsi_wsl_wordsl[2]
    words_to_search = rowsi_colsi_wsl_wordsl[3]
    find_words(num_of_rows, num_of_cols, word_search, words_to_search)

def get_file_name()->str:
    file_name = input("Enter the name of the file that contains the word search: ")
    return file_name

def parse_file(file_name) -> list:
    rowsi_colsi_wsl_wordsl = []
    word_search = []
    words_to_search = []

    with open(file_name, 'r') as myfile:
        data = myfile.readline().replace('\n', '')
        rows_and_cols = data.split(" ")
        rowsi_colsi_wsl_wordsl.append(int(rows_and_cols[0]))
        rowsi_colsi_wsl_wordsl.append(int(rows_and_cols[1]))

        num_of_rows = int(rows_and_cols[0])

        for row in range(num_of_rows):
            new_row = []
            new_data = myfile.readline().replace('\n', '')

            for letter in new_data:
                if letter == " ":
                    pass
                else:
                    new_row.append(letter.upper())
            word_search.append(new_row)

        rowsi_colsi_wsl_wordsl.append(word_search)

        myfile.readline()

        while True:
            word = myfile.readline()
            if len(word) > 0:
                word = word.upper()
                word = word.replace("\n", "")
                words_to_search.append(word)
            else:
                break

        words_to_search.sort()
        rowsi_colsi_wsl_wordsl.append(words_to_search)

        return rowsi_colsi_wsl_wordsl

def find_words( num_of_rows, num_of_cols, word_search, words_to_search):
    for word in words_to_search:
        while True:
            if is_forward_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_downwards_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_diag_word_right(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_diag_word_left(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_reverse_forward_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_reverse_downward_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_reverse_diag_word_left(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_reverse_diag_word_right(word_search, word, num_of_rows, num_of_cols):
                break

def is_forward_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_forward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    possible_cols = num_of_cols - len(word) + 1
    current_col = 0

    for row in range(num_of_rows):
        for col in range(possible_cols):
            if word_search[row][col] == word[0]:
                counter = 0
                for curr_col in range(col, col + len(word)):
                    if word_search[row][curr_col] == word[counter]:
                        counter += 1
                        current_col = curr_col
                    else:
                        break
                if counter == len(word):
                    is_forward = True
                    starting_point_init = row
                    starting_point_close = col
                    ending_point_init = row
                    ending_point_close = current_col
                    break
        if is_forward:
            break
    if is_forward:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close )+ ")" )
    return is_forward

def is_downwards_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_downward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    current_row = 0
    possible_rows = num_of_rows - len(word) + 1

    for row in range(0, possible_rows):
        for col in range(0, num_of_cols):
            if word_search[row][col] == word[0]:
                counter = 0
                for curr_row in range(row, row + len(word)):
                    if word_search[curr_row][col] == word[counter]:
                        counter += 1
                        current_row = row + len(word) - 1
                    else:
                        break
                if counter == len(word):
                    is_downward = True
                    starting_point_init = row
                    starting_point_close = col
                    ending_point_init = current_row
                    ending_point_close = col
                    break
        if is_downward:
            break
    if is_downward:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_downward

def is_diag_word_right(word_search: list, word: str, num_of_rows: int, num_of_cols: int)-> bool:
    is_diag = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    possible_rows = num_of_rows - len(word) + 1
    possible_cols = num_of_cols - len(word) + 1

    for row in range(possible_rows):
        for col in range(possible_cols):
            if word_search[row][col] == word[0]:
                next_col = col
                counter = 0
                for curr_row in range(row, row + len(word)):
                    if curr_row == row:
                        counter += 1
                    elif word_search[curr_row][next_col + 1] == word[counter]:
                        next_col += 1
                        counter += 1
                        ending_point_init = curr_row
                        ending_point_close = next_col
                    else:
                        break
                if counter == len(word):
                    is_diag = True
                    starting_point_init = row
                    starting_point_close = col
                    break
        if is_diag:
            break
    if is_diag:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_diag

def is_diag_word_left(word_search: list, word: str, num_of_rows: int, num_of_cols: int):
    is_diag = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    possible_rows = num_of_rows - len(word) + 1
    possible_cols = len(word) - 2

    for row in range(possible_rows):
        for col in range(num_of_cols - 1, possible_cols, -1):
            if word_search[row][col] == word[0]:
                counter = 0
                next_col = col
                for curr_row in range(row, row + len(word)):
                    if curr_row == row:
                        counter += 1
                    elif word_search[curr_row][next_col - 1] == word[counter]:
                        next_col -= 1
                        counter += 1
                        ending_point_init = curr_row
                        ending_point_close = next_col
                    else:
                        break
                if counter == len(word):
                    is_diag = True
                    starting_point_init = row
                    starting_point_close = col
                    break
        if is_diag:
            break
    if is_diag:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_diag

def is_reverse_forward_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_rev_forward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    word_length = len(word)
    possible_cols = word_length - 2
    current_col = 0

    for row in range(num_of_rows):
        for col in range(num_of_cols - 1, possible_cols, -1):
            if word_search[row][col] == word[0]:
                counter = 0
                for curr_col in range(col, col - word_length, -1):
                    if word_search[row][curr_col] == word[counter]:
                        counter += 1
                        current_col = curr_col
                    else:
                        break
                if counter == word_length:
                    is_rev_forward = True
                    starting_point_init = row
                    starting_point_close = col
                    ending_point_init = row
                    ending_point_close = current_col
                    break
        if is_rev_forward:
            break
    if is_rev_forward:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_rev_forward

def is_reverse_downward_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_rev_downward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    possible_rows = len(word) - 2
    current_row = 0

    for row in range(num_of_rows - 1, possible_rows, -1):
        for col in range(num_of_cols):
            if word_search[row][col] == word[0]:
                counter = 0
                for curr_row in range(row, row - len(word), -1):
                    if word_search[curr_row][col] == word[counter]:
                        counter += 1
                        current_row = curr_row
                    else:
                        break
                if counter == len(word):
                    is_rev_downward = True
                    starting_point_init = row
                    starting_point_close = col
                    ending_point_init = current_row
                    ending_point_close = col
                    break
        if is_rev_downward:
            break
    if is_rev_downward:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_rev_downward

def is_reverse_diag_word_left(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_rev_diag = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    possible_cols = len(word) - 2
    possible_rows = len(word) - 2

    for row in range(num_of_rows - 1, possible_rows, -1):
        for col in range(num_of_cols - 1, possible_cols, -1):
            if word_search[row][col] == word[0]:
                next_col = col
                counter = 0
                for curr_row in range(row, row - len(word), -1):
                    if curr_row == row:
                        counter += 1
                    elif word_search[curr_row][next_col - 1] == word[counter]:
                        next_col -= 1
                        counter +=1
                        ending_point_init = curr_row
                        ending_point_close = next_col
                    else:
                        break
                if counter == len(word):
                    is_rev_diag = True
                    starting_point_init = row
                    starting_point_close = col
                    break
        if is_rev_diag:
            break
    if is_rev_diag:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_rev_diag

def is_reverse_diag_word_right(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_rev_diag = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0
    possible_rows = len(word) - 2
    possible_cols = num_of_cols - len(word) + 1

    for row in range(num_of_rows - 1, possible_rows, -1):
        for col in range(possible_cols):
            if word_search[row][col] == word[0]:
                counter = 0
                next_col = col
                for curr_row in range(row, row - len(word), -1):
                    if curr_row == row:
                        counter += 1
                    elif word_search[curr_row][next_col + 1] == word[counter]:
                        next_col += 1
                        counter += 1
                        ending_point_init = curr_row
                        ending_point_close = next_col
                    else:
                        break
                if counter == len(word):
                    is_rev_diag = True
                    starting_point_init = row
                    starting_point_close = col
                    break
        if is_rev_diag:
            break
    if is_rev_diag:
        print(word + " starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_rev_diag

if __name__ == "__main__":
    main()