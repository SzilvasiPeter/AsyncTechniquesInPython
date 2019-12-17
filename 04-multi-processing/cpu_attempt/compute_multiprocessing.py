import datetime
import math
import multiprocessing


def main():
    do_math(1)

    t0 = datetime.datetime.now()

    print("Doing math on {} processor".format(multiprocessing.cpu_count()))

    processor_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool()
    tasks = []
    for n in range(1, processor_count + 1):
        task = pool.apply_async(do_math, (30_000_000 * (n - 1) / processor_count,
                                   30_000_000 * n / processor_count))

        tasks.append(task)

    pool.close()
    pool.join()
    print("Our result: ")
    for t in tasks:
        print(t.get())

    dt = datetime.datetime.now() - t0
    print("Done in {:,.2f} sec.".format(dt.total_seconds()))


def do_math(start=0, num=10) -> int:
    pos = start
    k_sq = 1000 * 1000
    sum = 0
    while pos < num:
        pos += 1
        value = math.sqrt((pos - k_sq) * (pos - k_sq))
        sum += value

    avarage = sum / num
    return int(avarage)


if __name__ == '__main__':
    main()
