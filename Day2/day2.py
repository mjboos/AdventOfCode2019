import numpy as np

def load_input():
    with open('input.txt', 'r') as fl:
        codes = fl.read().split(',')
    return [int(code) for code in codes]

def process_input(codes):
    codes = [c for c in codes]
    curr_pos = 0
    while codes[curr_pos] != 99:
        if codes[curr_pos] == 1:
            codes[codes[curr_pos+3]] = codes[codes[curr_pos+1]] + codes[codes[curr_pos+2]]
        elif codes[curr_pos] == 2:
            codes[codes[curr_pos+3]] = codes[codes[curr_pos+1]] * codes[codes[curr_pos+2]]
        curr_pos += 4
    return codes

testcases = [[[1,0,0,0,99], [2,0,0,0,99]],
        [[2,3,0,3,99],[2,3,0,6,99]],
        [[2,4,4,5,99,0], [2,4,4,5,99,9801]],
        [[1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]]]

if __name__=='__main__':
    codes = load_input()
    for case in testcases:
        assert process_input(case[0]) == case[1]
    codes[1] = 12
    codes[2] = 2
    codes_proc = process_input(codes)
    print(codes_proc[0])
    for code_one in range(100):
        for code_two in range(100):
            codes[1] = code_one
            codes[2] = code_two
            if process_input(codes)[0] == 19690720:
                print(100*code_one + code_two)
                break
        else:
            continue
        break
