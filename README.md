# Astar_rigid

This code implements A_star path planning algorithm. 
The obstacles are directly called from the half plane equations and are seperately plotted using matplotlib.
Three matrices rae initialised for updation of total cost (including heuristic) , visited nodes (marked as 1) and cost_2_come matrix for updation of edge costs.  
The orientation is prefixed but can be changed into user input by uncommenting line 54 similar for start and goal nodes at lines 59-65.

The value of radius and clearance is prefixed at 1 but can be changed. 
Step size is initialised to 2 but can be changed. 
The threshold value for rows and colomn is takes as 0.5 and 12 for orientation.
the backtracking is performed and the OPTIMAL PATH is stored in PATH LIST which is graphed using matplotlib.
Two functions are created namely "approximation" and "angle_approximation" for rounding of the value. ( division of 3 within each unit in the function approximation and division of 12 in 360 in angle_approximation).

when the goal area is reached a print statement is printed out 

For start node in obstacle it prints yes1
for goal node in obstacle it prints  yes2

start node : - 200 - user input , user input 
goal node : - 200 - user input , user input
