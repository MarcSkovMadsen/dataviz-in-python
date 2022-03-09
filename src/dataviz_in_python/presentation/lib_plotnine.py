import matplotlib.pyplot as plt
import panel as pn

from plotnine import (aes, element_rect, facet_wrap, geom_point, ggplot, stat_smooth, themes)
from plotnine.data import mtcars

pn.extension(sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Plotnine",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
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

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.Matplotlib(plot, height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()