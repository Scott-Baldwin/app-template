import os

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

import fonts


app_path = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join(app_path, "data", "icons", "app_icon.ico")


def main():
    dpg.create_context()
    dpg.create_viewport(
        title="DPG Built-in Demo", width=700, height=500, large_icon=icon
    )
    fonts.set_default(i=0, s=20)
    demo.show_demo()

    dpg.setup_dearpygui()
    dpg.show_viewport()

    # had to pull window id from show_demo source code
    dpg.set_primary_window("__demo_id", True)

    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
