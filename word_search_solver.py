

def main():
    file_name = get_file_name()

    rowsi_colsi_wsl_wordsl = parse_file(file_name)

    num_of_rows = rowsi_colsi_wsl_wordsl[0]
    num_of_cols = rowsi_colsi_wsl_wordsl[1]
    word_search = rowsi_colsi_wsl_wordsl[2]
    words_to_search = rowsi_colsi_wsl_wordsl[3]

    display_word_search(word_search, num_of_rows)
    find_words(num_of_rows, num_of_cols, word_search, words_to_search)

def get_file_name()->str:
    file_name = input("Enter the name of the file that contains the word search: ")
    #below is a test case
    file_name = "/Users/seancarnahan/PycharmProjects/ECS10/final_project/test.txt"

    return file_name

def parse_file(file_name) -> list:
    rowsi_colsi_wsl_wordsl = []
    word_search = []
    words_to_search = []
    counter = 1

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
                    new_row.append(letter)
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

        rowsi_colsi_wsl_wordsl.append(words_to_search)
        return rowsi_colsi_wsl_wordsl

def display_word_search(word_search, num_of_rows):
    for row in range(num_of_rows):
        print(word_search[row])

def find_words( num_of_rows, num_of_cols, word_search, words_to_search):
    for word in words_to_search:
        while True:
            if is_forward_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_downwards_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_diag_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_reverse_forward_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_reverse_downward_word(word_search, word, num_of_rows, num_of_cols):
                break
            elif is_reverse_diag_word(word_search, word, num_of_rows, num_of_cols):
                break
            else:
                print("______FAILURE___________")
                break



#the print statement should come from this
#BOBCAT starts at (2, 10) and ends at (7, 5)
def is_forward_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_forward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0

    if is_forward:
        print(word + "starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close )+ ")" )
    return is_forward

def is_downwards_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_downward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0

    if is_downward:
        print(word + "starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_downward

def is_diag_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int)-> bool:
    is_diag = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0

    if is_diag:
        print(word + "starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_diag

def is_reverse_forward_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_rev_forward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0

    if is_rev_forward:
        print(word + "starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_rev_forward

def is_reverse_downward_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_rev_downward = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0

    if is_rev_downward:
        print(word + "starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_rev_downward

def is_reverse_diag_word(word_search: list, word: str, num_of_rows: int, num_of_cols: int) -> bool:
    is_rev_diag = False
    starting_point_init = 0
    starting_point_close = 0
    ending_point_init = 0
    ending_point_close = 0

    if is_rev_diag:
        print(word + "starts at (" + str(starting_point_init) + ", " + str(starting_point_close) + ") and ends at (" + str(ending_point_init) + ", " + str(ending_point_close) + ")")
    return is_rev_diag






if __name__ == "__main__":
    main()