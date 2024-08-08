from time import perf_counter
from sys import argv


def working_time_prec(prec=2):
    def working_time(func):
        def wrapper(*args, **kwargs):
            t1 = perf_counter()
            ret = func(*args, **kwargs)
            t2 = perf_counter()
            print(f'Working time: {t2 - t1:.{prec}f} seconds. Function: {func.__name__}')
            return ret

        return wrapper

    return working_time


def data_console_output(data_final: list[str]) -> None:
    """Print list of the data to console string by string"""
    for line in data_final:
        print(line)


# @working_time_prec(6)  # for dev only
def string_handler(rules_list: list[str], data_list: list[str]) -> list[str]:
    """
    Strings handler.
    Takes rules list: list[str] and data_list: list[str]
    And changes data according to their rules
    Output: list of operated strings
    p.s Works with small files
    """
    data_final = []
    for data_line in data_list:
        for rule in rules_list:
            value_to_replace = rule.split('=')[0]
            value_for_replace = rule.split('=')[1]

            data_line = data_line.replace(value_to_replace, value_for_replace)
        data_final.append(data_line)

    return data_final


def open_files(rules_cfg: str, data_txt: str) -> tuple[list[str], list[str]]:
    with open(rules_cfg, 'r') as f:
        rules_list = f.read().splitlines()

    with open(data_txt, 'r') as f:
        data_list = f.read().splitlines()

    return data_list, rules_list


def start_processing() -> None:
    """Start processing of the file"""

    # for dev only
    # string_handler('rules.cfg', 'text.txt')

    try:
        if not argv[1].endswith('.cfg') or not argv[2].endswith('.txt'):
            raise TypeError('Please input cfg as first file and txt as second file')

        # get list data
        data_list, rules_list = open_files(argv[1], argv[2])
        # process list and output to console
        data_final = string_handler(rules_list, data_list)
        # output to console
        data_console_output(data_final)

    except IndexError:
        print('Please input 2 arguments(file names) after filename')


# @working_time_prec(5)  # for dev only
def main() -> None:
    """
    Main function of the file.
    Only for run other functions or main functional
    """

    start_processing()


if __name__ == '__main__':
    main()
