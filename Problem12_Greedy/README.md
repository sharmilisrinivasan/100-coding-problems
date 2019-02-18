
## Protect the Cities

### [Problem Statement](https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/protect-the-cities-1/)

There are _N_ cities in Imaginary Land. The President of Imaginary Land uses the Cartesian coordinates. Each city is located at some point with integer co-ordinates. The President is very careful and concerned about the well-being of the citizens of his country.

For that reason, he wants to create a boundary and cover all the cities inside that boundary. The boundary should in the shape of a square and should be parallel to the coordinate axes. Find the minimum area enclosed by the boundary such that all the cities are on or inside the boundary.


**Input**:

The first line of the input contains _T_, denoting the number of test cases.

Each test case consists of a single positive integer _N_ denoting the number of cities in Imaginary Land.

Each of the next _N_ lines contains two integers _x<sub>i</sub>_ and _y<sub>i</sub>_  denoting the coordinates of the i<sup>th</sup> city.


**Output**:

For each test-case, output a single non-negative integer denoting the minimum area of the square boundary that encloses all the cities inside or on its boundary.


**Constraints**:

`1 <= T <= 5`

`1 <= N <= 10<sup>5</sup>`

`-10<sup>9</sup> <= x<sub>i</sub>,y<sub>i</sub> <= 10<sup>9</sup>`


### Sample

#### Input

2

4

-1 -1

1 1

1 -1

-1 1

3

0 0

1 1

2 2


#### Sample Output

4

4


#### Explanation

In the first test case, all the points are on the boundary of a square of side 2. Hence answer = 4.

In the second test case, the smallest square can be drawn is of side 2 having center at (0, 0).

### Constraints

- **Time Limit**: 1.0 sec(s) for each input file.
- **Memory Limit**:	256 MB
- **Source Limit**:	1024 KB
