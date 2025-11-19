import matplotlib.pyplot as plt  


lineSettings1 = dict(marker = "o", markersize = 10, color = "red", linewidth = 4, linestyle = "dashed") 
lineSettings2 = dict(marker = "*", markersize = 10, color = "purple", linewidth = 4, linestyle = "dashed") 
lineSettings3 = dict(marker = "v", markersize = 10, color = "blue", linewidth = 4, linestyle = "dashed") 
lineSettings4 = dict(marker = "o", markersize = 10, color = "green", linewidth = 4, linestyle = "dashed") 

years = [2020, 2021, 2022, 2023, 2024] 
mahomesInt = [6, 13, 12, 14, 11] 
jacksonInt = [9, 13, 7, 7, 4] 
allenInt = [10, 15, 14, 18, 6]  
rodgersInt = [5, 4, 12, 0, 11] 

plt.plot(years, mahomesInt, **lineSettings1) 
plt.plot(years, jacksonInt, **lineSettings2) 
plt.plot(years, allenInt, **lineSettings3) 
plt.plot(years, rodgersInt, **lineSettings4)   

plt.xticks(years)  
plt.title("NFL Quarterback Interception (2020 - 2024)") 
plt.grid(axis = "x") 
plt.legend(["Patrick Mahomes", "Lamar Jackson", "Josh Allen", "Aaron Rodgers"])
plt.xlabel("Year") 
plt.ylabel("Interceptions")

plt.show() 
