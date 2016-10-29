
# coding: utf-8

# ## Aspects of the CFSR Atmospheric Relative Angular Momentum Climatology
# ###### Inputs: aam_climo.csv (created using the AAM.ipynb found in this repository)
# ###### Data for this example obtained from: http://rda.ucar.edu/datasets/ds093.0/
# ###### 6-hourly pressure level data also available from: http://nomads.ncdc.noaa.gov/modeldata/cmd_pgbh/
# ###### Outputs: Several aspects of Earth's relative AAM budget
# ##### Created by: Dr. Victor Gensini (Fall 2016) | http://weather.cod.edu/~vgensini
# ##### More information can be found here: http://nbviewer.jupyter.org/github/vgensini/aam/blob/master/notebooks/AAM.ipynb
# ##### Relative AAM is calculated following:
# $$M_R=\frac{a^3}g\int\limits_{-\frac\pi2}^{\frac\pi2}\int\limits_0^{2\pi}\int\limits_1^{1000}\cos^2\phi{d}\phi{d}\lambda{udp}$$

# In[3]:

#Import neccessary Python libraries (this example uses Python 2.7)
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


# ### Read in relative AAM climatology file
# ##### 6-hourly climatology file (aam_climo.csv) which can be found in this repository: https://github.com/vgensini/aam
# ##### csv headers = date (YYYY-MM-DD-HH), aam (kg m^2 s^-1)

# In[4]:

df = pd.read_csv('/home/scripts/aam/aam_code/aam_climo.csv')
#print df
format = '%Y-%m-%d-%H'
df['date']=pd.to_datetime(df['date'], format=format)
df['yr'], df['mn'], df['dy'], df['hr'] = df['date'].dt.year, df['date'].dt.month, df['date'].dt.day, df['date'].dt.hour
df=df.set_index(pd.DatetimeIndex(df['date']))
df['aam15dy']=pd.Series.rolling(df['aam'],window=60,center=True).mean()
aam = go.Scatter( x=df['date'], y=df['aam'],name='AAM' )
aam15 = go.Scatter( x=df['date'], y=df['aam15dy'],name='15-Day Rolling Average' )
data = [aam, aam15]
layout = go.Layout(title='Global Relative AAM Climatology from CFSR',yaxis=dict(title='$$kg \\cdot m^2 \\cdot s^{-1}$$'))
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

