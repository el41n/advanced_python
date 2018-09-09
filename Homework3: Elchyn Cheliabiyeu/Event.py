import threading


def print_number(number, event, next_event):
    while number <= 100:
        event.wait()
        event.clear()
        print(number)
        number += 5
        next_event.set()


if __name__ == '__main__':
    events = [threading.Event() for _ in range(5)]
    next_events = events[1:] + events[:1]
    threads = [threading.Thread(target=print_number, args=(num, event, next_event))
               for num, (event, next_event) in enumerate(zip(events, next_events))]
    for thread in threads:
        thread.start()
    events[0].set()
    for thread in threads:
        thread.join()
