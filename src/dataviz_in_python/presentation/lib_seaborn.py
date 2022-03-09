import matplotlib.pyplot as plt

import panel as pn
import seaborn as sns

pn.extension(sizing_mode="stretch_width")

penguins = sns.load_dataset("penguins")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Seaborn",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
    if theme == "dark":
        sns.set_style("darkgrid")
        plt.style.use("dark_background")
    else:
        plt.style.use("default")
        sns.set_style("whitegrid")

    plot = sns.displot(penguins, x="flipper_length_mm", color=accent_base_color)
    fig0 = plot.fig
    fig0.set_size_inches(8, 4)
    return fig0

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.Matplotlib(plot, sizing_mode="stretch_both")
template.main.append(component)
template.servable()