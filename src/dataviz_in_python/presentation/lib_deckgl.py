import panel as pn

pn.extension("deckgl", sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="DeckGL",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


# Please create your own access token one your own Access tokens page
# https://account.mapbox.com/access-tokens/
MAPBOX_KEY = "pk.eyJ1IjoicGFuZWxvcmciLCJhIjoiY2s1enA3ejhyMWhmZjNobjM1NXhtbWRrMyJ9.B_frQsAVepGIe-HiOJeqvQ"

def get_plot(theme="default", accent_base_color="blue"):
    if theme == "dark":
        deckgl_map_style = "mapbox://styles/mapbox/dark-v9"
    else:
        deckgl_map_style = "mapbox://styles/mapbox/light-v9"

    return {
        "initialViewState": {
            "bearing": -27.36,
            "latitude": 52.2323,
            "longitude": -1.415,
            "maxZoom": 15,
            "minZoom": 5,
            "pitch": 40.5,
            "zoom": 6,
        },
        "layers": [
            {
                "@@type": "HexagonLayer",
                "autoHighlight": True,
                "coverage": 1,
                "data": "https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv",
                "elevationRange": [0, 3000],
                "elevationScale": 50,
                "extruded": True,
                "getPosition": "@@=[lng, lat]",
                "id": "8a553b25-ef3a-489c-bbe2-e102d18a3211",
                "pickable": True,
            }
        ],
        "mapStyle": deckgl_map_style,
        "views": [{"@@type": "MapView", "controller": True}],
    }

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.DeckGL(
    plot, mapbox_api_key=MAPBOX_KEY, sizing_mode="stretch_both", height=500
)
template.main.append(component)
template.servable()