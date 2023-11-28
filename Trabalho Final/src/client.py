from proxy import Proxy

if __name__ == '__main__':
    proxy = Proxy(('localhost', 8080))

    # Example method calls
    result_eat = proxy.invoke_method("eat", "banana", "juice")
    print("Result of eat method:", result_eat)

    result_play = proxy.invoke_method("play", "fetch", "s")
    print("Result of play method:", result_play)

    result_sleep = proxy.invoke_method("sleep", "8", "s")
    print("Result of sleep method:", result_sleep)
