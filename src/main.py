# %% imports
import os
import dearpygui.dearpygui as dpg

import browse, fonts


# %% files and folders
class InputFiles:
    path_1 = None
    path_2 = None


def print_saved_path():
    print(InputFiles.path_1)


def file_browse_callback(sender, value, user_data):
    path = browse.file_browse()
    if path is not None:
        setattr(InputFiles, user_data, path)
        dpg.set_value(f"check_{user_data}", True)
        dpg.set_value(f"tip_{user_data}", path)


def add_file_browse_group(file_tag):
    with dpg.group(horizontal=True):
        dpg.add_button(
            label="...",
            callback=file_browse_callback,
            user_data=file_tag,
        )
        dpg.add_checkbox(tag=f"check_{file_tag}", enabled=False)
        dpg.add_text(f"File path: ({file_tag})", tag=f"text_{file_tag}")
    with dpg.tooltip(f"text_{file_tag}"):
        dpg.add_text(getattr(InputFiles, file_tag), tag=f"tip_{file_tag}", wrap=400)


def folder_browse_callback(sender, value, user_data):
    path = browse.folder_browse()
    if path is not None:
        setattr(InputFiles, user_data, path)
        dpg.set_value(f"check_{user_data}", True)
        dpg.set_value(f"tip_{user_data}", path)


def add_folder_browse_group(folder_tag):
    with dpg.group(horizontal=True):
        dpg.add_button(
            label="...",
            callback=folder_browse_callback,
            user_data=folder_tag,
        )
        dpg.add_checkbox(tag=f"check_{folder_tag}", enabled=False)
        dpg.add_text(f"Folder path: ({folder_tag})", tag=f"text_{folder_tag}")
    with dpg.tooltip(f"text_{folder_tag}"):
        dpg.add_text(getattr(InputFiles, folder_tag), tag=f"tip_{folder_tag}", wrap=400)


# %% main layout
def create_layout():
    with dpg.window(label="Main", tag="Main", no_close=True, no_move=True):
        with dpg.collapsing_header(label="Files"):
            add_file_browse_group("path_1")
            add_folder_browse_group("path_2")
            dpg.add_button(
                label="print",
                tag="print_path",
                callback=print_saved_path,
            )

        dpg.add_loading_indicator(circle_count=8)


# %% run
def main():
    # path to script or .exe
    app_path = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(app_path, "data", "app_icon.ico")

    # boilerplate
    dpg.create_context()
    dpg.create_viewport(
        title="App Template",
        width=200,
        height=100,
        large_icon=icon,
        small_icon=icon,
    )

    # add custom font
    fonts.set_default(i=0, s=20)

    # main window layout
    create_layout()

    # more boilerplate
    dpg.setup_dearpygui()

    dpg.show_viewport()

    # set main window
    dpg.set_primary_window("Main", True)

    # more boilerplate
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
