# First Week

## A New Golden Age for Computer Architecture

> 中文文章
>
> * [https://www.jiqizhixin.com/articles/2017-10-31-15](https://www.jiqizhixin.com/articles/2017-10-31-15)
> * [https://www.jiqizhixin.com/articles/2019-01-30-12](https://www.jiqizhixin.com/articles/2019-01-30-12)

* [Article](https://cacm.acm.org/magazines/2019/2/234352-a-new-golden-age-for-computer-architecture/fulltext)
* [Notes](https://cyyeh.github.io/new-golden-age-for-computer-architecture/)

### 歷史

* IBM 藉由 micro instruction 實現 [**Microprogramming**](https://www.quora.com/What-is-microinstruction) 讓單個 ISA 解決他所有的產品
* 設計 Control unit 為一大挑戰
* 此時的 ISA 還是為 [**CISC 架構**](https://zh.wikipedia.org/zh-tw/%E5%A4%8D%E6%9D%82%E6%8C%87%E4%BB%A4%E9%9B%86)
* 電晶體及 RAM 的竄起，CISC 指令能夠更加複雜，出現了 [minicomputer](https://zh.wikipedia.org/wiki/%E5%B0%8F%E5%9E%8B%E8%AE%A1%E7%AE%97%E6%9C%BA) 及 [**Microprocessor**](https://zh.wikipedia.org/wiki/%E5%BE%AE%E5%A4%84%E7%90%86%E5%99%A8) \(還是 CISC\)
* 出現了幾乎可以取代 CISC 的 [**RISC**](https://zh.wikipedia.org/zh-tw/%E7%B2%BE%E7%AE%80%E6%8C%87%E4%BB%A4%E9%9B%86)
* RISC = RAM for cache, simple ISA, better chip integration, better load-store ISAs
* 出現 RISC 贏過 CISC 的公式 \(4X 快\)

  $$
  \frac{\text{Time}}{\text{Program}} = \frac{\text{Instructions}}{\text{Program}} \times 
  \frac{\text{Clock cycles}}{\text{Instructions}} \times \frac{\text{Time}}{\text{Clock cycles}}
  $$

* 在 PC 時代還是 x86 主宰市場，但在後 PC 時代已經是 RISC 的天下 \(99% Processors\)
* 出現了 [**VLIW**](https://zh.wikipedia.org/zh-tw/%E8%B6%85%E9%95%BF%E6%8C%87%E4%BB%A4%E5%AD%97) 說不定可以成為下一個 RISC
* 但 VLIW 被證實有太多 issues，不過還是活躍於 [**Embedded DSP**](https://baike.baidu.com/item/%E5%B5%8C%E5%85%A5%E5%BC%8FDSP%E5%A4%84%E7%90%86%E5%99%A8) 市場
* CISC 已經 30 年沒有突破，VLIW 是 15 年，目前還是 RISC 的天下

### 挑戰

* End of [**Dennard scaling**](https://en.wikipedia.org/wiki/Dennard_scaling) and [**Moore’s Law**](https://zh.wikipedia.org/wiki/%E6%91%A9%E5%B0%94%E5%AE%9A%E5%BE%8B) =&gt; Power 吃重、Transistor 不再進化
* End of the uniprocessor era
* 市場改變 =&gt; 從 PC/Server 變成 IoT/Mobile/Clouds
* 資訊安全如 Meltdown & Spectre

### 未來

* Software Programmer 在撰寫程式前更需要知道硬體運作
* 或是找出方法讓 Python 也可以 run 的跟 C with compiler + HW 一樣
* Hardware 只剩 [**Domain Specific Architectures \(DSAs\)**](https://www.mem.com.tw/arti.php?sn=1811300007) 這條路可走 : 針對應用領域做最佳化的處理器架構
  * DSA 不是針對單個應用，而是整個應用 domain
  * 需要有該應用 domain 的深度認識 
  * 現有例子為 : neural network processors for ML \(TPU\), GPUs for graphics, Programmable network switches
* 搭配的是 [**Domain-specific language \(DSL\)**](https://en.wikipedia.org/wiki/Domain-specific_language)
  * 使用相應的語言來處理適合的 task
  * OpenGL, Tensorflow, P4
* 制定全新的開源 ISA 基礎 : [**RISC-V**](https://zh.wikipedia.org/zh-tw/RISC-V)

## Great Ideas in Computer Architecture

* [Video](https://www.youtube.com/watch?v=u_hXH5-tbM4)
* [Slide](https://drive.google.com/open?id=1iwOSP_MJj8hP5rshTT1jc78lY9I6aM0P)

### Abstraction \(Layers of Representation/Interpretation\)

High-level language program 如何藉由 Compiler, Assembler, Machine interpretation, Architecture implementation 來實現

以及其中牽涉到的 physics, electrons and quarks 等基礎原理是怎麼實作進來的

### Moore’s Law

David House 提出 每 18 個月晶片的效能將會提高一倍

### Principle of Locality/Memory Hierarchy

Jim Gray 定義了一系列譬喻 : **"How far away is the data ?"**

* Register : Head
* On-chip cache : Room
* On-board cache : Campus
* Memory : Sacramento \(薩克拉門托城市\)
* Disk : Pluto \(冥王星\)
* Tape : Andromeda \(仙女座\)

而在 memory hierarchy 中，金字塔越往下代表 **Cheaper, Bigger, Slower**

* CPU
  * Processor register
* CPU Cache
  * L1, L2, L3
* Physical memory
  * RAM
* Solid state memory
  * SSD, Flash
* Virtual memory
  * Hard drives

### Parallelism

* [Pipeline](https://zh.wikipedia.org/zh-tw/%E6%8C%87%E4%BB%A4%E7%AE%A1%E7%B7%9A%E5%8C%96)
* [Fork and join](https://en.wikipedia.org/wiki/Fork%E2%80%93join_model)
* [Data parallelism](https://zh.wikipedia.org/zh-tw/%E8%B3%87%E6%96%99%E5%B9%B3%E8%A1%8C)
  * like Google docs

但 ! [**Ahdahl's law**](https://zh.wikipedia.org/zh-tw/%E9%98%BF%E5%A7%86%E8%BE%BE%E5%B0%94%E5%AE%9A%E5%BE%8B) 指出 : **並不是平行化的越多，如 X 倍，執行速度就 X 倍**

要考慮工作中的 **Serial part** 是不能平行的 !

### Performance Measurement & Improvement

Great Performance measurement gives you great performance.

所以需要一個好的 benchmark 來測試效能 !

### Dependability via Redundancy

利用 Redundancy 讓系統在某一個區塊錯誤時不會整個崩潰

在 datacenter, disks \(RAID\), memory bits \(ECC\) 都可以看到這樣的作法

## Number representation

* [Slide](https://drive.google.com/open?id=1XzxbLSMOvP6BA18LYV60FUf64E9f3dSf)
* [補充 - 解讀計算機編碼](https://hackmd.io/@sysprog/rylUqXLsm)

#### Bits can represent anything

* Characters
* Logical values
* Pi

  $$
  N \text{ bits} \iff \text{ at most } 2^N \text{ things}
  $$

#### Base 10

$$
3271_{10} = (3 \times 10^3) + (2 \times 10^2) + (7 \times 10^1) + (1 \times 10^0)
$$

#### Base 2

$$
\begin{aligned}
1101_2 &= (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)\\
&= 8 + 4 + 0 + 1 \\
&= 13
\end{aligned}
$$

#### Base 16

$$
\begin{aligned}
0xA5 = A5_{16} &= (10 \times 16^1) + (5 \times 16^0)\\
&= 160 + 5 \\
&= 165
\end{aligned}
$$

#### Decimal to Binary

將二進位由大到小從左到右寫出

觀察是否可以被最大的減去，由左往右直到 1 為止 :

![](../.gitbook/assets/decimal_to_binary.png)

#### Decimal to Hexadecimal

跟上面差不多 :

![](../.gitbook/assets/decimal_to_hex%20%281%29.png)

#### Binary to Hexadecimal

將 二進位補滿 4 個數一組，再轉換每組數字 :

$$
\begin{aligned}
\text{e.g., 11110 to hex : }&\\
11110 &= 0001 1110\\
0001 &= 1\\
1110 &= 8 + 4 + 2 = 14 = E\\
11110 &= 1E
\end{aligned}
$$

#### Hexadecimal to Binary

跟上面相反，把數字拆開成為 4 個一組的二進位數，再把前面多餘的 0 刪掉 :

$$
\begin{aligned}
\text{e.g., 1E to binary : }&\\
1 &= 0001\\
E &= 14 = 8 + 4 + 2 + 0 = 1110\\
1E &= 0001 1110\\
&= 11110
\end{aligned}
$$

#### Binary Operations

Add, subtract is same as decimal.

#### Binary Overflow

當兩個 binary 數值相加超過 hardware 能承受最大的 bits \(11...1\) 時，就會發生 Overflow

#### Binary Negative numbers

**Sign and Magnitude**

* 在原本沒有負數的 unsigned numbers 取他的最左 bit 做為正負號 \(0001 =&gt; 1001\)
* 若有 N bits 則範圍為 \(減一是因為 0\)

  $$-(2^{N-1} - 1) \sim (2^{N-1} - 1)$$ 

* 因為要保證最左不參與加減法，所以電路複雜
* 而且這樣會有兩個 0 \(負的跟正的各一\)

**Ones' complement**

* 將所有的數字反轉 \(0001 =&gt; 1110\)
* 若有 N bits 則範圍為 \(減一是因為 0\)

  $$-(2^{N-1} - 1) \sim (2^{N-1} - 1)$$

* 電路設計變簡單
* 需要循環進位的電路 \(將 overflow 加回最低位\)
* 一樣有兩個 0 \(正負各一\)

**Two's complement**

* 利用在 negative, complement + 1 來解決兩個 0 的 "Overlap" \(0001 =&gt; 1110 =&gt; 1111\)
* 範圍為

  $$-(2^{N-1}) \sim (2^{N-1}-1)$$

* 因為解決了 0 的問題，看起來像是負數比正數還要多一個
* 負數可以用二的 power 來表示，公式為

  $$d_{31} \times {\color{red}-(2^{31})} + d_{30} \times 2^{30} + \cdots + d_1 \times 2^1 + d_0 \times 2^0$$

* 例如 1101 :

  $$
  \begin{aligned}
  &= 1 \times -(2^{3}) + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0\\
  &= -(2^3) + 2^2 + 0 + 2^0\\
  &= -8 + 4 + 0 + 1\\
  &= -3
  \end{aligned}
  $$

## Floating point

* [Slide](https://drive.google.com/open?id=1LNTzUuPr8vu_SW0woLGP_mp3fDg2CBxE)
* [補充 - 數值系統](https://hackmd.io/@sysprog/BkRKhQGae?type=view)

#### Fraction representation

representation 方式跟 decimal 差不多 : 而轉換方式如下 :

$$
10.1010_2 = 1\times2^1 + 1\times2^{-1} + 1\times2^{-3} = 2.625_{10}
$$

加法 :

multiplication

#### Scientific Notation

#### Floating Point Representation

#### IEEE 754 Floating Point Standard

**Representation for ± ∞**

**Representation for 0**

**Special Numbers**

**NaN**

## Memory management

* [Slide](https://drive.google.com/open?id=19Lvl-tne4H_dPosIeGAZmEW1pdadFjez)
* [Video](https://www.youtube.com/watch?v=fhEE4J4QCps&feature=youtu.be)

#### struct

#### linked list

#### global

#### 3 pools

#### memory management

**stack**

**Heap**

**malloc**

3 way find free space first, next, best fit

