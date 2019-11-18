# Basic Models

seq2seq

video captioning

# Picking the most likely sentence

machine translation = conditional language model

how to find the most likely translation

why not greedy algorithm

1. going > visiting
2. the vocab space is too large

# Beam Search

beam width = 3 consider 3 word



## Refine Beam Search

length normalization

because numerical underflow => take log and become summing

and max log equals to max

===

and multiply may tend to use shorter sentence

its true also for log summing

=> normalize with alpha

===

beam width decision

if too big, better but cost higher
if too small, worse but cost cheaper
production 10 - 100

make paper best 1000 - 3000

## Error Analysis in Beam Search

use human example y* to compare with predicted y^

if y* > y^ then beam search may have problems

else y* < y^ then RNN models may have problems

finally you go through each examples and collect the ratio from B problems and R problems


# Bleu Score

how to evaluate multiple translations

understudy 表示隨時可替代正規的後補

human reference => dev/test set

precision : not good 7/7

modified precision : credit = appear times

n-grams

# Attension Model

改善 encoder - decoder network

## Intuition

long sentence's bleu score is not good 

memorize super long sentence is hard

attension model translation like human

at each RNN steps + attension weights to get context

## Detail

c = alpha * a

and use c to compute y

new a is described as s

how to compute alpha

how to compute e<t,t'>


# Speech Recognition


# Trigger Word Detection

