# Links and Notes for Placements
During my preparation for placements, I came across various useful resources for practicing programming problems.
1. Useful session on [Resume Building]( https://register.gotowebinar.com/recording/383093349775878413) 
2. Description about all important STLs can be found [here.]( https://github.com/meenakshiravisankar/coding-interview-cpp#algorithms)
3. Handbook for [Placements.](https://yangshun.github.io/tech-interview-handbook/algorithms/algorithms-introduction)
4. Top 100 questions on [LeetCode]( https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)
4. Must do Coding Questions on [Geeksforgeeks]( https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/)
5. Placement Tips at [IIT Kharagpur]( https://medium.com/@sunnydh/placement-preparation-iit-kgp-cse-89d7b7b37de3)
6. [Leetcode Patterns]( http://seanprashad.com/leetcode-patterns/)
8. [LeetCode Blind 75](https://leetcode.com/discuss/interview-question/460599/Blind-75-LeetCode-Questions)

## STLs
1. CPP STLs - https://github.com/meenakshiravisankar/coding-interview-cpp
2. Python STLS - [Python](/python-ds.py)

# C++ and OOPs Concepts
1. https://www.toptal.com/c-plus-plus/interview-questions
1. https://www.geeksforgeeks.org/c-cpp-tricky-programs/
# Java Videos
1. https://www.linkedin.com/feed/update/urn:li:activity:7048473240330997761/
2. Contains Spring etc.
3. Java Collections - https://www.callicoder.com/java-arraylist/
# Computer Networks
1. [Computer Networks](https://www.geeksforgeeks.org/commonly-asked-computer-networks-interview-questions-set-1/)

# Operating Systems
1. [Operating System](https://www.geeksforgeeks.org/commonly-asked-operating-systems-interview-questions-set-1/)

# DBMS
1. SQL practice from InterviewBit and W3Schools - https://www.w3schools.com/sql/default.asp

# Miscellaneous
1. [Sorting Algorithm Animation](https://www.toptal.com/developers/sorting-algorithms)
2. [Amazon Debugging](https://www.evernote.com/client/snv?noteGuid=d0047552-4cff-4c29-b305-b8aa2d33f364&noteKey=636f07d57c2eb3ea&var=b&sn=https%3A%2F%2Fwww.evernote.com%2Fshard%2Fs683%2Fsh%2Fd0047552-4cff-4c29-b305-b8aa2d33f364%2F636f07d57c2eb3ea&exp=ENB3907&title=Amazon%2BOA1%2BDebugging)

# Interview
4. [Top Interview Questions](https://www.geeksforgeeks.org/top-25-interview-questions/)
5. [Algorithm Questions](https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/?ref=rp)
6. [Amazon Interview](https://www.geeksforgeeks.org/amazon-interview-questions/?ref=rp)
5. [Puzzles](https://www.geeksforgeeks.org/category/puzzles/)
6. [NeetCode](https://neetcode.io)
7. [Grind75](https://www.techinterviewhandbook.org/grind75)
8. [Leetcode Patterns](https://seanprashad.com/leetcode-patterns/)
9. https://github.com/williamfiset/Algorithms
10. CPP STLs - https://github.com/meenakshiravisankar/coding-interview-cpp
11. 
12. https://github.com/kaushal02/interview-coding-problems


# Topic Wise DS-Algorithm Questions 
## Array
## Strings
## Two Pointers
1. Container with most water https://www.geeksforgeeks.org/container-with-most-water/ 
2. 3 Sum
## Binary Search
1. Search in Rotated Sorted Array https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
## Hashing
## Linked List
1. Rotate LinkedList https://www.geeksforgeeks.org/rotate-a-linked-list/ 
1. Reverse Linked List https://www.geeksforgeeks.org/reverse-a-linked-list/
2. Find Intersection of Y https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/ 
3. Detect Cycle https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/ 
4. Detect and Remove Cycle https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/ 
## Stacks
1. Parenthesis
## Queues
## Greedy 
1. Job Scheduling
## Dynamic Programming
Write-ups with a worked example and Python: [Dynamic Programming](docs/index.html). Live site: https://akramit.github.io/Placement-Preparation/
1. [Maximum Sum Subarray](docs/dp/maximum-sum-subarray.html)
    - max_sum[i] = max(arr[i], arr[i]+max_sum[i-1])
    - O(n)
2. [Longest Common Subsequence](docs/dp/longest-common-subsequence.html)
   - lcs[i][j] = 1 + lcs[i-1][j-1]  if str1[i] = str2[j]
   - lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]) if str1[i] != str2[j]
   - O(n^2) - space can be reduced to just O(n)
3. [Edit Distance](docs/dp/edit-distance.html)
   - edit[i][0] = i, edit[0][j] = j
   - edit[i][j] = edit[i-1][j-1] if str1[i] = str2[j]
   - edit[i][j] = 1 + min(edit[i-1][j], edit[i][j-1], edit[i-1][j-1]) if str1[i] != str2[j]
   - O(n^2)
4. [Coin Change](docs/dp/coin-change.html) (min coins and number of ways) **IMP**
    - amount n, denoms of size m. Each coin may be reused.
    - P1 min coins: dp[a] = min(dp[a - c] + 1) over coins c <= a, dp[0] = 0
    - P2 combinations (order ignored): for each coin, then for amount upward, dp[a] += dp[a - c]
    - P3 permutations (order counts): [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/description/). For each amount, then each coin, dp[a] += dp[a - c]
5. [Longest Increasing Subsequence](docs/dp/longest-increasing-subsequence.html)
   - lis[i] - longest increasing subsequence ending at i
   - lis[i] = max(lis[i], 1 + lis[j]) for j < i and arr[j] < arr[i]
   - O(n^2). O(n log n) keeps the smallest tail of every subsequence length and binary-searches it
6. [Longest Palindromic Subsequence](docs/dp/longest-palindromic-subsequence.html)
   - lps[i][i] = 1
   - lps[i][j] = 2 + lps[i+1][j-1] if s[i] == s[j] (inside is 0 when j = i+1)
   - else lps[i][j] = max(lps[i+1][j], lps[i][j-1])
   - Fill by substring length from 1 to n
   - O(n^2)
9. [0-1 Knapsack](docs/dp/knapsack.html)
   - dp[i][c] = best value using the first i items and capacity c
   - dp[i][c] = max(dp[i-1][c], dp[i-1][c - w[i]] + v[i]) when the item fits
   - O(n * W). Scan a 1D table downward so each item is used at most once
10. 
11. [Subset Sum](docs/dp/subset-sum.html)
    - dp[t] is true if some subset sums to t. dp[0] = true
    - for each number x, for t from T down to x: dp[t] = dp[t] or dp[t - x]
    - O(n * T)
## Trees
1. Invert Tree, Height of Tree, BST Search, 
2. Identical Trees https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
2. Lowest Common Ancestor https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
3. Diameter of Tree https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
4. Maximum Path Sum https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
5. Level Order Traversal https://www.geeksforgeeks.org/level-order-tree-traversal/
## Graphs
1. BFS
2. DFS
3. Cycle in Undirected Graph, Directed Graph
4. Topological Sorting 
5. Shortest Path using BFS
5. Shortest Path (Dijkstra)
6. Minimum Spanning Tree
## Miscellaneous
1. Backtracking - NQueens https://leetcode.com/problems/n-queens/

# System Design 
1. GitHub Repo - [Donne Marting](https://github.com/donnemartin/system-design-primer)
1. https://github.com/arpitbbhayani 
2. [Alex Xu](system-design.pdf)
3. https://medium.com/system-design-blog
4. [Uber Blog](https://www.uber.com/en-SG/blog/engineering/)
5. [Martin Fowler](https://martinfowler.com/tags/microservices.html)
6. InterviewBit - https://www.interviewbit.com/system-design-interview-questions/

## Design
1. Tiny URL - http://n00tc0d3r.blogspot.com 
- Algorithm - https://stackoverflow.com/questions/742013/how-do-i-create-a-url-shortener 
2. SQL vs NoSQL - https://www.sitepoint.com/sql-vs-nosql-differences/

