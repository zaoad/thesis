import time

if __name__ == '__main__':
    st = time.time()
    for number in range(4004):
        for i in range(100):
            a=2
        result = number * number
        print(result)
    for number in range(4004):
        for i in range(100):
            a=2
        result = number * number
        print(result)
    et = time.time()
    total_time = et - st
    print(total_time)
