import logging
import threading
import time



logging.basicConfig(
    level=logging.DEBUG,
    format="%(threadName)s: %(message)s"
    )

def worker1(condition):
    with condition:
        condition.wait()
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")

def worker2(condition):
    with condition:
        condition.wait()
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")

def worker3(condition):
    with condition:
        logging.debug("start")
        time.sleep(3)
        logging.debug("end")
        condition.notify_all()



if __name__ == "__main__":
    
    t1 = threading.Thread(target=worker1, args=(condition,))
    t2 = threading.Thread(target=worker2, args=(condition,))
    t3 = threading.Thread(target=worker3, args=(condition,))
    t1.start()
    t2.start()
    t3.start()


    #eventとlockの機能を組み合わせたものがcondition
    #condition = threading.Condition()
    #t1 = threading.Thread(target=worker1, args=(condition,))
    #t2 = threading.Thread(target=worker2, args=(condition,))
    #t3 = threading.Thread(target=worker3, args=(condition,))
    #t1.start()
    #t2.start()
    #t3.start()

    #event.set()が実行されると、event.wait()で待機していた処理が走る
    #event = threading.Event()
    #t1 = threading.Thread(target=worker1, args=(event,))
    #t2 = threading.Thread(target=worker2, args=(event,))
    #t3 = threading.Thread(target=worker3, args=(event,))
    #t1.start()
    #t2.start()
    #t3.start()


    #threading.enumerate()に現在使っているスレッドの名前をリストで取得できる
    #for _ in range(5):
    #    t1 = threading.Thread(target=worker1)
    #    t1.start()
    #for thread in threading.enumerate():
    #    print(thread)

    #スレッドを何秒後に実行するかを決めれる
    #t = threading.Timer(3, worker1)
    #t.start()

    #Semaphoreを使うことで、Lockの使用可能スレッド数を指定することができる。Lockじゃなくて、Semaphoreでいい説
    #lock = threading.Semaphore(2)
    #t1 = threading.Thread(target=worker1, args=(lock,))
    #t2 = threading.Thread(target=worker2, args=(lock,))
    #t3 = threading.Thread(target=worker3, args=(lock,))
    #t1.start()
    #t2.start()
    #t3.start()
    #print("start")
