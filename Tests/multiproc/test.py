from multiprocessing import Process


def count(name, num):
    i = 0
    while i < num:
        print name, i
        i += 1

def count1(name, num):
    i = 0
    while i < num:
        print name, i
        i += 1

if __name__ == '__main__':
    Process(target=count, args=('b',200)).start()
    Process(target=count1, args=('a',100)).start()
