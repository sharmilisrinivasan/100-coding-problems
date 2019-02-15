## Chandan and Balanced Strings

### [Problem Statement](https://www.hackerearth.com/ja/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/chandan-and-balanced-strings/)

Chandan got bored playing with the arrays all the time. Therefore he has decided to buy a string S consists of N lower case alphabets. Once he purchased the string, He starts formulating his own terminologies over his string S. Chandan calls a string str A Balanced String if and only if the characters of the string str can be paritioned into two multisets M1 and M2 such that M1= M2 .

**For eg**:

Strings like "abccba" , "abaccb" , "aabbcc" are all balanced strings as their characters can be partitioned in the two multisets M1 and M2 such that M1 = M2.

M1 = {a,b,c}

M2 = {c,b,a}

whereas strings like ababab , abcabb are not balanced at all.

Chandan wonders how many substrings of his string S are Balanced String ? Chandan is a little guy and do not know how to calculate the count of such substrings.

Can you help him in accomplishing this task ?

### Input

First line of input contains a single integer T denoting the number of test cases. First and the only line of each test case contains a string consists of lower case alphabets only denoting string S .

### Output

For each test case, print the count of Balanced Substrings of string S.

### Constraints

1 ≤ T ≤ 105

1 ≤ |S| ≤ 105

S consists of lower case alphabets only.

NOTE : sum of |S| over all the test case will not exceed 10^6.

### Sample

#### Input

2

aabb

abccba

#### Sample Output

3

3

#### Explanation

For test case 1 : Balanced substring are "aa" , "bb" , "aabb" . For test case 2 : Balanced substring are "cc" , "bccb" , "abccba" .

### Misc constraints

- **Time Limit**:	1.0 sec(s) for each input file.
- **Memory Limit**:	256 MB
- **Source Limit**:	1024 KB
