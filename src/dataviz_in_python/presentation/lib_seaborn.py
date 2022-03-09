import matplotlib.pyplot as plt

import panel as pn
import seaborn as sns

penguins = sns.load_dataset("penguins")

from dataviz_in_python import config

config.configure(url="lib_seaborn", title="Seaborn")

TEXT = """
# Seaborn: Statistical data visualization

[Seaborn](https://seaborn.pydata.org/) Seaborn is a Python data visualization
library based on [matplotlib](lib_matplotlib). It provides a high-level 
interface for drawing attractive and informative statistical graphics.

Please note the lead developer is tweeting about upcoming, major changes to
the api.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_seaborn.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default", accent_base_color="blue"):
    if theme == "dark":
        sns.set_style("darkgrid")
        plt.style.use("dark_background")
    else:
        plt.style.use("default")
        sns.set_style("whitegrid")

    plot = sns.displot(penguins, x="flipper_length_mm", color=accent_base_color)
    fig0 = plot.fig
    fig0.set_size_inches(16, 8)
    return fig0


plot = get_plot(theme=config.get_theme(), accent_base_color=config.ACCENT_BASE_COLOR)
pn.pane.Matplotlib(plot, height=700, sizing_mode="stretch_both").servable()
