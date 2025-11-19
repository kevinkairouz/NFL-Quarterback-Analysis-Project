import matplotlib.pyplot as plt 


lineSettings1 = dict(marker = "o", markersize = 10, color = "red", linewidth = 4, linestyle = "dashed") 
lineSettings2 = dict(marker = "*", markersize = 10, color = "purple", linewidth = 4, linestyle = "dashed") 
lineSettings3 = dict(marker = "v", markersize = 10, color = "blue", linewidth = 4, linestyle = "dashed") 
lineSettings4 = dict(marker = "o", markersize = 10, color = "green", linewidth = 4, linestyle = "dashed") 

years = [2020, 2021, 2022, 2023, 2024] 
mahomesTouchdowns = [38, 37, 41, 27, 26] 
lamarTouchdowns = [26, 16, 17, 24, 41] 
allenTouchdowns = [37, 36, 35, 29, 28] 
rodgersTouchdowns = [48, 37, 26, 0, 28]  


plt.plot(years, mahomesTouchdowns, **lineSettings1) 
plt.plot(years, lamarTouchdowns, **lineSettings2) 
plt.plot(years, allenTouchdowns, **lineSettings3) 
plt.plot(years, rodgersTouchdowns, **lineSettings4)
plt.legend(["Patrick Mahomes", "Lamar Jackson", "Josh Allen", "Aaron Rodgers"])
plt.title("NFL QB Touchdowns (2020-2024)")
plt.show() 