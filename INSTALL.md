### installation of eegmlwidgets

pip install git+https://github.com/eegml/eegmlwidgets

probably will work (not yet tested)

### Installing qgrid is can be a bit complicated as it must be installed both in the server process for the jupyter notebook and in the kernel process which is running in the notebook.


Here is how to set up a new conda environment "newenv" with this working as both the server and kernel.
```
$ conda create --name newenv   pandas jupyter jupyterlab ipywidgets ipykernel # add any other packages
$ conda activate newenv
(newenv)$ conda install qgrid -c conda-forge

# jupyter-widget/jupyterlab-manager and node js are required if not already installed
(newenv)$ conda install nodejs==10 -c conda-forge  # could probably use nodejs version 8 too

(newenv)$ jupyter labextension install @jupyter-widgets/jupyterlab-manager

# now install more recent qgrid2 widget set
(newenv)$ jupyter labextension install qgrid2

# make it so that other jupyter installs can see this environment
(newenv)$ python -m ipykernel install --name 'newenv' --display-name "newenv with qgrid"
```


### add bokeh support if you want
```
(newenv)$ conda install bokeh
(newenv)$ jupyter labextension install @bokeh/jupyter_bokeh
```

### jupyterhub specific setup
```
(newenv)$ pip install nbserverproxy
(newenv)$ jupyter serverextension enable --py nbserverproxy
```
- Note this also requires a proxy function to be used in kernel code. Need to find a reference for this

### This is what is installed on my system:
```
$ jupyter labextension list
JupyterLab v1.2.6
Known labextensions:
   app dir: /opt/conda/envs/jupyterhub/share/jupyter/lab
     @bokeh/jupyter_bokeh v1.2.0  enabled  OK
     @jupyter-widgets/jupyterlab-manager v1.1.0  enabled  OK
     jupyter-matplotlib v0.7.2  enabled  OK
     jupyterlab-jupytext v1.1.1  enabled  OK
     qgrid2 v1.1.3  enabled  OK
```										   
