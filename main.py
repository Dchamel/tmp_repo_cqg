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
        print(line[1])


# @working_time_prec(6)  # for dev only
def string_handler(rules_list: list[str], data_list: list[str]) -> list[[int, str]]:
    """
    Strings handler.
    Takes rules list: list[str] and data_list: list[str]
    And changes data according to their rules
    Output: list of operated & sorted strings by desc and quantity of changes
    p.s Works with small files
    """

    outer_data = tuple()
    for i, data_line in enumerate(data_list):
        no_of_changes = 0
        for rule in rules_list:
            value_to_replace, value_for_replace = rule.split('=')
            no_of_changes += data_line.count(value_to_replace)
            data_line = data_line.replace(value_to_replace, value_for_replace)
        outer_data += ([no_of_changes, data_line],)
    # sorting by descending from the most changed line
    outer_data = sorted(outer_data, key=lambda x: x, reverse=True)
    return outer_data


def open_files(rules_cfg: str, data_txt: str) -> tuple[list[str], list[str]]:
    """
    Function for reading data from files
    Input: Path to the files as strings
    Output: tuple of lists with data from files
    p.s Works with small files
    """
    with open(rules_cfg, 'r') as f:
        rules_list = f.read().splitlines()

    with open(data_txt, 'r') as f:
        data_list = f.read().splitlines()

    return data_list, rules_list


def start_processing() -> None:
    """Start processing of the file"""

    # for dev only
    # data_list, rules_list = open_files('rules.cfg', 'text.txt')
    # data_final = string_handler(rules_list, data_list)
    # data_console_output(data_final)

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
