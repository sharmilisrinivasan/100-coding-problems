
## Encrypted Love 2.O

### [Problem Statement](https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/encrypted-love-2o/)

Hello guys i think you remeber Karthik from Encrypted Love problem right ?

His girlfriend's brother  got some doubt about her messages and somehow decrypted the messages.

But Karthik still a smart guy  obviously a true lover and dont wanted to giveup messaging her. So he came up with a new encryption technique.

**Decryption Process**:

word will start with the middle character of the string and will be formed henceforth with the middle characters of the right and left substrings (of the middle character of the word) and so on. Take a look at the explanation of the sample test case for better comprehension.

Since you are a best programmer she know ,she asked  your help to decrypt  the message.


**Input**:

The first line contains an integer _T_ denoting the number of TEST CASES.

Each TEST CASE consists of 2 lines.

The first line contains an integer _N_ denoting the length of the word that needs to be decrypted.

The second line contains the word that needs to be decrypted.


**Output**:

_T_ lines where each line will contain the decrypted words


**Constraints**:

`1 <= T <= 40`

`1 <= |S| <= 10000`


### Sample

#### Input

2

3

abc

4

abcd


#### Sample Output

bca

bcda


#### Explanation

In Test Case 2: The word was "*abcd*"

Middle character of this word is 'b' print b

Right Substring of 'b' is "cd"

Left Substring of 'b' is "a"

Now middle character of right substring is c print c

Now right substring and its middle character both d print d

Now left substring of b is a and its middle character is b print a

so finally

*bcda* is answer


### Constraints

- **Time Limit**: 1.0 sec(s) for each input file.
- **Memory Limit**:	256 MB
- **Source Limit**:	1024 KB
