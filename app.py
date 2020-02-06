
from sys import argv
from cleanWordInput import clean_word_from_spaces_commas


def main():
    arg_length = len(argv)
    if arg_length != 3:
        raise ValueError(
            "first arg should be path to text file and second verb or adj")

    path_to_file = argv[1]
    wantedGermanWordType = argv[2]

    with open(path_to_file) as f:
        for line in f:
            cleaned_word = clean_word_from_spaces_commas(line)
            print(cleaned_word)
            # put info into csv file
            # if error make new error file


if __name__ == "__main__":
    # execute only if run as a script
    main()
