import time
import random

def main():
    print(time.time())
    print(time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())))

    randomTime = random.randint(2,8)
    print('休眠时长：', randomTime)

    timeFilename = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())) + '-' + str(randomTime)

    print(timeFilename)

if __name__ == '__main__':
    main()