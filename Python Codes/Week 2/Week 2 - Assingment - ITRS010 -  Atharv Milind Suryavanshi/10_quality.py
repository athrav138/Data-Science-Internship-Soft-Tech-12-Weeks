'''
10. Production Quality Inspection Report
A manufacturing company stores product quality scores in a text file named quality.txt.
quality.txt
78
85
91
67
88
95
72
80
Task:
• Read all quality scores from the file.
• Handle file-related errors.
• Store the scores in a suitable numerical structure.
• Calculate average, maximum, and minimum score.
• Create a tabular report containing all scores.
• Display only the scores that are above the average.
'''

import numpy as np
import pandas as pd

# • Handle file-related errors.
try:
  # • Read all quality scores from the file.
  f = open("quality.txt",'r')
  arr = f.readlines()
  arr = [int(i) for i in arr]
    
  print("File content: \n",arr)

  # • Store the scores in a suitable numerical structure.
  quality_scores = np.array(arr)
  print("The quality scores are: \n",quality_scores)

  # • Calculate average, maximum, and minimum score.
  print("Average: ",np.mean(quality_scores))
  print("Maximum: ",np.max(quality_scores))
  print("Minimum: ",np.min(quality_scores))

  # • Create a tabular report containing all scores.
  df = pd.DataFrame(quality_scores,columns=["scores"])
  print("Tabular report : ",df)

  # • Display only the scores that are above the average.
  print("The scores above average: ",df[df["scores"]>np.mean(quality_scores)])


  f.close()
except FileNotFoundError as e:
  print("The file not found: ",e)
except Exception as e:
  print("Some Exception: ",e)