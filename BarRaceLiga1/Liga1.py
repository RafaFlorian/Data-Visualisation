#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import bar_chart_race as bcr


data = pd.read_csv('Liga1DataSet.csv')
data.fillna(0, inplace=True)

cols = ['Season','FC Universitatea Craiova','Dinamo Bucureşti','Inter Sibiu','CSA Steaua București','Gloria Bistrita','FC Politehnica Timisoara','Petrolul Ploiesti','Arges Pitesti','Fc Brasov','Universitatea Cluj','Politehnica Iasi','Farul Constanta','Rapid Bucuresti','Astra Ploieşti','Oţelul Galaţi','Gaz Metan Mediaş','CFR Cluj','FC Vaslui','UTA Arad']
subset = data[cols]
subset.set_index('Season', inplace = True)
cum_sum_df = subset.cumsum(axis = 1)
cum_sum_df.tail()


# In[ ]:



cum_sum_df.tail()


bcr.bar_chart_race(
        
        df = cum_sum_df,
        img_label_folder = 'img',
        orientation='h',
        sort='desc',
        n_bars=8,
        fixed_order=False,
        fixed_max=True,
        steps_per_period=20,
        period_length=200,
        interpolate_period=False,
        period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'},
        period_summary_func=lambda v, r: {'x': .98, 'y': .2,
                                          's': f'Total points: {v.sum():,.0f}',
                                          'ha': 'right', 'size': 11},
        perpendicular_bar_func='median',
        title='Liga1 Points since 1990',
        bar_size=.95,
        shared_fontdict=None,
        scale='linear',
        fig=None,
        writer=None,
        bar_kwargs={'alpha': .6},
        filter_column_colors=False)


# In[ ]:




