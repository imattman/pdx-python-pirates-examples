#!/usr/bin/env python3

import re
import time
from tqdm import tqdm

LEXICON = 'sowpods.txt'
TEST_FILE = 'shakespeare.txt'
NEW_WORDS_FILE = 'new-words.txt'

# Change below to see a big difference in execution speed
CONVERT_TO_SET = False


def time_execution(func):
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f">>> Time to execute: {end - start:.2f} sec\n")
        return result
    return timed


@time_execution
def read_words(filename, label='file'):
    print("reading {}... ".format(label), end='', flush=True)
    with open(filename) as fin:
        words = []
        for line in fin:
            # do some basic clean up - convert any non word characters to spaces
            line = re.sub(r'[^\w]', ' ', line)
            for word in line.split():
                word = word.lower().strip()
                # ignore empty strings and any values that start with a digit
                if not word or re.search(r'^\d+', word):
                    continue
                words.append(word)
    print()
    print("word count: {}".format(len(words)))
    return words


@time_execution
def find_new_words(source, lexicon, label='source', progress_dots=False):
    print("processing {} against lexicon... ".format(label), flush=True)

    new_words = set()
    for word in tqdm(source):
        if (word not in new_words) and (word not in lexicon):
            new_words.add(word)
            if progress_dots and len(new_words) % 20 == 0:
                print('.', end='', flush=True)

    if progress_dots:
        print()

    return new_words


def main():
    literature = read_words(TEST_FILE, label=TEST_FILE)

    lexicon = read_words(LEXICON, label="lexicon")

    if CONVERT_TO_SET:
        lexicon = set(lexicon)

    unfamiliar = find_new_words(literature, lexicon, TEST_FILE, False)
    unfamiliar = sorted(list(unfamiliar))

    print("Unfamiliar words not found in lexicon: {}".format(len(unfamiliar)))
    # print("Examples:\n  " + '\n  '.join(unfamiliar[:20]))

    with open(NEW_WORDS_FILE, 'w') as fout:
        for w in unfamiliar:
            print(w, file=fout)
    print("List written to '{}'".format(NEW_WORDS_FILE))


if __name__ == "__main__":
    main()
