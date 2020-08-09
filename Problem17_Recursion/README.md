
## Combination Sum

### [Problem Statement](https://leetcode.com/problems/combination-sum/)

Given a *set* of candidate numbers (`candidates`) *(without duplicates)* and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The *same* repeated number may be chosen from `candidates` unlimited number of times.


**Note**:

- All numbers (including `target`) will be positive integers.

- The solution set must not contain duplicate combinations.


**Constraints**:

- `1 <= candidates.length <= 30`

- `1 <= candidates[i] <= 200`

- Each element of candidate is unique.

- `1 <= target <= 500`


### Sample

#### Input-1

candidates = [2,3,6,7], target = 7,

#### Output-1

[
  [7],
  [2,2,3]
]

#### Input-2

candidates = [2,3,5], target = 8,

#### Output-2

[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
