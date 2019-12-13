import time
import threading


def main():
    threads = [
        threading.Thread(target=greeter, args=("Peter", 10), daemon=True),
        threading.Thread(target=greeter, args=("Ellis", 5), daemon=True),
        threading.Thread(target=greeter, args=("Robert", 7), daemon=True),
        threading.Thread(target=greeter, args=("Sam", 4), daemon=True)
    ]

    [t.start() for t in threads]

    print("Do some other work.")
    print(2*2)

    [t.join(timeout=2) for t in threads]

    print("Done.")


def greeter(name: str, times: int):
    for n in range(0, times):
        print("{} Hello there {}".format(n, name))
        time.sleep(1)


if __name__ == '__main__':
    main()
