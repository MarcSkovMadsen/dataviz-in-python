import folium as fm
import panel as pn

from html import escape # noqa

pn.extension(sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="Folium",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
    plot = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain") #,  width='100%', height="50%")

    folium.Marker(
        location=[45.3288, -121.6625],
        popup="Mt. Hood Meadows",
        icon=folium.Icon(icon="cloud"),
    ).add_to(plot)

    folium.Marker(
        location=[45.3311, -121.7113],
        popup="Timberline Lodge",
        icon=folium.Icon(color="green"),
    ).add_to(plot)

    folium.Marker(
        location=[45.3300, -121.6823],
        popup="Some Other Location",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(plot)
    return plot

plot = get_plot(theme=theme, accent_base_color=accent_base_color)

def _get_properties(self):
    properties = pn.pane.HTML._get_properties(self)
    text = '' if self.object is None else self.object
    if hasattr(text, '_repr_html_'):
        text = text._repr_html_()
        before = '<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;">'
        after = '<div style="width:100%;height:100%"><div style="position:relative;width:100%;height:100%;padding-bottom:0%;">'
        text=text.replace(before, after)
    return dict(properties, text=escape(text))

pn.pane.plot.Folium._get_properties=_get_properties
component = pn.pane.plot.Folium(plot, min_height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()