import os
from webbrowser import get
import dearpygui.dearpygui as dpg

import browse, fonts


app_path = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join(app_path, "data", "app_icon.ico")


class InputFiles:
    path_1 = None
    path_2 = None


def file_browse_callback(sender, value, user_data):
    path = browse.file_browse()
    if path is not None:
        setattr(InputFiles, user_data, path)
        dpg.set_value(f"check_{user_data}", True)
        dpg.set_value(f"tip_{user_data}", path)


def add_file_browse_group(file_tag):
    with dpg.group(horizontal=True):
        dpg.add_text(f"File path: ({file_tag})", tag=f"text_{file_tag}")
        dpg.add_button(label="...", callback=file_browse_callback, user_data=file_tag)
        dpg.add_checkbox(tag=f"check_{file_tag}", enabled=False)
    with dpg.tooltip(f"text_{file_tag}"):
        dpg.add_text(getattr(InputFiles, file_tag), tag=f"tip_{file_tag}", wrap=400)


def print_saved_path():
    print(InputFiles.path_1)


dpg.create_context()
dpg.create_viewport(
    title="App Template", width=200, height=100, large_icon=icon, small_icon=icon
)

fonts.set_default(i=0, s=20)

with dpg.window(label="Main", tag="Main", no_close=True, no_move=True):
    with dpg.collapsing_header(label="Tab 1"):
        add_file_browse_group("path_1")
        add_file_browse_group("path_2")
        dpg.add_button(
            label="print",
            tag="print_path",
            callback=print_saved_path,
        )

    dpg.add_loading_indicator(circle_count=8)

dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("Main", True)

dpg.start_dearpygui()
dpg.destroy_context()
