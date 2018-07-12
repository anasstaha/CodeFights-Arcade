Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

![alt text](area.png)

__Example__

* For n = 2, the output should be <br /> shapeArea(n) = 5;
* For n = 3, the output should be <br /> shapeArea(n) = 13.

__Input/Output__

* __[time limit] 4 seconds (py)__
* __[input] integer n__ <br /> Guaranteed constraints: <br />1 ≤ n < 104.

* __[output] integer__ <br />The area of the n-interesting polygon.
