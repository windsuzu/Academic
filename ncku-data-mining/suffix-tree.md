# FP-growth

FP-growth 的主要目的是破解 candidate generation 所引起的 bottleneck

並且在 main memory 實作，進而減少對 database 的 scans

FP-growth 主要的概念是 divide-and-conquer

並且利用了 suffix tree 的概念

## Suffix Tree

文章中有沒有出現字串

用 tree 查詢 leaf node + 1

先找出 suffix 建成 tree



## FP-Growth Algorithm

mining frequent without candidate generation.

1.generate frequent pattern tree



### FP-Trees Construction

scan 1-item and sorted

itemset =&gt; frequent based sorted reordering

build fp-tree \(p.56\)

link header table to fp-tree



fetch 由下往上 find conditional pattern base

建立出 conditional fp-tree

再拼出所有 frequent patterns



### Start FP-Growth



### Example



### FP-Growth Adventages



## Presentation of Association Rules

support decision

reduced support 動態決定 flexible support \(商品單價也會影響\)

max pattern : 一個 frequent itemset 沒有比他更大的 frequent itemset



## Closed Association Rules

closed itemset : 

frequent closed itemset : 沒有一個 superset 有跟自己一起出現

再用 closed frequent itemsets =&gt; association rule







