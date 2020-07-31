from toymodels import *
from modal_functions import *

def test5(i2, i3, i4, i5, i6, i7, i8):

   for f2 in toy[i2]:
       for f3 in toy[i3]:
            for f4 in toy[i4]:
                for f5 in toy[i5]:
                    for f6 in toy[i6]:
                        for f7 in toy[i7]:
                            for f8 in toy[i8]:
                                for i in K[5]:
                                    for j in K[5]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[5]:
                                            print(f2, f3, f4, f5, f6, f7, f8, modfun(f2, f3, f4, f5, f6, f7, f8, i, j))
