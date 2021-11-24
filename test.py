import numpy as np


id = True
test = False
x = 500

state = [id,test, x]
ttse = np.array(state, dtype=int)
for states in ttse:
    print(states)