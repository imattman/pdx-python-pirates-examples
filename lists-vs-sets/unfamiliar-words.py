#!/usr/bin/env python3

import re
import time

LEXICON = 'sowpods.txt'
LITERATURE = 'shakespeare.txt'
UNFAMILIAR = 'new-words.txt'


def time_execution(fn):
    def timed(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(">>> Time to execute: {}\n".format(end - start))
        return result
    return timed


@time_execution
def read_words(filename, label='file'):
    print("reading {}... ".format(label), end='', flush=True)
    with open(filename) as fin:
        words = []
        for line in fin:
            line = re.sub(r'[,;:?!()\[\]#*$&"\'_.-]', '', line)
            for word in line.split():
                word = word.lower().strip()
                if not word or re.search(r'^\d+', word):
                    continue
                words.append(word)
    print()
    return words


@time_execution
def find_new_words(source, lexicon, label='source', progress=False):
    print("processing {} against lexicon... ".format(label), end='', flush=True)
    new_words = set()

    for word in source:
        if (word not in new_words) and (word not in lexicon):
            new_words.add(word)
            if progress and len(new_words) % 20 == 0:
                print('.', end='', flush=True)

    print()
    return new_words


@time_execution
def main():
    lexicon = read_words(LEXICON, label="lexicon")
    lexicon = set(lexicon)
    literature = read_words(LITERATURE, label=LITERATURE)

    unfamiliar = find_new_words(literature, lexicon, 'words', True)
    unfamiliar = sorted(list(unfamiliar))

    print("Unfamiliar words: {}".format(len(unfamiliar)))
    # print("Examples:\n  " + '\n  '.join(unfamiliar[:20]))

    with open(UNFAMILIAR, 'w') as fout:
        for w in unfamiliar:
            print(w, file=fout)


if __name__ == "__main__":
    main()
