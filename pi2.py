
from testing_for_preservation import *


def pi2(f):
    if [f(0, 0), f(1, 1)] in K[2]:
        if [f(0, 1), f(1, 0)] in K[2]:
            if [f(1, 0), f(0, 1)] in K[2]:
                if [f(1, 1), f(0, 0)] in K[2]:
                    print(f)


