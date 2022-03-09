import pydeck
import panel as pn

pn.extension("deckgl", sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="PyDeck",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
    LAND_COVER = [
        [[-123.0, 49.196], [-123.0, 49.324], [-123.306, 49.324], [-123.306, 49.196]]
    ]
    polygon = pydeck.Layer(
        "PolygonLayer",
        LAND_COVER,
        stroked=False,
        # processes the data as a flat longitude-latitude pair
        get_polygon="-",
        get_fill_color=[0, 0, 0, 20],
    )

    DATA_URL = "https://raw.githubusercontent.com/uber-common/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
    geojson = pydeck.Layer(
        "GeoJsonLayer",
        DATA_URL,
        opacity=0.8,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True,
        get_elevation="properties.valuePerSqm / 20",
        get_fill_color="[255, 255, properties.growth * 255]",
        get_line_color=[255, 255, 255],
        pickable=True,
    )

    if theme == "dark":
        deckgl_map_style = "mapbox://styles/mapbox/dark-v9"
    else:
        deckgl_map_style = "mapbox://styles/mapbox/light-v9"
    MAPBOX_KEY = "pk.eyJ1IjoicGFuZWxvcmciLCJhIjoiY2s1enA3ejhyMWhmZjNobjM1NXhtbWRrMyJ9.B_frQsAVepGIe-HiOJeqvQ"
    INITIAL_VIEW_STATE = pydeck.ViewState(
        latitude=49.254, longitude=-123.13, zoom=11, max_zoom=16, pitch=45, bearing=0
    )

    r = pydeck.Deck(
        api_keys={"mapbox": MAPBOX_KEY},
        layers=[polygon, geojson],
        initial_view_state=INITIAL_VIEW_STATE,
        map_style=deckgl_map_style,
    )

    # Tooltip (you can get the id directly from the layer object)
    geojson_tooltip = {
        "html": """
        <b>Value per Square meter:</b> {properties.valuePerSqm}<br>
        <b>Growth:</b> {properties.growth}
        """,
        "style": {"backgroundColor": accent_base_color, "color": "white"},
    }
    tooltips = {geojson.id: geojson_tooltip}
    return r, tooltips

plot, tooltips = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.DeckGL(plot, tooltips=tooltips, height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()