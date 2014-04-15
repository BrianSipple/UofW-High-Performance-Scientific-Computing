# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

pwd

# <codecell>

import mysqrt

# <codecell>

mysqrt.test()

# <codecell>

run mysqrt.py

# <codecell>

mysqrt.sqrt2

# <codecell>

mysqrt.__cached__

# <codecell>

mysqrt.__reduce_ex__

# <codecell>

time sqrt(2.)

# <codecell>

time mysqrt(2, 3)

# <codecell>

timeit sqrt(2.)

# <markdowncell>

# us means micro-seconds, 1e-6 seconds

# <codecell>

timeit mysqrt.sqrt2(44, 2)

# <codecell>

timeit y = sqrt(linspace(0, 1, 1000))

# <codecell>

%%timeit
y = zeros(1000)
for i in range(len(y)):
    y[i] = sqrt(i)
    

# <markdowncell>

# ms = millisecond = 1e-3 seconds = 1000 microseconds

# <codecell>


