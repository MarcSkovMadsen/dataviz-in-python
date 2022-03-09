import panel as pn
import vtk

from vtk.util.colors import tomato

pn.extension("vtk", sizing_mode="stretch_width")

accent_base_color = "#DAA520"
template = pn.template.FastListTemplate(
    site="Awesome Panel",
    title="VTK",
    accent_base_color=accent_base_color,
    header_background=accent_base_color,
    header_accent_base_color="white",
)
theme = "dark" if template.theme == pn.template.DarkTheme else "default"


def get_plot(theme="default", accent_base_color="blue"):
    # This creates a polygonal cylinder model with eight circumferential
    # facets.
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)

    # The mapper is responsible for pushing the geometry into the graphics
    # library. It may also do color mapping, if scalars or other
    # attributes are defined.
    cylinderMapper = vtk.vtkPolyDataMapper()
    cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

    # The actor is a grouping mechanism: besides the geometry (mapper), it
    # also has a property, transformation matrix, and/or texture map.
    # Here we set its color and rotate it -22.5 degrees.
    cylinderActor = vtk.vtkActor()
    cylinderActor.SetMapper(cylinderMapper)
    cylinderActor.GetProperty().SetColor(tomato)
    # We must set ScalarVisibilty to 0 to use tomato Color
    cylinderMapper.SetScalarVisibility(0)
    cylinderActor.RotateX(30.0)
    cylinderActor.RotateY(-45.0)

    # Create the graphics structure. The renderer renders into the render
    # window.
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)

    # Add the actors to the renderer, set the background and size
    ren.AddActor(cylinderActor)
    if theme == "dark":
        ren.SetBackground(0.13, 0.13, 0.13)
    else:
        ren.SetBackground(0.97, 0.97, 0.97)
    return renWin

plot = get_plot(theme=theme, accent_base_color=accent_base_color)
component = pn.pane.VTK(plot, height=500, sizing_mode="stretch_both")
template.main.append(component)
template.servable()