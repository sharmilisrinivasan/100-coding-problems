## Deque Problem

### Problem Statement

Given a Deque with **_N_** elements .You have to find the maximum Alpha Value of the Deque that can be achieved by applying remove operation any number of times.

### Definitions
- **Alpha value** is defined as number of elements currently present in the deque multiply by the smallest element currently in the deque.
- You can remove an element from both front and rear in a **Deque**.

### Constraints
- `1<=T<=100`
- `1<=N<=10^4`
- `1<=Value<=10^9`

### Format of the input file 
- **First line**: **_T_** i.e number of testcases. 

    For each testcase,
    
- **First line** : **_N_** i.e number of elements 
- **Second line** : N space separated integers denoting value of each element. 

### Format of the output file
Print the answer for each test case in a separate line.

### Sample

#### Input
2

5

1 2 3 4 5

5

3 2 1 4 5
#### Sample Output
9

8

#### Explanation
Maximum alpha value is obtained if the Deque Contains 3 elements {3,4,5} = 9.
