from taumodels import *
from modal_functions import *

def test22(i2, i3, i4, i5, i6, i7, i8):

   for f2 in tal[i2]:
       for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[22]:
                                    for j in K[22]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[22]:
                                            return i2, i3, i4, i5, i6, i7, i8