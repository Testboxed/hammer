import dearpygui.dearpygui as dpg
from TestboxedClient import TestboxedClient

class Unity:
    # https://docs.unity3d.com/Manual/PlayerCommandLineArguments.html
    opengl_levels = "32,33,40,41,42,43,44,45".split(",")
    renders = [
        "default",
        "directx 11",
        "directx 11 fl 10.0",
        "directx 11 fl 10.1",
        "directx 11 fl 11.0",
        "directx 12",
        "opengl core",
        "vulkan",
        "wayland",
        "metal",
    ]

for x in Unity.opengl_levels:
    Unity.renders.append(f"opengl {x}")

def about(sender):
    with dpg.window(label = "About Testboxed Hammer"):
        dpg.add_text("Branch: dev, official")
        dpg.add_text("Made by DFC")

def run_map(sender):
    with dpg.window(label = "Run map"):
        dpg.add_text(f"Testboxed exec: {TestboxedClient.exec_path}\n")
        dpg.add_text(f"Render:")
        dpg.add_listbox(Unity.renders, width=100, default_value="default")
        dpg.add_button("Run")

dpg.create_context()
dpg.create_viewport(
    title = 'Testboxed Hammer',
    max_width = 1280, max_height = 720,
    width = 1280, height = 720,
    min_width = 800, min_height = 600,
    vsync = True,
    small_icon = "icon.ico", large_icon = "icon.ico"
)

with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Open")
        dpg.add_menu_item(label="Save")
        dpg.add_menu_item(label="Save As")

    with dpg.menu(label="Editor"):
        dpg.add_menu_item(label="Texture browser (Local)")
        dpg.add_menu_item(label="Texture browser (Online)")
        dpg.add_separator()
        dpg.add_menu_item(label="Settings")
        dpg.add_menu_item(label="Run map", callback=run_map)

    with dpg.menu(label="About"):
        dpg.add_menu_item(label="Hammer", callback=about)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()