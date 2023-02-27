import pandas as pd
import numpy as np
mx, mx_1 = np.eye(3), np.eye(3)
new_mx_v = np.vstack((mx, mx_1))

print(new_mx_v)




# def stars(rwm):
#     if rwm.country == 'Canada':
#         return 3
#     elif rwm.points >= 95:
#         return 3
#     elif rwm.points >= 85:
#         return 2
#     else:
#         return 1
#
#
# star_rt = rev.apply(stars, axis=1)
# print(star_rt.loc[340:349])
# print(star_rt)
# print(rev.points.loc[rev.points >= 95])

