#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:55:30 2022

@author: juan
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:06:13 2022

@author: juan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:49:20 2022

@author: juan
"""
from multiprocessing import Process, Lock ,BoundedSemaphore
from multiprocessing import current_process
from multiprocessing import Value, Array
N = 8
def task(common, tid, turn, lock):
    a = 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section')
        while turn.value!=tid:
            pass
        lock.acquire()
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1
        print(f'{tid}−{i}: Inside critical section')
        common.value = v
        print(f'{tid}−{i}: End of critical section')
        turn.value = (tid + 1) % N
        lock.release()

def main():
    lp = []
    common = Value('i', 0)
    turn = Value('i', 0)
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, turn,lock )))
        print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    for p in lp:
        p.join()

    print (f"Valor final del contador {common.value}")
    print ("fin")
if __name__ == "__main__":
        lock = BoundedSemaphore(1)
        main()
