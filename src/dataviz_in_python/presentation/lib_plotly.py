import pandas as pd
import panel as pn

import plotly.express as px

from dataviz_in_python import config

config.configure("plotly", url="lib_plotly", title="Plotly")

TEXT = """
# Plotly: High Quality Plots in Python

[Plotly](https://plotly.com/python/)'s Python graphing library makes interactive, publication-quality graph.

Plotly is one of the most popular plotting libraries in Python. It has high quality documentation and produces very appealing plots.

One thing to note is that Plotly is a also a company that has a hard time finding funding for developing Plotly. 
Increasingly they focus on and market Dash the data app framework because there is a business case.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_plotly.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default", accent_base_color="blue"):
    data = pd.DataFrame(
        [
            ("Monday", 7),
            ("Tuesday", 4),
            ("Wednesday", 9),
            ("Thursday", 4),
            ("Friday", 4),
            ("Saturday", 4),
            ("Sunay", 4),
        ],
        columns=["Day", "Orders"],
    )

    if theme == "dark":
        plotly_template = "plotly_dark"
    else:
        plotly_template = "plotly"

    fig = px.line(
        data,
        x="Day",
        y="Orders",
        template=plotly_template,
        color_discrete_sequence=(accent_base_color,),
    )
    fig.update_traces(mode="lines+markers", marker=dict(size=10), line=dict(width=4))
    fig.layout.autosize = True
    return fig

plot = get_plot(theme=config.get_theme(), accent_base_color=config.ACCENT_BASE_COLOR)
pn.pane.Plotly(plot, config={"responsive": True}, sizing_mode="stretch_both", height=700).servable()