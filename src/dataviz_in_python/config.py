import pathlib
from typing import Optional

import panel as pn

ACCENT_BASE_COLOR = "#4099da"

ROOT = pathlib.Path(__file__).parent
MENU_HTML_PATH = (ROOT / "assets" / "menu.html")
MENU_HTML = MENU_HTML_PATH.read_text()

COLLAPSED_ICON = """
<svg style="stroke: { self.accent_base_color }" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="collapsed-icon">
<path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
<path d="M9 5.44446V12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
<path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
"""

EXPANDED_ICON = """
<svg style="stroke: { self.accent_base_color }" width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg" slot="expanded-icon">
<path d="M15.2222 1H2.77778C1.79594 1 1 1.79594 1 2.77778V15.2222C1 16.2041 1.79594 17 2.77778 17H15.2222C16.2041 17 17 16.2041 17 15.2222V2.77778C17 1.79594 16.2041 1 15.2222 1Z" stroke-linecap="round" stroke-linejoin="round"></path>
<path d="M5.44446 9H12.5556" stroke-linecap="round" stroke-linejoin="round"></path>
</svg>
"""

TEXT_CLASS = "presentation-text"

CSS = """
#menu .menu-item-active a {
    color: white !important; 
}
div.bk.presentation-text.markdown div {
    font-size: var(--type-ramp-plus-3-font-size);
}
"""
            

def get_menu(url, title):
    return (
        MENU_HTML_PATH.read_text()
        .replace("{ COLLAPSED_ICON }", COLLAPSED_ICON)
        .replace("{ EXPANDED_ICON }", EXPANDED_ICON)
        .replace(f'<li><a href="{ url }">{ title }</a></li>', f'<li class="menu-item-active"><a href="{ url }">{ title }</a></li>')
    )

def get_theme():
    template = pn.state.template
    theme = "dark" if template.theme == pn.template.DarkTheme else "default"
    return theme

def configure(
    *args,
    title: str,
    url: Optional[str]=None,
    sizing_mode="stretch_width",
    template="fast",
    accent_color=ACCENT_BASE_COLOR,
    site="DataViz in Python",
):
    """Runs pn.extension and pn.state.template.param.update with the specified 
    arguments"""
    if not CSS in pn.config.raw_css:
        pn.config.raw_css.append(CSS)
    
    pn.extension(*args, sizing_mode=sizing_mode, template=template)
    
    if not url:
        url = title.lower().replace(" ", "_")
    menu = get_menu(url=url, title=title)

    pn.state.template.param.update(
        site=site,
        title=title,
        accent_base_color=accent_color,
        header_background=accent_color,
        sidebar_footer=menu
    )
