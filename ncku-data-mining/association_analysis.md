# Association Rule Mining
4
use other items occurrence => predict an item occurrence
diaper => beer
**co-occurence**! **not causality**!

5
itemset : collection of n items
k-itemset : collection of k items

support count : itemset 出現幾次

support : support count 在所有 itemset 的比例 probability ratio (0 to 1)

frequent itemset : 若 itemset appear 大於 support 就叫 frequent itemset

6
x imply y , x, y 都是 itemsets

rule evaluation metrics
 support : 同時出現 x, y 的 fraction
 confidence : 所有包含 x 也有包含 y 的 fraction

7
example

8
association rule mining task
transactions set T
support >= minsup = minimum support
confidence >= minconf = minimum confidence

brute force => 不可行
找出演算法

9
mining association rules
若用相同的 itemset 來拆分 並且重組
support 會都一樣
confidence 會不一樣

10
產生所有 frequent itemset 非常困難
而 frequent itemset 最多產生不到五個

11
frequent itemset generation
d items => 2^d possible

12
brute-force
先產生 M 個 candidates
從 n 個 itemset 去比對所有 M
來看該 itemset 是否為 frequent itemset
O(MNw)
M (candidate) 太大

13
strategies
reduce M
reduce N
reduce NM: data strucutre


# Apriori Algorithm
15
自己的 support 不會超過自己的 subset 的 support
subset 不是 frequent => 自己也不是 frequent

16
AB 不是 frequent
ABC ABD 也不會是 frequent
prune supersets

17
從 1-itemsets 刪
得到新的 2-itemsets 再刪
最後得到 3-itemsets

因為 milk beer 被砍掉 => beer milk diaper 也不會出現

41 => 13 次

第二層可能還是非常多

18
notation
frequent k-itemset (lk)
candidate k-itemset (ck)

k-1 to explore k
subset test to k
ck = lk-1 x lk-1
generate frequent k-itemset (lk)

19
example of apriori

20 - 22
apriori algorithm

23
challenge
multiple scans
C2 very large

24
use hash to store candidate itemset

25 - 34
generate hash tree

35
產生完 freqeunt itemset 後
計算每種 subset 的 confidence 的方法



===

FP close