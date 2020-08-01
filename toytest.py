
from toymodels import *
from modal_functions import *

import time
start_time = time.time()

for i in K[21]:
    for j in K[21]:
        for f2 in toy2:
            for f3 in toy2:
                for f4 in toy2:
                    for f5 in toy2:
                        for f6 in toy2:
                            for f7 in toy2:
                                for f8 in toy2:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[21]:
                                        print(i[0], j[0], i[1], j[1], modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                              modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]), f2, f3, f4, f5, f6, f7,
                                              f8)
print("time elapsed: {:.2f}s".format(time.time() - start_time))