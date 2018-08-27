import sys
import os
import argparse
import collections


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', help='Path to file')
    parser.add_argument(
        '-count',
        default=10,
        help='Count of most frequent words'
    )
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
    words_counter = collections.Counter(all_words_list)
    return words_counter.most_common(most_frequent_count)


def print_most_frequent_words(words_list):
    print('List of most frequent words:')
    for word in words_list:
        print(word)


if __name__ == '__main__':

    parser = create_arg_parser()
    args = parser.parse_args()
    filepath = os.path.abspath(args.file)
    try:
        most_frequent_count = int(args.count)
    except ValueError:
        sys.exit("Parameter 'count' must be integer.")

    text = load_data(filepath)
    if text is None:
        sys.exit('File not found.')
    if not text:
        sys.exit('File is empty.')

    most_frequent_words = get_most_frequent_words(
        text,
        most_frequent_count
    )
    print_most_frequent_words(most_frequent_words)
