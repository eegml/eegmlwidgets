import csv
import datetime

import pandas as pd
import qgrid
import ipywidgets


class CsvGridWidget:
    """                                                                         
    Idea is to make it easy to view and edit a csv file (or anyting loadable by pandas)                 
    in the jupyter notebook or jupyter lab notebook.

    TODO: it is harder to get to work in jupyterlab/jupyterhub
    TODO: need to test round trip process especially around types like dates/times
    """

    def __init__(self, file_name, qgrid_precision=2, **kwargs_read_csv):
        
        self.file_name = file_name
        default_options = {"keep_default_na": False}
        default_options.update(kwargs_read_csv)
        self._read_csv_options = (
            default_options  # save this for later to use when writing (TODO!!!)
        )

        self.df = pd.read_csv(file_name, **default_options)
        # gui

        self.qgrid_widget = qgrid.show_grid(self.df, show_toolbar=True, precision=qgrid_precision)
        # save button
        self.savebutton = ipywidgets.Button(
            description="Save",
            tooltip="click to save and resyncronize the dataframe back to file",
            disabled=False,
        )
        # define callback for save button
        def on_save_button_clicked(b):
            print(
                f"Saved {self.file_name} {str(datetime.datetime.now())}"
            )  # type(b), repr(b))
            self.save()
            
        self.savebutton.on_click(on_save_button_clicked)
        
        # container/layout
        self.topwidget = ipywidgets.VBox([self.qgrid_widget, self.savebutton])

    def save(self):
        updated_df = self.qgrid_widget.get_changed_df()
        updated_df.to_csv(self.file_name, index=False, quoting=csv.QUOTE_NONNUMERIC)
        self.df = updated_df

    def show(self):
        """display the widget in the notebook"""
        display(self.topwidget)
