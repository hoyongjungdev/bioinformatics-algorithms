from chapter1.minimum_skew import skew
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

genome = input()
skew_val = skew(genome)
skew_array = np.array(skew_val)
series = pd.Series(skew_array, index=np.arange(0, len(skew_val), 1))
series.plot()
plt.xlabel('index')
plt.ylabel('skew')
plt.show()
