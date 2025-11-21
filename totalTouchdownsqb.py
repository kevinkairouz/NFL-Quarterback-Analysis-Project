import matplotlib.pyplot as plt 

quarterbacks = ["Patrick Mahomes", "Lamar Jackson", "Josh Allen", "Aaron Rodgers"]
plt.title("Touchdowns thrown from 2020 - 2024")  


#2020-2024 seasons
mahomesTouchdowns = [38, 37, 41, 27, 26] 
lamarTouchdowns = [26, 16, 17, 24, 41] 
allenTouchdowns = [37, 36, 35, 29, 28] 
rodgersTouchdowns = [48, 37, 26, 0, 28]  

totalTouchdownsthrown = [sum(mahomesTouchdowns), sum(lamarTouchdowns), sum(allenTouchdowns), sum(rodgersTouchdowns)] 

plt.pie(totalTouchdownsthrown, colors=["red", "purple", "blue", "green"], labels= quarterbacks)  
plt.legend(["Patrick Mahomes", "Lamar Jackson", "Josh Allen", "Aaron Rodgers"]) 
plt.show()
