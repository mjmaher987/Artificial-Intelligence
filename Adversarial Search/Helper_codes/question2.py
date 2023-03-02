import os

BASE_PATH = '.'
INPUTS_PATH = f'{BASE_PATH}/Inputs'
OUTPUT_PATH = f'{BASE_PATH}/Outputs'


def get_all_tests(prefix):
    test_files = [f for f in os.listdir(INPUTS_PATH) if os.path.isfile(os.path.join(INPUTS_PATH, f))]
    return list(filter(lambda f: f.startswith(prefix), test_files))


def scan_test_input(test):
    with open(f'{INPUTS_PATH}/{test}', 'r') as f:
        test_lines = f.readlines()[::-1]
    
    n, m = map(int, test_lines.pop().split())
    m_next_lines = [list(map(int, test_lines.pop().split())) for _ in range(m)]
    e = int(test_lines.pop())
    next_e_lines = [list(map(int, test_lines.pop().split())) for _ in range(e)]

    return n, m, m_next_lines, e, next_e_lines


def _clean_result(result):
    return ' '.join(map(str, result)) if result != 'NO' and ' ' not in result else result


def is_result_valid(test: str, result: str):
    with open(f'{OUTPUT_PATH}/{test.replace("in", "out")}', 'r') as f:
        possible_outcomes = map(str.strip, f.readlines())
    return _clean_result(result) in possible_outcomes
