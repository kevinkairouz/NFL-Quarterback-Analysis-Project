import matplotlib.pyplot as plt    
import numpy as np 

#using numpy arrays because they are faster and increase performance 


#bar chart that contain wins per qb   
plt.title("Total Touchdowns per Quarterback", color = "gray")

quarterBacks = ["Patrick Mahomes", "Lamar Jackson", "Josh Allen", "Aaron Rodgers"] 
wins = np.array([108, 78, 83, 162])

plt.bar(quarterBacks, wins, color = ["red", "purple", "blue", "green"]) 
plt.show()