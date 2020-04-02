Traveling Salesperson:

Reference: 
(Only used the reference very briefly, tried to figure out a possible algorithm by myself on paper.)

This module can be used for TSP problems that are symmetrical (same "distance" back and forth) and "distance" can stand for any variable that should be minimalized (e.g. time, gas consumption).
It uses as input the matrix of distances, which should be in the format and given as .csv
	A	B	C
A		AB	AC

B	AB		BC	

C	AC	BC	


For problems with N<=8, it uses the exact method to calculate the shortest route.

For problems with N>8, it uses the nearest-neighbour method from different starting points to find the shortest route available to the nearest-neighbour method.
Unfortunately, this method can work badly for some problems (e.g. with many outliers).
Therefore, the module gives the lower limit (sum of the shortest distances for each city) and the upper limit (sum of the longest distances for each city), as well as the average distance of a random route in order to see how the output route compares.
A possible optimization (that there was no time for), would be to offer optimization of the route to the user after comparing to these values, for example by taking out individual nodes with very large differences way over the average distance for this node and placing them into the nearest edge.

This repository also contains 3 example datasets, two larger than 8 (sweden, germany) and one of size 8 (eurotrip).
The standard is the Sweden dataset, to use a different one the filename has to be changed in the code.