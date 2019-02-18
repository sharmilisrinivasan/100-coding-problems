
## Game of Colors

### [Problem Statement](https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/game-of-colors/)

You are given a grid of size N * N where each cell contains either **red\(R\)**, **green(G)** or **blue(B)** color. Each cell changes it color after a fix interval of time  t[i][j] (1<=i,j<=N) known as frequency of that cell.

For example, consider a cell with color R at t=0 and frequency of this cell is 2. At t=1, its colour will be R, at t=2, its colour will be G at t=4 it will be B and at t=6 it will R again. That is, it changes its colour every 2 seconds.

Now you have to answer Q queries where each query contains a time instant T and a sub-grid denoted by Left-top point (x1,y1)  and Right-bottom point (x2,y2) and a color C (R,G or B). You have to tell number of cells having color C in the sub-grid at time T.

**Constraints**:

`1 <= N <= 100`

`1 <= Q <= 500000`

`1 <= t[i][j] <= 100`

`1 <= T <= 100`

`1 <= x1, y1 <= N, x1 <= x2 <= N, y1 <= y2 <= N`

`Colour = R / G / B`


**Format of the input file**:

_First line_ : Two space separated integers N and Q.

_Next N lines_ : N space separated integers denoting frequency of each cell.

_Next Q lines_ : Five space separated integers and a space separated characted C denoting T x1 y1 x2 y2 C where C is the color.


**Format of the output file**:

For each test case output desired answer in a separate line.

### Sample

#### Input

3 2

1 2 1

2 1 2

1 2 3

2 1 1 3 3 G

2 1 1 3 3 R


#### Sample Output

4

1


#### Explanation
At the end of 2 seconds, we get the following grid:

B G B

G B G

B G R

Number of Green cells in sub-grid (1, 1) (3, 3) = 4.

Number of Red Cells in sub-grid (1, 1) (3, 3) = 1.

### Constraints

- **Time Limit**: 3.0 sec(s) for each input file.
- **Memory Limit**:	256 MB
- **Source Limit**:	1024 KB
