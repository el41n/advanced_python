import threading
import time


if __name__ == '__main__':
    for num_begin in range(0, 100, 5):
        threads = [threading.Thread(name='Thread {}'.format(num),
                                    target=lambda x: print(x), args=(num,))
                   for num in range(num_begin, num_begin + 5)]
        timers = [threading.Timer(timer, thread.start)
                  for timer, thread in enumerate(threads)]
        for timer in timers:
            timer.start()
        time.sleep(5)
