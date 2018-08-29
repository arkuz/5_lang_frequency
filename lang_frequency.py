import sys
import os
import argparse
import collections
import re


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', help='Path to file')
    parser.add_argument(
        '-count',
        default=10,
        type=int,
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
    lower_text = text.lower()
    words_list = re.findall('\w+', lower_text)
    words_counter = collections.Counter(words_list)
    return words_counter.most_common(most_frequent_count)


def print_most_frequent_words(most_frequent_words):
    print('List of most frequent words:')
    for word, count in most_frequent_words:
        print('  {0} - {1}'.format(
            word,
            count,
        ))


if __name__ == '__main__':

    parser = create_arg_parser()
    args = parser.parse_args()
    filepath = os.path.abspath(args.file)
    most_frequent_count = args.count

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
