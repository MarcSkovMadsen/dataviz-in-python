import panel as pn

from dataviz_in_python import config

config.configure(url="lib_vega", title="Vega & Vega-Lite")

TEXT = """
# Vega: A Grammar of Graphics for Python

[Vega](https://vega.github.io/) is a declarative format for creating, saving, and sharing 
visualization designs. With Vega, visualizations are described in JSON, and 
generate interactive views using either HTML5 Canvas or SVG.

Please note that **you should be using the higher level Vega-Lite format.**

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_vega.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default"):
    vegalite = {
        "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
        "data": {
            "url": "https://raw.githubusercontent.com/vega/vega/master/docs/data/barley.json"
        },
        "mark": {"type": "bar", "tooltip": True},
        "width": "container",
        "height": "container",
        "encoding": {
            "x": {"aggregate": "sum", "field": "yield", "type": "quantitative"},
            "y": {"field": "variety", "type": "nominal"},
            "color": {"field": "site", "type": "nominal"},
        },
    }

    if theme == "dark":
        vegalite["config"] = {
            "background": "#333",
            "title": {"color": "#fff"},
            "style": {"guide-label": {"fill": "#fff"}, "guide-title": {"fill": "#fff"}},
            "axis": {"domainColor": "#fff", "gridColor": "#888", "tickColor": "#fff"},
        }
    return vegalite

plot = get_plot(theme=config.get_theme())
pn.pane.Vega(plot, height=700, sizing_mode="stretch_both").servable()