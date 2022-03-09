import matplotlib.pyplot as plt
import panel as pn

from plotnine import aes, element_rect, facet_wrap, geom_point, ggplot, stat_smooth, themes
from plotnine.data import mtcars
from dataviz_in_python import config

config.configure(url="lib_plotnine", title="Plotnine")

TEXT = """
# Plotnine: A Grammar of Graphics for Python

[Plotnine](https://plotnine.readthedocs.io/en/stable/) is an implementation of a grammar of graphics in Python, it is based on [ggplot2](https://ggplot2.tidyverse.org/). The grammar allows users to compose plots by explicitly mapping data to the visual objects that make up the plot. Its based on Matplotlib.

[Source Code](https://github.com/MarcSkovMadsen/dataviz-in-python/blob/main/src/dataviz_in_python/presentation/lib_plotnine.py)
"""
pn.panel(TEXT, css_classes=[config.TEXT_CLASS]).servable()


def get_plot(theme="default"):
    plt.style.use("default")
    if theme == "dark":
        plotnine_theme = themes.theme_dark() + themes.theme(
            plot_background=element_rect(fill="black", alpha=0)
        )
    else:
        plotnine_theme = themes.theme_xkcd()

    plot = (
        (
            ggplot(mtcars, aes("wt", "mpg", color="factor(gear)"))
            + geom_point()
            + stat_smooth(method="lm")
            + facet_wrap("~gear")
        )
        + plotnine_theme
        + themes.theme(figure_size=(16, 8))
    )
    return plot.draw()


plot = get_plot(theme=config.get_theme())

pn.pane.Matplotlib(plot, height=700, sizing_mode="stretch_both").servable()
