#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hung-sheng liao
#
# Created:     24/05/2014
# Copyright:   (c) Xli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
from itertools import product
import copy
sorted_words = {}
output_str = []
def combinations(target,data):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        sorted_jumble = ''.join(sorted(new_target))
        if sorted_jumble in sorted_words:
            if ", ".join(sorted_words[sorted_jumble]) not in output_str:
                output_str.append(", ".join(sorted_words[sorted_jumble]))

        combinations(new_target,new_data)

def jumble():
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "12dicts-5.0\\5desk.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        for word in f:
            word = word.strip()
            sorted_word = ''.join(sorted(word))
            sorted_words.setdefault(sorted_word,[]).append(word)

    while 1:
        input = raw_input("Enter a jumble to decode or 'exit': ")
        if input == 'exit':
            return
        target = []
        data = ['a','b','c','d']
        combinations([], input)
        print(', '.join(output_str))




if __name__ == '__main__':
    jumble()
