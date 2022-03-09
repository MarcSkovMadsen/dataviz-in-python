import panel as pn

pn.extension("vega", sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Vega",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
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

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.Vega(plot, height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()