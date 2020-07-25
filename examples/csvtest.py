# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: pytorch 1.5+
#     language: python
#     name: pyt15
# ---

# %% [markdown]
# ### CsvGridWidget
# CsvGridWidget is meant to be a quick way to visualize and edit a csv file using pandas, ipywidgets and qgrid.
# It should only be used if you have a backup of the csv file because it will over-write the changes with the save button

# %%
# %load_ext autoreload
# %autoreload 2

# %%
import eegmlwidgets                                             
                                                       
eegmlwidgets.wide_notebook_display()   # allow jupyternotebook to use full width      

# %%
datacsv = eegmlwidgets.CsvGridWidget("SalesJan2009.csv")

# %%
datacsv.show() # doupble click a cell to make changes, click save to save the grid state back to the csv file, note if you have filtered, this will delete data!

# %% [markdown]
# To manipulate the underlying dataframe directly, get the DataFrame from
# datacsv.df

# %%
# example
datacsv.df.head()

# %%

# %%
import qgrid
qgrid.__version__

# %%
import ipywidgets
ipywidgets.__version__

# %%
# thanks to this article for the source of the example csv:
# source url https://support.spatialkey.com/spatialkey-sample-csv-data/ 
# # # !wget http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv 

# %%
