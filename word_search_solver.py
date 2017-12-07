

def main():
    file_name = get_file_name()

    rowsi_colsi_wsl_wordsl = parse_file(file_name)

    num_of_rows = rowsi_colsi_wsl_wordsl[0]
    num_of_cols = rowsi_colsi_wsl_wordsl[1]
    word_search = rowsi_colsi_wsl_wordsl[2]
    words_to_search = rowsi_colsi_wsl_wordsl[3]

    


def get_file_name()->str:
    file_name = input("Enter the name of the file that contains the word search: ")

    return file_name

def parse_file(file_name) -> list:
    rowsi_colsi_wsl_wordsl = []
    counter = 1

    with open(file_name, 'r') as myfile:

        data = myfile.readline()
        rows_and_cols = data.split(" ")

        rowsi_colsi_wsl_wordsl.append()

        return rowsi_colsi_wsl_wordsl






if __name__ == "__main__":
    main()