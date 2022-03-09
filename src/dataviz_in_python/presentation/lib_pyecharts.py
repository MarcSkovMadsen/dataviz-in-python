import json
import panel as pn

from pyecharts.charts import Bar

pn.extension("echarts", sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="PyECharts",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
    plot = (
        Bar()
        .add_xaxis(["Helicoptors", "Planes", "Air Ballons"])
        .add_yaxis("Total In Flight", [50, 75, 25], color=accent_base_color)
    )

    # Workaround to make plot responsive
    plot = json.loads(plot.dump_options())
    plot["responsive"] = True
    return plot

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.ECharts(plot, min_height=500, sizing_mode="stretch_both", theme=theme)
template.main.append(component)
template.servable()