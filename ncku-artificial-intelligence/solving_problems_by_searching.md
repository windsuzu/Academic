# Introduction
problem solving agent = one of goal based agent

in chapter only consider peas



# Problem-Solving Agents
3
Search :

Execution : 

Design :


## Formulation
init
find possible actions
transition model (做了 action 會發生什麼)
goal test
path cost (action 的花費)
從 action 當中找出一個 best solution

### Example 
以地圖來說明

8-puzzle problem

8-queens problem

real world problem

## Searching for solution
finding map to tree
branches are actions
nodes are states
form a search tree

node properties
state
parent
action
path cost

### Measuring
completeness
optimality
time complexity
space complexity

# Uninformed Search Strategies
blind search
current state => tgenerate successors => goal / non-goal
order

example : BFS
子節點全試

受到深度控制 (輩分)

example : uniform-cost search
只選 lowest cost 子節點

每次都執行 gold test

還是會全掃過，但受到 path cost 控制

example : DFS


example : depth-limited search

example : iterative  deepening DFS
逐步增加 limit
complexity bound 在 最後一層

example : bidirectional search

# Informed (Heuristic) Search Strategies
best first search 
f > h , f = h

## Greedy best first search

f = h

## A* Search

f = g + h

best required = admissible heuristic + monotonicity

