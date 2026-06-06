# Research Plan

## Tasks
1. Math verification (Part I, Chs 1-4)
2. Safety survey for Ch 12 (mid-2026 state of alignment/interp/safety)
3. References organized by chapter (Chs 1-12)
4. Executive summary

## Math claims to verify

### Ch 1 (Bayes)
- [ ] Cox's theorem (R. T. Cox 1946, Jaynes/Van Horn/Paris cleanups)
- [ ] Bayes' theorem derivation
- [ ] Coin example arithmetic: prior 1%, posterior 24%
- [ ] 5 heads in 32 trials = once in 32 (this is 1/32 = ~3.125%)
- [ ] Cox consistency requirements stated correctly
- [ ] Loose ends acknowledged accurately

### Ch 2 (Prior Problem)
- [ ] Aria's calculation: prior 0.5, posterior 0.97
  - P(trick|HHHHH) = (1*0.5) / (1*0.5 + (1/32)*0.5) = 0.5 / (0.5 + 0.015625) ≈ 0.97
- [ ] Ben's calculation: prior 0.001, posterior 0.031
  - P(trick|HHHHH) = (1*0.001) / (1*0.001 + (1/32)*0.999) ≈ 0.001 / (0.001 + 0.0312) ≈ 0.031
- [ ] Laplace's principle of insufficient reason
- [ ] Maximum entropy
- [ ] Empirical Bayes characterization

### Ch 3 (Description and Probability)
- [ ] Kraft's inequality statement and proof sketch
- [ ] Average length calculation: 1.75 bits
- [ ] Shannon/Fano 1940s, Huffman 1952
- [ ] Lengths ≈ -log_2 P(i)

### Ch 4 (Solomonoff Induction)
- [ ] K(x) definition (plain vs prefix)
- [ ] UTM and invariance (Turing 1936, Solomonoff/Kolmogorov 1964-65)
- [ ] M(x) = sum_{p: U(p)=x*} 2^{-|p|}
- [ ] Solomonoff 1964 attribution
- [ ] Semimeasure property
- [ ] M(x) >= 2^{-K(x)}
- [ ] Dominance theorem (c_mu * mu(x) <= M(x))
- [ ] Lower-semicomputable
- [ ] Halting problem connection

### Historical claims
- Turing 1936
- Cox 1946
- Shannon-Fano 1948-49?
- Huffman 1952
- Solomonoff 1964
- Kolmogorov 1965
- Chaitin's incompleteness?
- Levin coding theorem
