
# [aaaa, abaa, baaa] sequence -> len = 3
# [[a, b], [b, a], [a], [a]] '[ab]'
import numpy as np;


def find_regex(sequence):
    regex = []
    for i in range(len(sequence)):
        for j in range(len(sequence[i])):
            if len(regex) > j:
                if not np.isin(sequence[i][j], regex[j]):
                    regex[j].append(sequence[i][j])
            else:
                regex.append([sequence[i][j]])

    str = ''
    for i in range(len(regex)):
        curr_sequence = '['
        if len(regex[i]) > 1:
            for j in range(len(regex[i])):
                curr_sequence += '{}'.format(regex[i][j])
            curr_sequence += ']'
            str += curr_sequence
        else:
            str += regex[i][0]

    return str

print(find_regex(['aaaa', 'abaa', 'baaa']))
