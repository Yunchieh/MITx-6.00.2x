#Exercise 5
#5/5 points (graded)
#Challenge Problem! This problem is difficult and may stump you, but we include it because it is very interesting, especially for those who are more mathematically inclined.

#Don't worry if you can't get all the math behind it, and don't get discouraged. Remember that you do not lose points for trying a problem multiple times, nor do you lose points if you hit "Show Answer". If this problem has you stumped after you've tried it, feel free to reveal the solution and read our explanations.

#In the following examples, assume all graphs are undirected. That is, an edge from A to B is the same as an edge from B to A and counts as exactly one edge.

#A clique is an unweighted graph where each node connects to all other nodes. We denote the clique with n nodes as KN. Answer the following questions in terms of n.

How many edges are in KN?

n * (n - 1)/2
 
Consider the new version of DFS. This traverses paths until all non-circular paths from the source to the destination have been found, and returns the shortest one.

Let A be the source node, and B be the destination in KN. How many paths of length 2 exist from A to B?

n - 2

How many paths of length 3 exist from A to B?

(n - 2) * (n - 3)

Continuing the logic used above, calculate the number of paths of length m from A to B, where 1≤m≤(n-1), and write this number as a ratio of factorials.

To indicate a factorial, please enter fact(n) to mean n!; fact(n+2) to mean (n+2)!, etc.

#The 'logic above' from the last part of the problem
#Click to see the solution for the previous problem, if you want some guidence on how to think about this problem part

fact(n - 2)/fact(n - m - 1)

Using the fact that for any n, 10!+11!+12!+...+1n!≤e for all n, where e is some constant, determine the asymptotic bound on the number of paths explored by DFS. For simplicity, write O(n) as just n, O(n2) as n^2, etc.

fact(n - 2)