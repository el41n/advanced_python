import multiprocessing
import sys


def print_num(num, step, syncronize):
    number = num
    while num <= 100:
        syncronize[number].acquire()
        print(num)
        sys.stdout.flush()
        num += step
        if number == len(syncronize) - 1:
            syncronize[0].release()
        else:
            syncronize[number + 1].release()


if __name__ == '__main__':
    syncronize = [multiprocessing.Lock() for _ in range(2)]
    for sync in syncronize:
        sync.acquire()
    p1 = multiprocessing.Process(name="Process 1", target=print_num,
                                 args=(0, 2, syncronize))
    p2 = multiprocessing.Process(name="Process 2", target=print_num,
                                 args=(1, 2, syncronize))
    p1.start()
    p2.start()
    syncronize[0].release()
    p1.join()
    p2.join()



