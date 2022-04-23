#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import bar_chart_race as bcr


data = pd.read_csv('project (2).csv')


cols = ['Luna','Alba','Arad','Argeș','Bacău','Bihor','Bistrița-Năsăud','Botoșani','Brașov','Brăila','Buzău','Caraș-Severin','Călărași','Cluj','Constanța','Covasna','Dâmbovița','Dolj','Galați','Giurgiu','Gorj','Harghita','Hunedoara','Ialomița','Iași','Ilfov','Maramureș','Mehedinți','Mureș','Neamț','Olt','Prahova','Satu Mare','Sălaj','Sibiu','Suceava','Teleorman','Timiș','Tulcea','Vaslui','Vâlcea','Vrancea','Mun. București']
data.fillna(0, inplace=True)
subset = data[cols]
subset.set_index('Luna', inplace = True)


# In[54]:




bcr.bar_chart_race(
        
        df = subset,
        orientation='h',
        sort='desc',
        n_bars=8,
        fixed_order=False,
        fixed_max=True,
        steps_per_period=25,
        period_length=2500,
        interpolate_period=False,
        period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'},
        period_summary_func=lambda v, r: {'x': .98, 'y': .2,
                                          's': f'Total cazuri: {v.sum():,.0f}',
                                          'ha': 'right', 'size': 11},
        perpendicular_bar_func='median',
        title='Top cazuri Covid distribuite pe județe ',
        bar_size=.95,
        shared_fontdict=None,
        scale='linear',
        fig=None,
        writer=None,
        bar_kwargs={'alpha': .6},
        filter_column_colors=False)


# In[ ]:




