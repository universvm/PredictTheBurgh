# PredictTheBurgh

## Inspiration
We wanted to understand whether there are predictable patterns in the movement of stock prices, and whether deep neural network models would be able to learn these patterns.

## What it does
We applied state-of-the-art RNNs using LSTM and GRU units to the task of stock price prediction, as well as CNNs. We sourced our own high frequency intraday data.

## Challenges we ran into
Obtaining high granularity intraday data was our main challenge: the best freely available data is only day OHLC candles (Open-High-Low-Close). 

We observed early on that intraday movement is too significant to ignore: exclusively modelling closing prices misses out on most of the potential returns.

Further problems were found in the published code that we were able to obtain that already implemented these models. We discovered many unreasonable assumptions in the training and testing of them. 

## How we built it
We prototyped in Jupyter notebooks using Keras as a high level interface to Tensorflow. We tested several RNN models with LSTM and GRU units and also tested a Conv1d with dropout.

We acquired our data from a popular platform for strategy testing.

## Accomplishments that we're proud of
We are happy about how quickly we explored and iterated over ideas, and much we learned as a result. Our findings are initial for now, but this offers a clear direction for future research.

We were astonished to find out about the low standards of scientific publishing in this domain and we believe more rigorous standards should be enforced. 

## What we learned
We learned that modelling the stock price itself is a fool's errand. While price movements may have an autoregressive component, the majority of the movement clearly comes from external events. Attempting to connect events and movements is a hard task that requires high quality data sources and an exploration of different models.

## What's next for PredictTheBurgh
We deem our findings worthy of dissemination, and so will aim to publish them as a paper and/or blog post.

Our resolve is to continue researching methods not just for stock price prediction, but methods that would lead to successful Systematic Trading Strategies. For this, the next step is to develop a flexible backtesting framework. Having tried out existing ones for Python (Zipline, backtrader, bt, etc.), we find them lacking in flexibility.
