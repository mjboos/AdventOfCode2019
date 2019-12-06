import numpy as np

#six digit number
#two adjacent digits the same
#never decreases from left to right

start_range = 231832
stop_range = 767346

test_cases = [112233, 123444, 111122]

def combinations_left(code):
    '''Returns the combinations that are still valid given code'''
    pass

def is_valid_code_part2(code):
    diffs = code[1:] - code[:-1]
    sec_val = False
    if np.any(diffs == 0):
        diff_locs = np.where(diffs==0)[0]
        if len(diff_locs)==1 or (np.diff(diff_locs).max() > 1 and not np.all(np.diff(diff_locs)==np.array([1,2,1]))):
            sec_val = True
    return np.all(diffs >= 0) and sec_val

def is_valid_code(code):
    diffs = code[1:] - code[:-1]
    return np.all(diffs >= 0) and np.any(diffs == 0)

def get_first_cons_incr_code(code):
    code = code.copy()
    diffs = code[1:] - code[:-1]
    if np.all(diffs >= 0):
        return code
    else:
        min_diff = np.where(diffs<0)[0].min()
        code[min_diff+1:] = code[min_diff]
        return code

def get_last_cons_incr_code(code):
    code = code.copy()
    diffs = code[1:] - code[:-1]
    if np.all(diffs >= 0):
        return code
    else:
        min_diff = np.where(diffs<0)[0].min()
        min_diff = min(min_diff,np.where(code[:min_diff+1] == code[min_diff])[0].min())
        code[min_diff] -= 1
        code[min_diff+1:] = 9
        return code

def int_to_arr(int_code):
    return np.array([int(digit) for digit in str(int_code)])

def count_valid_codes(pre_code, post_code):
    counter = 0

    if len(post_code) == 1:
        codes = np.append(np.tile(pre_code[None], 10-post_code), np.arange(post_code, 10), axis=-1)
        return np.sum([is_valid_code(code) for code in codes])

    for i in range(post_code[0], 10):
        counter += count_valid_codes(np.append(pre_code,i), post_code[1:])
    return counter

def to_int(arr):
    return (arr*(10**np.arange(arr.shape[0])[::-1])).sum()

def generate_codes_in_range(start, stop, check_func):
    import tqdm
    start_code = get_first_cons_incr_code(start)
    stop_code = get_last_cons_incr_code(stop)
    counter = 0
    listi = []
    for code in tqdm.tqdm(range(to_int(start_code), to_int(stop_code)+1)):
        if check_func(int_to_arr(code)):
            counter += 1
            listi.append(code)
    return counter, listi

if __name__ == '__main__':
    #print(generate_codes_in_range(int_to_arr(start_range), int_to_arr(stop_range), is_valid_code))
    print(generate_codes_in_range(int_to_arr(start_range), int_to_arr(stop_range), is_valid_code_part2))
