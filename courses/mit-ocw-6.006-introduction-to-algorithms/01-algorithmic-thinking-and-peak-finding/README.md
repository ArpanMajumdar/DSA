# Lecture 1 - Algorithmic thinking and peak finding

## Peak finding

### Problem
Given a-i are integers. You have to find peak. A position `b` is defined as peak if and only if
1. `b >= a` and `b >= c`
2. Positions at ends have to be greater than or equal to only one side.
Find the peak if it exists.

#### Straight forward solution
Start from left and go all the way to right. The best and worst case algorithm complexity is $\theta(n)$.

#### Divide & conquer algorithm
Divide the array in half and compare the `n/2` element with `n/2 -1` and `n/2 + 1` element.

**Pseudocode**

```
if(a[n/2] < a[n/2 - 1]):
    only look at the left half 1..n/2-1 for a peak
else if(a[n/2] < a[n/2 + 1]):
    only look at the right half n/2+1..n for a peak
else:
    n/2 position is the peak
```

**Algorithmic complexity**
Let `T(N) is the work done on input of size N.` After each step, size of the input reduces by half. `\theta(1)` is the constant time taken for making 2 comparisons.
```
T(N)    = T(n/2) + \theta(1)
        = T(n/4) + \theta(1) + \theta(1)
        ...
        = 0 + {\theta(1) + ... + \theta(1)} log_2(n) times.
        = \theta(log_2(n))
```

### 2-D version of peak finding
