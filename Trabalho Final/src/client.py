#client.py

from proxy import Proxy
import time

if __name__ == '__main__':
    proxy = Proxy(('localhost', 8080))

    # Example method calls
    result_eat = proxy.eat("banana", "juice")
    print("Result of eat method:", result_eat)
    time.sleep(1)

    result_play = proxy.play("fetch", "s")
    print("Result of play method:", result_play)
    time.sleep(1)

    result_sleep = proxy.sleep("8", "s")
    print("Result of sleep method:", result_sleep)
    time.sleep(1)

    result_eat = proxy.eat("banana", "juice")
    print("Result of eat method:", result_eat)
    time.sleep(1)

    result_play = proxy.play("fetch", "s")
    print("Result of play method:", result_play)
    time.sleep(1)

    result_sleep = proxy.sleep("8", "s")
    print("Result of sleep method:", result_sleep)
    time.sleep(1)

