# -*- coding: utf-8 -*-

import random
r1 = random.randrange(0, 7)
r2 = random.randrange(0, 7)
r = r1 + r2
print('r1 is', r1, '\n', 'r2 is', r2, '\n', 'Sum r is', r, '\n')


if  r1 == 0 or r2 == 0:
    print('Not valid!')
elif r == 7:
    print('Draw!')
elif r < 7:
    print('Small!')
elif r > 7:
    print('Big!')
