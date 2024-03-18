# %% imports
import os
import dearpygui.dearpygui as dpg

import browse, fonts


# %% files and folders
class InputFiles:
    path_1 = None
    path_2 = None


def test():
    dpg.show_font_manager()
    # fonts.font_manager()
    # print(InputFiles.path_1)


def file_browse_callback(sender, value, user_data):
    path = browse.file_browse()
    if path is not None:
        setattr(InputFiles, user_data, path)
        dpg.set_value(f"check_{user_data}", True)
        dpg.set_value(f"tip_{user_data}", path)


def file_browse_group(file_tag):
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


def folder_browse_group(folder_tag):
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


def custom_menu_bar():
    # def _log(sender, app_data, user_data):
    #     print(f"sender: {sender}, \t app_data: {app_data}, \t user_data: {user_data}")

    with dpg.menu_bar():
        # copied from dpg demo script

        with dpg.menu(label="Menu"):

            dpg.add_text("This menu is just for show!")
            # dpg.add_menu_item(label="New")
            # dpg.add_menu_item(label="Open")

            # with dpg.menu(label="Open Recent"):

            #     dpg.add_menu_item(label="harrel.c")
            #     dpg.add_menu_item(label="patty.h")
            #     dpg.add_menu_item(label="nick.py")

            # dpg.add_menu_item(label="Save")
            # dpg.add_menu_item(label="Save As...")

            # with dpg.menu(label="Settings"):

            #     dpg.add_menu_item(label="Option 1", callback=_log)
            #     dpg.add_menu_item(label="Option 2", check=True, callback=_log)
            #     dpg.add_menu_item(
            #         label="Option 3", check=True, default_value=True, callback=_log
            #     )

            #     with dpg.child_window(height=60, autosize_x=True, delay_search=True):
            #         for i in range(10):
            #             dpg.add_text(f"Scolling Text{i}")

            #     dpg.add_slider_float(label="Slider Float")
            #     dpg.add_input_int(label="Input Int")
            #     dpg.add_combo(("Yes", "No", "Maybe"), label="Combo")

        with dpg.menu(label="Tools"):

            dpg.add_menu_item(
                label="Show About", callback=lambda: dpg.show_tool(dpg.mvTool_About)
            )
            dpg.add_menu_item(
                label="Show Metrics", callback=lambda: dpg.show_tool(dpg.mvTool_Metrics)
            )
            dpg.add_menu_item(
                label="Show Documentation",
                callback=lambda: dpg.show_tool(dpg.mvTool_Doc),
            )
            dpg.add_menu_item(
                label="Show Debug", callback=lambda: dpg.show_tool(dpg.mvTool_Debug)
            )
            dpg.add_menu_item(
                label="Show Style Editor",
                callback=lambda: dpg.show_tool(dpg.mvTool_Style),
            )
            dpg.add_menu_item(
                label="Show Font Manager",
                callback=lambda: dpg.show_tool(dpg.mvTool_Font),
            )
            dpg.add_menu_item(
                label="Show Item Registry",
                callback=lambda: dpg.show_tool(dpg.mvTool_ItemRegistry),
            )

        with dpg.menu(label="Settings"):

            dpg.add_menu_item(
                label="Wait For Input",
                check=True,
                callback=lambda s, a: dpg.configure_app(wait_for_input=a),
            )
            dpg.add_menu_item(
                label="Toggle Fullscreen",
                callback=lambda: dpg.toggle_viewport_fullscreen(),
            )


# %% main layout
def create_layout():
    with dpg.window(label="Main", tag="Main", no_close=True, no_move=True):
        custom_menu_bar()
        with dpg.collapsing_header(label="Files"):
            file_browse_group("path_1")
            folder_browse_group("path_2")
            dpg.add_button(
                label="test",
                tag="print_path",
                callback=test,
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
