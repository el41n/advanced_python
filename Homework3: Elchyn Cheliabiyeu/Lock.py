import threading


def print_number(number, mutexes):
    mutex_pos = number
    while number <= 100:
        mutexes[mutex_pos].acquire()
        print(number)
        number += 5
        if mutex_pos == len(mutexes) - 1:
            mutexes[0].release()
        else:
            mutexes[mutex_pos + 1].release()


if __name__ == '__main__':
    mutexes = [threading.Lock() for _ in range(5)]
    for mutex in mutexes:
        mutex.acquire()
    mutexes[0].release()
    threads = [threading.Thread(name='Thread {}'.format(num),
                                target=print_number, args=(num, mutexes))
               for num in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
