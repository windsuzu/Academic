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