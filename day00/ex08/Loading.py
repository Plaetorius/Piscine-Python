import time
import os


def format_time(seconds: int) -> str:
    '''Returns a formatted string displaying the numbers of hours, minutes and
    seconds that the seconds passed as a parameter represent.

    Parameters:
    seconds (int): the time (in seconds) to format

    Returns:
    A formatted string:
    - HH...HH:MM:SS if time is bigger than 59min and 59s
    - MM:SS else
    '''
    hours = int(seconds / 3600)
    seconds -= hours * 3600
    minutes = int(seconds / 60)
    seconds -= minutes * 60
    if hours:
        return f"{hours}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    return f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


def format_iterations(delta_t: float) -> str:
    '''Returns a string with 2 decimals-precision of the number of iterations
    of the loop per second.

    Parameters:
    delta_t (float): the time elapsed during one iteration

    Returns:
    A string, '?' if delta_t is 0 (no iteration has been made yet), or 2
    decimals-precision of the number of iterations of the loop per second.
    '''
    if delta_t == 0:
        return '?'
    iterations = 1.0 / delta_t
    return f"{iterations:.2f}"


def format_display(data: dict) -> str:
    '''Formats the data ditionary to create the loading bar

    Parameters:
    data (dict): the data to the processed to fill the loading bar

    Returns:
    A string containing the loading bar, ready to print printed.
    '''
    data['time_elapsed'] = format_time(int((time.time() - data['start_time'])))
    data['iterations'] = format_iterations(data['delta_t'])
    if data['iterations'] != '?':
        data['time_remaining'] = format_time(int((data['items_tot'] -
                                                  data['items_done']) /
                                                 int(float(data['iterations']))
                                                 ))
    else:
        data['time_remaining'] = '?'
    data['adv'] = int((float(data['items_done']) /
                      float(data['items_tot'])) * 100)
    len_elems = len(
        str(data['adv']) +
        str(data['items_done']) +
        str(data['items_tot']) +
        data['time_elapsed'] +
        data['time_remaining'] +
        str(data['iterations'])
        ) + 15  # for the extra characters: %, [], spaces...
    len_to_fill = os.get_terminal_size().columns - len_elems
    len_compl = int((len_to_fill * data['items_done']) / data['items_tot'])
    len_space = len_to_fill - len_compl

    return (f"\r{data['adv']}%"
            f"|{'█' * len_compl}{' ' * len_space}| "
            f"{data['items_done']}/{data['items_tot']} "
            f"[{data['time_elapsed']}<{data['time_remaining']}, "
            f"{data['iterations']}it/s]")


def ft_tqdm(lst: range) -> None:
    '''Prints a loading bar in the terminal, visually showing the advancement
    in the range iteration.

    Parameters:
    lst (range): a range of items to go through

    Returns:
    None
    '''

    if ((lst.start > lst.stop and lst.step > 0)
            or (lst.start < lst.stop and lst.step < 0)):
        print("0it [00:00, ?it/s]")
        return

    data = {
        'start_time': time.time(),
        'items_tot': len(lst),
        'items_done': 0,
        'delta_t': 0,
        'adv': 0,
        'time_elapsed': '00:00',
        'time_remaining': '00:00',
        'iterations': 0.0,
    }

    for items_done in range(data['items_tot']):
        start_it = time.time()
        print(format_display(data), end="")
        yield lst[items_done]
        data['items_done'] += 1
        data['delta_t'] = time.time() - start_it

    print(format_display(data))
