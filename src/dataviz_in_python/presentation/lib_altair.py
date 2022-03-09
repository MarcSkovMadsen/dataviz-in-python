import altair as alt
import panel as pn

from vega_datasets import data
from dataviz_in_python import config

config.configure("vega", title="Altair")

theme = config.get_theme()

TEXT = """
# Altair

Source: 
"""

def get_plot(theme="default"):
    if theme == "dark":
        alt.themes.enable("dark")
    else:
        alt.themes.enable("default")

    return (
        alt.Chart(data.cars())
        .mark_circle(size=60)
        .encode(
            x="Horsepower",
            y="Miles_per_Gallon",
            color="Origin",
            tooltip=["Name", "Origin", "Horsepower", "Miles_per_Gallon"],
        )
        .properties(
            height="container",
            width="container",
        )
        .interactive()
    )

plot = get_plot(theme=theme)
pn.pane.Vega(plot, height=800, sizing_mode="stretch_both").servable()