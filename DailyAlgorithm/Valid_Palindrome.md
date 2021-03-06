# 문제 설명

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

<br />

# 입출력 예

**Example 1**:

**Input**: s = "A man, a plan, a canal: Panama" <br>
**Output**: true <br>
**Explanation**: "amanaplanacanalpanama" is a palindrome. <br>

**Example 2**:

**Input**: s = "race a car" <br>
**Output**: false <br>
**Explanation**: "raceacar" is not a palindrome. <br>

**Constraints**:

1 <= s.length <= 2 \* 105 <br>
s consists only of printable ASCII characters. <br>

<br />

# 문제 풀이

## Python

```py
import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque(string.lower() for string in s if string.isalnum())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True
```
