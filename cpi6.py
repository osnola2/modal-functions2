from taumodels import *
from modal_functions import *

def test6(i2, i3, i4, i5, i6, i7, i8):

   for f2 in tal[i2]:
       for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[6]:
                                    for j in K[6]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[6]:
                                            return i2, i3, i4, i5, i6, i7, i8

