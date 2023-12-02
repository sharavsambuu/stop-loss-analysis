#%%
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt


#%%


#%%
mu   = 0
sig  = 0.2 / np.sqrt(252)
stop = 0.05
n    = 50000

#%%


#%%
no_stop_df      = pd.DataFrame(index=range(n), columns=['No Stop Returns'     ])
with_stop_df    = pd.DataFrame(index=range(n), columns=['With Stop Returns'   ])
pretend_stop_df = pd.DataFrame(index=range(n), columns=['Pretend Stop Returns'])


#%%


#%%
for i in range(n):
    prices = np.cumprod(1 + np.random.normal(mu, sig, 10))
    no_stop_df.iloc[i] = prices[9] - 1
    if np.min(prices) < 1 - stop:
        with_stop_df.iloc[i]    = -stop
        pretend_stop_df.iloc[i] = np.nan
    else:
        with_stop_df.iloc[i]    = prices[9] - 1
        pretend_stop_df.iloc[i] = with_stop_df.iloc[i]

#%%
result_df = pd.concat([no_stop_df, with_stop_df, pretend_stop_df], axis=1)
result_df['No Stop Returns'     ] = pd.to_numeric(result_df['No Stop Returns'     ])
result_df['Pretend Stop Returns'] = pd.to_numeric(result_df['Pretend Stop Returns'])
result_df['With Stop Returns'   ] = pd.to_numeric(result_df['With Stop Returns'   ])


#%%
result_df.info()


#%%


#%%
fig, ax = plt.subplots()
fig.suptitle("Expectation of Stop Loss")
ax.hist(result_df['No Stop Returns'     ], bins=500, color='orange', label="No Stop Loss")
ax.hist(result_df['Pretend Stop Returns'], bins=500, color='black' , label="Expectation of Stop Loss")
ax.legend();


#%%
fig, ax = plt.subplots()
fig.suptitle("Actual impact of Stop Loss")
ax.hist(result_df['No Stop Returns'  ], bins=500, color='orange', label="No Stop Loss")
ax.hist(result_df['With Stop Returns'], bins=500, color='black' , label="With Stop Loss")
ax.legend();


#%%


#%%

