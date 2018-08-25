import sys
import os
import argparse
import collections


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help='Path to file')
    return parser

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
            return None


def get_most_frequent_words(text, most_frequent_count):
    all_words_list = []
    strings_list = text.split('\n')
    for _string in strings_list:
        lower_string = _string.lower()
        words_list = lower_string.split(' ')
        all_words_list.extend(words_list)
    col_counter = collections.Counter(all_words_list)
    return col_counter.most_common(most_frequent_count)


def print_most_frequent_words(words_list):
    print('List of most frequent words:')
    for item in words_list:
        print(item)


if __name__ == '__main__':

    parser = create_arg_parser()
    args = parser.parse_args()
    filepath = os.path.abspath(args.file)

    data_object = load_data(filepath)
    if data_object is None:
        sys.exit('File not found.')
    if not data_object:
        sys.exit('File is empty.')

    most_frequent_words = get_most_frequent_words(data_object, 10)
    print_most_frequent_words(most_frequent_words)

