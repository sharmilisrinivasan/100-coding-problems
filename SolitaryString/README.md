## [Solitary String](https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/solitary-string/)

### Problem Statement

In order to celebrate Women's day, Stella started playing with string **_S_**. She needs to know the maximum number of characters between any two same characters in the string.
As she is busy in playing, help her for the same.

If there are no two same characters in the string, print −1.

_Note_: String is composed of lowercase letters of the Latin alphabet.

### Input
First line contains one integer **_T_**, denoting the number of test cases. 
Each of the next **_T_** line contains one string **_S_**.

### Output
For each test case, output the maximum number of characters between any two same characters in the string. If there are no two same characters in the string, print -1. Print answer for each test case in a new line.

### Constraints
- `1<=T<=10`
- `1<=S<=10^5` , where `|S|` determines the length of the string.
- String is composed of lowercase alphabets ranging from _a_ to _z_.

### Sample

#### Input
2

aba

babcddc

#### Sample Output
1

2

#### Explanation
Here, 
1. For string = _aba_

	There is only one character between two occurrences of _a_.

2) For string = _babcddc_
	
    There is one character between two occurrences of _b_, and 2 characters between two occurrences of _c_. So, the answer is _2_.
