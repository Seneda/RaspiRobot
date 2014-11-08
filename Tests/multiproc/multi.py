from multiprocessing import Process

def loop_a():
    a = 0
    while a < 100:
        print("a")

def loop_b():
    while 1:
        print("b")

if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()