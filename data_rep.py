import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

data = {
  normal: random.normal(loc=1, scale=0.4, size=1000),
  binomial: random.binomial(n=10, p=0.5, size=1000),
}
sns.displot(data, kind = "kde", labels = ["Normal Distribution", "Binomial Distribution"])
plt.show()