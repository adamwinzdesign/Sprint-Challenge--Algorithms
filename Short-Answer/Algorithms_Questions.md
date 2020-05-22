# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n

      O(n) because n * n^2 = n^3, so it would take n number of n^2 increments to reach n^3
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

      O(n log n) because of the nested loop
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

      O(n) because the function is recursive and it ends when bunnies reaches 0.
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Assuming that there is an equal chance of egg survivability from n floors given zero trials, we would want to implement a binary search to minimize the number of trials and thus broken eggs.

To do this, we would start by dropping an egg from floor n // 2 and observing the result.  If the egg breaks, we have eliminated all floors above the floor at n // 2.  We would then determine the new midpoint for all of the remaining floors and drop an egg from that floor.  If the egg breaks again, we have eliminated half of the remaining floors again, or 75% of the original total number of floors n.  

If the egg survives the first drop from n // 2, we have eliminated half of the floors below the floor at n // 2, so we determine the midpoint of the remaining floors and drop another egg from that floor, observe the result, and so on, until we determine the correct floor f.

This method would have a runtime complexity of O(log n)
