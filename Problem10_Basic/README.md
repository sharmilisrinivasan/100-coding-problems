## Number of Markers (Question from competition in Skillenza platform)

### Problem Statement

In a metro city in Lalaland there is a long road with markers on it after each 1 metre. There is a big International School whose vehicles are parked on the road in front of the school.

Let’s say there are **_N_** vehicles standing on road. You are given the starting and the end point of each vehicle standing on the road. (both inclusive.)

You have to find the number of markers that is covered by at least one vehicle. A vehicle with starting point **_X_** and end point **_Y_** is considered to be present on a marker **_M_** if `X <= M <= Y`.

_Note_: This is a parallel parking lot. The markers cover the whole lot. And it is possible for multiple vehicles to overlap. (That is suppose a vehicle is parked from starting point **_X_** to end point **_Y_**. It is possible for another vehicle to be parked parallely from **_A_** to **_B_** where `X<=A<=Y`) As mentioned, the markers cover the whole lot.

### Input
The first line of input consists of an integer **_T_** (number of test cases). Each test case consists of the following:
The first line of test case consists of an integer **_N_**.
This is followed by **_N_** lines with two space separated integers **_X_** and **_Y_** in each line. **_X_** represents the starting position and **_Y_** the ending position as described above.

### Output
For each test case, print a single integer which is the count of the number of markers with at least one vehicle in separate lines.

### Constraints
- `0<T< 1000`
- `0<N<10000`
- `-32768<X,Y<32767`

### Sample

#### Input
2


3


4 7


-1 5


3 6


2


1 4


8 13

#### Sample Output
9

10

#### Explanation
For the first test case, we have at least one vehicle standing at markers (-1,0,1,2,3,4,5,6,7); so output is 9.
