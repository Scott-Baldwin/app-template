import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def main():
    dpg.create_context()
    dpg.create_viewport(title="DPG Demo", width=650, height=450)

    demo.show_demo()

    dpg.setup_dearpygui()
    dpg.show_viewport()

    # had to pull window id from source code
    dpg.set_primary_window("__demo_id", True)

    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
