## Binary associativity

### [Problem Statement](https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/binary-associativity-fc8ca73f/)

A binary operation * on a set S is called associative if it satisfies the associative law: (x * y) * z = x * (y * z) for all x, y , z  in S.

For the binary set S = {0,1} and a particular binary operator * , you are given its truth table. Determine if the operation is associative.

                                | a | b | a*b |
                                |---|---|-----|
                                | 0 | 0 | c0  |
                                | 0 | 1 | c1  |
                                | 1 | 0 | c2  |
                                | 1 | 1 | c3  |

### Input

* First line: A single integer  denoting the number of test cases

* For each test case:

    * First line: Four space-separated integers 

### Output

For each test case, print 'Yes' (without quotes) in a new line if the binary operation is associative in nature. Otherwise, print 'No' (without quotes).

### Constraints

1 <= T <= 8

c0, c1, c2, c3 ϵ {0,1}

### Sample

#### Input

1
0 1 1 0

#### Sample Output

Yes

#### Explanation

The given operation is the binary xor. It can be easily proved that it is associative.

### Misc constraints

- **Time Limit**:	1.0 sec(s) for each input file.
- **Memory Limit**:	256 MB
- **Source Limit**:	1024 KB
