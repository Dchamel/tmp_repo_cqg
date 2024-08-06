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


@working_time_prec(4)  # for dev only
def string_handler(rules_cfg: str, data_txt: str) -> None:
    """
    Strings handler.
    Takes rules from first file data_cfg: str
    And changes data according to thr rules from second file data_txt: str
    Output to console
    p.s Works with small files
    """
    with open(rules_cfg, 'r') as f:
        rules_list = f.read().splitlines()

    with open(data_txt, 'r') as f:
        data_list = f.read().splitlines()

    for data_line in data_list:
        for rule in rules_list:
            value_to_replace = rule.split('=')[0]
            value_for_replace = rule.split('=')[1]

            data_line = data_line.replace(value_to_replace, value_for_replace)
        print(data_line)


@working_time_prec(4)  # for dev only
def main() -> None:
    """
    Main function of the file.
    Only for run other functions or main functional
    """

    # for dev only
    # string_handler('rules.cfg', 'text.txt')

    try:
        if not argv[1].endswith('.cfg') or not argv[2].endswith('.txt'):
            raise TypeError('Please input cfg as first file and txt as second file')

        string_handler(argv[1], argv[2])
    except IndexError:
        print('Please input 2 arguments(file names) after filename')


if __name__ == '__main__':
    main()
