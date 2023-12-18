## ❄️ Advent of Code Solutions ❄️

A repository to store my solutions to the annual advent of code puzzles. All of my solutions are written in Python.

### 📝 Learnings

#### :snake: Python

**<u>2-element list indexing using a boolean</u>:**

This is extremely useful when you binary choices for indexing. It can remove the need to write an *if else* statement depending on what the value of the index is.

```
list = ['a', 'b']
list[False]
> 'a'
list[True]
> 'b'
list = ['XXX', 'ZZZ']
current = 'R'
list[current=='R'] # this statement is true
# has chosen the right element
> ZZZ 
```

**<u>iterools.pairwise</u>**

Allows you to get the successive overlapping pairs in any iterable.
```
from itertools import pairwise
list(pairwise(list(range(5))))
> [(0, 1), (1, 2), (2, 3), (3, 4)]
```
https://docs.python.org/3/library/itertools.html#itertools.pairwise

#### 🧠 Algorithm Patterns
*Algorithm learnings go here.*

#### Misc
*Misc learnings go here.*
