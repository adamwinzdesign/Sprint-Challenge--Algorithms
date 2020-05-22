#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n) because n * n^2 = n^3, so it would take n number of n^2 increments to reach n^3


b)  O(n log n) because of the nested loop


c)  O(n) because the function is recursive and it ends when bunnies reaches 0.

## Exercise II

Assuming that there is an equal chance of egg survivability from n floors given zero trials, we would want to implement a binary search to minimize the number of trials and thus broken eggs.

To do this, we would start by dropping an egg from floor n // 2 and observing the result.  If the egg breaks, we have eliminated all floors above the floor at n // 2.  We would then determine the new midpoint for all of the remaining floors and drop an egg from that floor.  If the egg breaks again, we have eliminated half of the remaining floors again, or 75% of the original total number of floors n.  

If the egg survives the first drop from n // 2, we have eliminated half of the floors below the floor at n // 2, so we determine the midpoint of the remaining floors and drop another egg from that floor, observe the result, and so on, until we determine the correct floor f.

This method would have a runtime complexity of O(log n)