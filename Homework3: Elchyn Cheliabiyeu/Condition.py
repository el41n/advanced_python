import threading


def print_number(number, conditions):
    mutex_pos = number
    while number <= 100:
        with conditions[mutex_pos]:
            conditions[mutex_pos].wait()
            print(number)
            number += 5
            if mutex_pos == len(conditions) - 1:
                with conditions[0]:
                    conditions[0].notify()
            else:
                with conditions[mutex_pos + 1]:
                    conditions[mutex_pos + 1].notify()


if __name__ == '__main__':
    conditions = [threading.Condition() for _ in range(5)]
    # for condition in conditions:
    #     condition.acquire()
    threads = [threading.Thread(name='Thread {}'.format(num),
                                target=print_number, args=(num, conditions))
               for num in range(5)]
    for thread in threads:
        thread.start()
    with conditions[0]:
        conditions[0].notify()
    for thread in threads:
        thread.join()
