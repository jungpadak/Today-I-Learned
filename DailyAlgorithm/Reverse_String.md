# 문제 설명

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

<br />

# 입출력 예시

**Example 1**:
Input: ["h","e","l","l","o"] <br />
Output: ["o","l","l","e","h"] <br />

**Example 2**:
Input: ["H","a","n","n","a","h"] <br />
Output: ["h","a","n","n","a","H"] <br />

<br />

# 문제 풀이

## Python

```py
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

```
