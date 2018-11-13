from threading import Thread

import subprocess as sp
import time

class Printer(Thread):
    def __init__(self, receiver):
        super().__init__()
        self.receiver = receiver
        self.t = 0

    def run(self):
        while self.receiver.is_alive():
            self.t += 1
            if self.receiver.msg == 't':
                print(self.t)
                self.receiver.msg = ''
            else:
                print('waiting ...')
            time.sleep(0.5)

class Receiver(Thread):
    def __init__(self):
        super().__init__()
        self.msg = ''

    def run(self):
        while self.msg != 'q':
            self.msg = input('enter msg: ')

def main():
    rec = Receiver()
    rec.start()
    time.sleep(1)
    prt = Printer(rec)
    prt.start()
    rec.join()
    prt.join()

if __name__ == '__main__':
    main()
