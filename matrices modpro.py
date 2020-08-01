from matrices_by_lenght import *
from modalprofile import *

# for i in M1:
#     for j in i:
#         for k in i:
#             print(i, j, k, modpro(j, k))

for i in M2:
    for j in i:
          for k in i:
            print(j[0], k[0], modpro(j[0], k[0]), modpro(j[1], k[1]), i)