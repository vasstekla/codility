def solution(A):
    dictionary = { i : 0 for i in A }
    for element in A:
        dictionary[element] += 1
    for key, value in dictionary.items():
        if (value % 2 != 0):
            return key