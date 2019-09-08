# Cognitive Computing 
Cognitive computing 與傳統的計算機計算技術不同，不再只是數學、邏輯的判斷，而是以人類思考的角度來閱讀資料並計算、提出假設。

例如 Congnitive computing 透過分析 natural language 的文法、語意、文化與對話情境，來進一步了解句子的真正意義。

Cognitive computing systems 與 conventional computing systems 的不同 :
* Read and interpret unstructured data, understanding not just the meaning of words but also the intent and context in which they are used.
* Reason about problems in a way that humans reason and make decisions.
* Learn over time from their interactions with humans and keep getting smarter.

> [How to get started with cognitive technology](https://www.ibm.com/watson/advantage-reports/getting-started-cognitive-technology.html)


# Terminology and Related Concepts
以下是學習 AI 時，常看到的名詞解釋。

## Artificial Intelligence
利用一堆電腦科學來模擬人類智慧的行為，例如用於 :
* Planning
* Learning
* Reasoning
* Problem-Solving
* Knowledge
* Perception
* Motion
* Manipulation
* Social Intelligence
* Creativity

## Machine Learning
是 AI 的底下分支的一種，透過演算法及大量解析 data 來訓練機器，使機器能夠因此自行做出判斷，而不需特別額外設計 rule-based algorithms。

傳統的 programming 方式，會先定義好規則，讓程式跑過演算法，看看是否為對的答案。

而 machine-learning 則是先給定好 input 和應該產生的 result，來得到 rules 及 models，之後再以此模型讓機器學習。

機器學習依賴定義好的 behavioral rules 來檢驗數據中有沒有類似出現過的 common patterns。

舉幾個例 :
* 事先輸入病人身體資料，以及是否有糖尿病，讓機器不斷學習新的資料，改進預測糖尿病的機率。
* 事先輸入圖片，並且標籤圖片的名稱，讓機器學習並有辦法辨識圖片。

機器學習分為三大種類 :
1. Supervised Learning
   * 指的是透過事先 labeled 過的 data 來訓練演算法，給的 data 越多，在之後判斷時會越精確。
     * 上面的例子皆為 supervised learning
2. Unsupervised Learning
   * 直接用未 labeled 的 data 來訓練演算法，讓機器自行在 data 中尋找 patterns，並分組標籤。
     * 例如給予一堆不知名的 network stream，讓機器自己去區分，找到一般網路、外部網路、甚至是惡意網路。
3. Reinforcement Learning
   * 事先定義好 state, desired goal, constraints，然後訓練演算法自行去找到解決辦法完成目標。
     * 常見於 chess 或 navigate an obstacle path

在 machine learning 中，通常會把得到的 big data set 切割為三類 :
* Training
  * 用來訓練演算法的資料。
* Validation
  * 用來驗證是否訓練成功，以及將演算法加強的資料。
* Test Sets
  * 是一些從來沒丟進給演算法訓練的資料，來測試演算法的準確性。


Supervised learning 又分為三大種類 :

### Regression
Regression 用於預測持續變化的數值，透過觀察 feature x 來判斷 result y，而這個 y 將會持續變化。

### Neural Networks
Neural Networks 模擬人腦結構。

### Classification
給予 algorithm 一堆 `features` data x 學習 (Training)，並產生對應的 `result` y 標籤，之後再進行測試、觀察完全沒看過的資料，得到準確度。

y 標籤不一定只能有兩個 (true or false)，可以有多個，例如要知道菜單是適合哪國人吃的 (Chinese, Japanese, Indian, Thai ...)

Classification 又分為多種方法來實作 :
* Deicison Tree
* Support vector machines
* Logistic regression
* Random forests

> 那麼是如何學習 (Training) 的呢 ?
>> Training 會使用一些 learning algorithm 來決定我們的 feature 對應的 result 為何，例如給他看一些資料並告訴他是 True，給他看另一些資料並告訴他是 False，訓練他直到可以獨立判斷 True or False 為止。


## Deep Learning
Deep learning 是 machine learning 的一種特殊形態，他透過 layers algorithms 創建 layered neural networks 模擬人類的 decision-making。

Deep learning 能夠分類並標籤 data ，並且從中找到 patterns，讓 AI 能夠在工作中持續的學習，並提高準確性，
因此 deep learning 可以從 unstructured data 如 image, video, audio 來進行學習。

Deep learning 並不是直接將 input 配一個 output，而是在中間加入一或多層的 processing units。

在創建一個 deep learning algorithm 時，開發者會先想好 layer 數，以及每一個輸出接到下一個輸入的 function。

Deep learning 在以下的領域都展現了不錯的表現 :
* Image captioning
* Voice recognition & transcription
* Facial recognition
* Medical imaging
* Language translation
* Driverless cars


## Neural Networks
是利用一群 small computing units 稱作 neurons，他們吃下的 data，並且不斷的往下學習。

Neural networks 通常能將資料分析至非常深度的層次，這也是為什麼 deep learning 可以將大量資料有效分析，而其他 machine learning algorithms 會隨著資料量變大而停滯無法工作。

我們稱有多個 neurons 在一起的為一個 layer，資料經過 input layer 並由 `Activation functions` 運算最終輸出至 output layer。
若 input & output 中間有一個以上的 hidden layers 稱之為 `Deep neural network`。
而 `Perceptrons` 為最簡單也最古老的 neural networks，他的 input node 會直接連接至 output node。

Input 或 hidden layer 會將 input value 取 weight 或 sum 並計算完傳至下一個 layer，而 hidden 或 output node 有一個 property 叫作 `bias`。

這個 `bias` 為一種特殊的 weight，他會連其他 node 的值也參考進去。

而 `Activation functions` 將會把 input 和 bias 一同考慮進去，決定出真正有幫助的 output 給下一個 node。

### Backpropogation
Neural networks 透過 backpropogation 進行學習，利用已知 input 對應 output `a` 的 training data，
試著先透過 input 計算出 output `b`，再利用 error function 來計算 `a` 和 `b` 的差異有多少，
再來重複調整並且減少錯誤。


### Convolutional Neural Networks (CNNs)
CNNs 是一種 multilayer neural networks，其中 convolution 是一種數學運算，
意思是將 function apply 至下一個 function，而 result 就是兩個 function 的 mixture。

Convolution 可以很棒的偵測一些 simple structure，
並且將這些 simple features 組合成 complex features。

常用於 Image processing, video recognition, natural language processing ...

### Recurrent Neural Networks (RNNs)
CNNs 在一些特定情況下，若前一個 node 提供的 information 不符合 context，可能無法產生正確的結果。

而 RNNs 可以讓 information 得到延伸，每個 layer 代表的都是不同時段的 observation。

> Recurrent Neural Networks or RNNs are multi-layered neural networks that perform the same task for every element of a sequence, with prior outputs feeding subsequent stage inputs. RNNs make use of information in long sequences, each layer of the network representing the observation at a certain time.

## Data Science
和 AI 是兩種跨學科的領域，data science 透過很多方法，如 mathematics, statistics, machine learning 等，來解析資料得到一些肉眼無法得到的知識，並作為決策判斷。但他跟 AI 一樣都使用到了 Big Data 作為依據。


# Key Fields of Application in AI

## Natural Language Processing
Natural language is one of the **most complex** data for machine learning to work with. Natural language is highly contextualized, moreover humans view and use language conceptually rather than literally. Other types of data, be it **auditory** or **visual dat**a, have some form of **discernible patterns**, making it easier to work with than natural language.

Natural language processing is broken down into many subcategories related to audio and visual tasks.
* Speech to text
* Text to speech (Speech Synthesis)

## Computer Vision
Computer vision is one of the technologies that enables the digital world to interact with the physical world.

The field of computer vision focuses on replicating parts of the complexity of the human visual system, and enabling computers to identify and process objects in images and videos, in the same way humans do.

Computer vision has taken great leaps in recent years and surpasses humans in tasks related to detecting and labeling objects, thanks to advances in **deep learning** and **neural networks**. 
* self-driving cars
  * Self-driving vehicles fuse laser data, vision data, and radar data to create a three-dimensional view of their driving environment helping them make accurate decisions on the road.
* facial recognition
* augmented and mixed reality

> **Visual attention** is a limitation of human vision that computer vision can help makeup for. 
> Human vision cannot attend to everything in its visual field, all at the same time, like computer vision can.