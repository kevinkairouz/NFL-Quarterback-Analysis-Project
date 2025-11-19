import matplotlib.pyplot as plt 

years = [2020, 2021, 2022, 2023, 2024] 
mahomesCP = [66.3, 66.3, 67.1, 67.2, 67.5] 
jacksonCP = [64.4, 64.4, 62.3, 67.2, 66.7]  
allenCP = [69.2, 63.3, 63.3, 66.5, 63.6]  
rodgersCP = [70.7, 68.9, 64.6, 64.6, 63.0]


lineSettings1 = dict(marker = "o", markersize = 10, color = "red", linewidth = 4, linestyle = "dashed") 
lineSettings2 = dict(marker = "*", markersize = 10, color = "purple", linewidth = 4, linestyle = "dashed") 
lineSettings3 = dict(marker = "v", markersize = 10, color = "blue", linewidth = 4, linestyle = "dashed") 
lineSettings4 = dict(marker = "o", markersize = 10, color = "green", linewidth = 4, linestyle = "dashed") 

titleSettings = dict(fontsize = 15, color = "blue")

plt.title("NFL QB Completion % (2020-2024)", **titleSettings) 
plt.xlabel("Year", **titleSettings) 
plt.ylabel("Completion Percentage", **titleSettings) 
plt.plot(years, mahomesCP, **lineSettings1) 
plt.plot(years, jacksonCP, **lineSettings2)  
plt.plot(years, allenCP, **lineSettings3)  
plt.plot(years, rodgersCP, **lineSettings4)
plt.xticks(years)  
plt.grid(axis = "y")  
plt.legend(["Patrick Mahomes", "Lamar Jackson", "Josh Allen", "Aaron Rodgers"])
plt.show()

