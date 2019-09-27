$$
transfer error (f)

\text{message transfer = 3 bits once}

3f^2 + f^3
\text{lower error percentage}

$$

11

$$
hamming distance = bit diff counts

1234 => real code
5 => parity (look up 123)
6 => parity (look up 234)
7 => parity (look up 134)

0110 => 0110|001

non error percentage: (1-f)^7 + 7f(1-f)^6

erro percentage: C(7,2) * f^2(1-f)^5 \approx 21f^2

$$

quiz

$$
\begin{bmatrix}
 & a & g & c & t\\
a & 1-4f&2f&f&f\\
g&2f&1-4f&f&f\\
c&f&f&1-4f&2f\\
t&f&f&2f&1-4f
\end{bmatrix}\\
a,t: 30 \%
\\
c,g: 20 \%\\


P(r) = e^\lambda \cdot \frac{r^\lambda}{\lambda!} \\
r= \lambda \\
e^\lambda \frac{\lambda^\lambda}{\lambda!} = \frac{1}{\sqrt{2\pi\lambda}}\\
\lambda! = (\frac{\lambda}{e})^\lambda \frac{1}{\sqrt{2\pi\lambda}}
$$


baye's law

prior odds
P(A) = 20%
P(-A) = 80%
=1/4

likelihood

XXX7XXXX
YYYYYYYY

phone number = $$\frac{1}{10^7} / \frac{1}{10^8}$$ = 10 倍 

posterior odds
$$
\frac{P[A|S]}{P[-A|S]} = \frac{P[A]}{P[-A]} \frac{P[S|A]}{P[S|-A]}
$$

posterior = prior odds * likelihood

is better than bayes law (P[S] is not easy to get.)

---

linearly variance

linearly expectation



---

* odds form of bayes law (p29)

* expectation (p1)
$$
E[f(x)] = \sum_ipx_if(x_i)
$$

* entropy (p32)
https://planetcalc.com/2476/
$$
H(p_1 \cdots p_k) = \sum_i p_i \log\frac{1}{p_i} = E[\log\frac{1}{p_i}]
$$
entropy can be used to predict the least bits needs to be transfer
a = 1/2, b = 1/2, h = 1
a = 2/3, b = 1/3, h = .92 => can use less than 1 bit to code
(use huffman code)

* approx combination (Stirling approx) (p2)
$$
N! \approx (\frac{n}{e})^n\sqrt{2\pi n}
$$

another way

$$
H_2(p) = H(p, 1-p) = p\log p + (1-p)\log(1-p) \\
\ln \binom{N}{r} \approx NH_2(\frac{r}{N})
$$

hw : 1.13 => 1.15 => 1.17
