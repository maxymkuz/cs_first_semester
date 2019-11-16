import time
import sys
n = int(1e7)

lst = []

start = time.time()

# lst = [i for i in range(n)] 0.7152180671691895
# lst.append(i)   1.323805570602417
# lst += [i]   1.4630308151245117
# lst.extend([i])   1.5238490104675293
# lst.insert(-1, i)   2.090437889099121


print(time.time() - start)
