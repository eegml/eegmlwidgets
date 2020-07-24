# package placeholder
from IPython.core.display import display, HTML


from .gridwidgets import CsvGridWidget

__version__ = "0.1.0"


def wide_notebook_display():
    """make jupyter notebook use full width of display"""
    display(HTML("<style>.container { width:100% !important; }</style>"))      
