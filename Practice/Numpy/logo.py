import numpy as np
import matplotlib.pyplot as plt

try:
  load = np.load('logo.webp')
  plt.subplot(121)
  plt.imshow(load)
except:
  print("file Not found")
