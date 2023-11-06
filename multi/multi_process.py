import logging
import multiprocessing
import time

import concurrent.futures


logging.basicConfig(
    level=logging.DEBUG,
    format="%(processName)s: %(message)s")

def worker1(x, y):
    logging.debug("start")
    time.sleep(3)
    logging.debug("end")
    return x * y

def f(num, arr):
    logging.debug(num)
    num.value += 1.0
    logging.debug(arr)
    for i in range(len(arr)):
        arr[i] *= 2

def worker2(l, d):
    l.reverse()
    d["x"] += 1


if __name__ == "__main__":

    with concurrent.futures.ProcessPoolExecutor() as process:
        p1 = process.submit(worker1, 10, 10)
        p2 = process.submit(worker1, 20, 20)
        logging.debug(p1.result())
        logging.debug(p2.result())

    #with concurrent.futures.ProcessPoolExecutor(max_workers=1) as process:
    #    args = [[1,2],[10,10]]
    #    r = process.map(worker1, *args)
    #    logging.debug([i for i in r])

    #with multiprocessing.Manager() as manager:
    #    l = manager.list()
    #    d = manager.dict()
    #    l.append(1)
    #    l.append(2)
    #    l.append(3)
    #    d["x"] = 0
    #    p1 = multiprocessing.Process(target=worker2, args=(l, d))
    #    p2 = multiprocessing.Process(target=worker2, args=(l, d))
    #    p1.start()
    #    p2.start()
    #    p1.join()
    #    p2.join()
    #    logging.debug(l)
    #    logging.debug(d)

    #processのmemoryの共有
    #num = multiprocessing.Value("f", 0.0)
    #arr = multiprocessing.Array("f", [1,2,3,4,5])
    #p1 = multiprocessing.Process(target=f, args=(num, arr))
    #p2 = multiprocessing.Process(target=f, args=(num, arr))
    #p1.start()
    #p2.start()
    #p1.join()
    #p2.join()
    #logging.debug(num.value)
    #logging.debug(arr[:])

    #with multiprocessing.Pool(100) as p:
    #    r = p.map_async(worker1, [100,200])
    #    logging.debug("executed")
    #    logging.debug(r.get())
    #print(multiprocessing.cpu_count())


    #with multiprocessing.Pool(3) as p:
    #    p_syn = p.apply(worker1, (200,))
    #    logging.debug("executed apply")
    #    p1 = p.apply_async(worker1, (100,))
    #    p2 = p.apply_async(worker1, (100,))
    #    logging.debug("executed")
    #    logging.debug(p1.get())
    #    logging.debug(p2.get())

    #i = 10
    #t1 = multiprocessing.Process(target=worker1, args=(i,), name="rename process1")
    #t1.daemon = True
    #t2 = multiprocessing.Process(target=worker2, args=(i,), name="rename process2")
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()


