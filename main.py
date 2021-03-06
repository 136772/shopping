import threading
import queue
import user
import core
import sys



exitFlag = 0
num = sys.argv[1]
if num == "":
    num = '320'
print(num)

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        # print("Starting " + self.name)
        process_data(self.name, self.q)
        # print("Exiting " + self.name)


def process_data(threadName, q):
    try:
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                # print("%s processing %s" % (threadName, data))
                # print(data)
                weikegu = core.Weikegu(str(data), num=num)


                flag, tmTel,err = weikegu.login()
                return user.savedata(flag, tmTel, err)
            else:
                queueLock.release()
    except Exception as e:
        print('不知道咋了',e)



threadList = [i for i in range(20)]
nameList = user.loaduser()
queueLock = threading.Lock()
workQueue = queue.Queue(20)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")
