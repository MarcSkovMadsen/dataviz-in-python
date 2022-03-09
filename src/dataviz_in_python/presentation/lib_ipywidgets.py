import panel as pn
import ipywidgets as ipw
import ipysheet

from dataviz_in_python import config

config.configure("ipywidgets", title="ipywidgets", url="lib_ipywidgets")

TEXT = """
# Ipywidgets: Interactive Visualization in the Browser

[Ipywidgets](https://ipywidgets.readthedocs.io/en/latest/) ipywidgets, also 
known as jupyter-widgets or simply widgets, are interactive HTML widgets for 
Jupyter notebooks, the IPython kernel and your 
[Panel](https://panel.holoviz.org) data app. 

A lot of data visualization widgets are built on top of ipywidgets.

Here we are displaying [Ipysheet](https://github.com/QuantStack/ipysheet)

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_ipywidgets.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_widget(accent_base_color="blue"):
    slider = pn.widgets.FloatSlider(value=10, start=0, end=100)
    sheet = ipysheet.sheet()

    ipysheet.cell(1, 1, "Input")
    cell3 = ipysheet.cell(1, 2, 42.0)
    ipysheet.cell(2, 1, "Output")
    cell_sum = ipysheet.cell(2, 2, 52.0, read_only=True, background_color=accent_base_color)

    @pn.depends(slider, cell3, watch=True)
    def calculate(a, b):
        cell_sum.value = a + b

    return pn.Column(slider, sheet)


widget = get_widget(accent_base_color=config.ACCENT_BASE_COLOR)
pn.panel(widget, height=700, sizing_mode="stretch_both").servable()
