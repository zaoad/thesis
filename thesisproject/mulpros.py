import os
from multiprocessing import Process, current_process
import multiprocessing
from time import time

class a:
    a=100
    def __init__(self,a):
        self.a=a
class b:
    b=50
    def __init__(self,b):
        self.b=b
def square(st, end):
    stime=time()
    for i in range(end - st):
        a = i + st;
        for i in range(100):
            b=2
        #time.sleep(.01)
        result = a * a;
        #print(result)
    #process_id= os.getpid()
    etime=time()
    print('time',etime-stime)

def squaree(a,b,return_dict,return_list):
    print('call',a.a,b.b)
    print(a.a+b.b)
    return_dict[0]=(a.a+b.b)
    return_list.append(100)

if __name__ == '__main__':
    print(multiprocessing.cpu_count())
    st = time()
    processes = []

    process1 = Process(target=square, args=(0, 400000,))
    process2 = Process(target=square, args=(0, 400000,))
    process3 = Process(target=square, args=(0, 400000,))
    # process4 = Process(target=square, args=(1201, 1600,))
    # process5 = Process(target=square, args=(1601, 2000,))
    # process6 = Process(target=square, args=(2001, 2400,))
    # process7 = Process(target=square, args=(2401, 2800,))
    # process8 = Process(target=square, args=(2801, 3200,))
    # process9 = Process(target=square, args=(3201, 3600,))
    # process10 = Process(target=square, args=(3601,4000,))
    # process11 = Process(target=square, args=(0, 400,))
    # process12 = Process(target=square, args=(401, 800,))
    # process13 = Process(target=square, args=(801, 1200,))
    # process14 = Process(target=square, args=(1201, 1600,))
    # process15 = Process(target=square, args=(1601, 2000,))
    # process16 = Process(target=square, args=(2001, 2400,))
    # process17 = Process(target=square, args=(2401, 2800,))
    # process18 = Process(target=square, args=(2801, 3200,))
    # process19 = Process(target=square, args=(3201, 3600,))
    # process20 = Process(target=square, args=(3601, 4000,))
    # process31 = Process(target=square, args=(0, 400,))
    # process32 = Process(target=square, args=(401, 800,))
    # process33 = Process(target=square, args=(801, 1200,))
    # process34= Process(target=square, args=(1201, 1600,))
    # process35 = Process(target=square, args=(1601, 2000,))
    # process36 = Process(target=square, args=(2001, 2400,))
    # process37 = Process(target=square, args=(2401, 2800,))
    # process38 = Process(target=square, args=(2801, 3200,))
    # process39 = Process(target=square, args=(3201, 3600,))
    # process110 = Process(target=square, args=(3601, 4000,))
    # process111 = Process(target=square, args=(0, 400,))
    # process112 = Process(target=square, args=(401, 800,))
    # process113 = Process(target=square, args=(801, 1200,))
    # process114 = Process(target=square, args=(1201, 1600,))
    # process115 = Process(target=square, args=(1601, 2000,))
    # process116 = Process(target=square, args=(2001, 2400,))
    # process117 = Process(target=square, args=(2401, 2800,))
    # process118 = Process(target=square, args=(2801, 3200,))
    # process119 = Process(target=square, args=(3201, 3600,))
    # process120 = Process(target=square, args=(3601, 4000,))
    # # processes.append(process)

    process1.start()
    process2.start()

    process3.start()
    # process4.start()
    # process5.start()
    # process6.start()
    #
    # process7.start()
    # process8.start()
    # process9.start()
    # process10.start()
    # process11.start()
    # process12.start()
    #
    # process13.start()
    # process14.start()
    # process15.start()
    # process16.start()
    #
    # process17.start()
    # process18.start()
    # process19.start()
    # process20.start()
    # process31.start()
    # process32.start()
    #
    # process33.start()
    # process34.start()
    # process35.start()
    # process36.start()
    #
    # process37.start()
    # process38.start()
    # process39.start()
    # process110.start()
    # process111.start()
    # process112.start()
    #
    # process113.start()
    # process114.start()
    # process115.start()
    # process116.start()
    #
    # process117.start()
    # process118.start()
    # process119.start()
    # process120.start()

    process1.join()
    process2.join()
    process3.join()
    # process4.join()
    # process5.join()
    # process6.join()
    # process7.join()
    # process8.join()
    # process9.join()
    # process10.join()
    # process11.join()
    # process12.join()
    # process13.join()
    # process14.join()
    # process15.join()
    # process16.join()
    # process17.join()
    # process18.join()
    # process19.join()
    # process20.join()
    # process31.join()
    # process32.join()
    # process33.join()
    # process34.join()
    # process35.join()
    # process36.join()
    # process37.join()
    # process38.join()
    # process39.join()
    # process110.join()
    # process111.join()
    # process112.join()
    # process113.join()
    # process114.join()
    # process115.join()
    # process116.join()
    # process117.join()
    # process118.join()
    # process119.join()
    # process120.join()
    et = time()
    totaltime = et - st
    print(totaltime)
    '''
    manager = multiprocessing.Manager()
    return_dict= manager.dict()
    return_list=manager.list()
    processes = []
    x=a(10)
    y=b(20)
    c=[]
    process1 = Process(target=squaree, args=(x, y, return_dict,return_list ))
    process1.start()
    process1.join()
    for i in return_dict:
        print(i)
    print ('ac', return_dict,return_list ,len(return_list))
    '''