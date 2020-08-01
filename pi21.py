from toymodels import *

# Defines pi21, i.e. the polymorphisms of K[21]. It is battery of definitions, compiled in a last definition.
# It works well for functions in tau2. However, I'm having trouble to use it with mu2, i.e. the binary modal functions.
# I'm looking for a form of definition of mu2 that could work with this definition, or a definition of pi21 that suits
# the current treatment of mu2.

def pi21a(f):
    if [f(0, 0), f(0, 0)] in K[21]:
        if [f(0, 6), f(0, 9)] in K[21]:
            if [f(0, 2), f(0, 9)] in K[21]:
                if[f(0, 3), f(0, 9)] in K[21]:
                    if [f(0, 5), f(0, 6)] in K[21]:
                        if [f(0, 4), f(0, 6)] in K[21]:
                            if [f(0, 9), f(0, 6)] in K[21]:
                                if [f(0, 1), f(0, 1)] in K[21]:
                                    return f
                                
def pi21b(f):
    if [f(6, 0), f(9, 0)] in K[21]:
        if [f(6, 6), f(9, 9)] in K[21]:
            if [f(6, 2), f(9, 9)] in K[21]:
                if [f(6, 3), f(9, 9)] in K[21]:
                    if [f(6, 5), f(9, 6)] in K[21]:
                        if [f(6, 4), f(9, 6)] in K[21]:
                            if [f(6, 9), f(9, 6)] in K[21]:
                                if [f(6, 1), f(9, 1)] in K[21]:
                                    return f
                                
def pi21c(f):
    if [f(2, 0), f(9, 0)] in K[21]:
        if [f(2, 6), f(9, 9)] in K[21]:
            if [f(2, 2), f(9, 9)] in K[21]:
                if [f(2, 3), f(9, 9)] in K[21]:
                    if [f(2, 5), f(9, 6)] in K[21]:
                        if [f(2, 4), f(9, 6)] in K[21]:
                            if [f(2, 9), f(9, 6)] in K[21]:
                                if [f(2, 1), f(9, 1)] in K[21]:
                                    return f
                                
def pi21d(f):
    if [f(3, 0), f(9, 0)] in K[21]:
        if [f(3, 6), f(9, 9)] in K[21]:
            if [f(3, 2), f(9, 9)] in K[21]:
                if [f(3, 3), f(9, 9)] in K[21]:
                    if [f(3, 5), f(9, 6)] in K[21]:
                        if [f(3, 4), f(9, 6)] in K[21]:
                            if [f(3, 9), f(9, 6)] in K[21]:
                                if [f(3, 1), f(9, 1)] in K[21]:
                                    return f
                                
def pi21e(f):
    if [f(5, 0), f(6, 0)] in K[21]:
        if [f(5, 6), f(6, 9)] in K[21]:
            if [f(5, 2), f(6, 9)] in K[21]:
                if [f(5, 3), f(6, 9)] in K[21]:
                    if [f(5, 5), f(6, 6)] in K[21]:
                        if [f(5, 4), f(6, 6)] in K[21]:
                            if [f(5, 9), f(6, 6)] in K[21]:
                                if [f(5, 1), f(6, 1)] in K[21]:
                                    return f
                                
def pi21f(f):
    if [f(4, 0), f(6, 0)] in K[21]:
        if [f(4, 6), f(6, 9)] in K[21]:
            if [f(4, 2), f(6, 9)] in K[21]:
                if [f(4, 3), f(6, 9)] in K[21]:
                    if [f(4, 5), f(6, 6)] in K[21]:
                        if [f(4, 4), f(6, 6)] in K[21]:
                            if [f(4, 9), f(6, 6)] in K[21]:
                                if [f(4, 1), f(6, 1)] in K[21]:
                                    return f
                                
def pi21g(f):
    if [f(9, 0), f(6, 0)] in K[21]:
        if [f(9, 6), f(6, 9)] in K[21]:
            if [f(9, 2), f(6, 9)] in K[21]:
                if [f(9, 3), f(6, 9)] in K[21]:
                    if [f(9, 5), f(6, 6)] in K[21]:
                        if [f(9, 4), f(6, 6)] in K[21]:
                            if [f(9, 9), f(6, 6)] in K[21]:
                                if [f(9, 1), f(6, 1)] in K[21]:
                                    print(f)

def pi21(f):
    if pi21a(f):
        if pi21b(f):
            if pi21c(f):
                if pi21d(f):
                    if pi21e(f):
                        if pi21f(f):
                            pi21g(f)