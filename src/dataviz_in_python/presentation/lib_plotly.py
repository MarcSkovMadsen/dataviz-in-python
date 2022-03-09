import pandas as pd
import panel as pn

import plotly.express as px

pn.extension("plotly", sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Plotly",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


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

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.Plotly(plot, config={"responsive": True})
template.main.append(component)
template.servable()