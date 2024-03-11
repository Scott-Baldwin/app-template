import os
import dearpygui.dearpygui as dpg


app_path = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join(app_path, "data", "icons", "app_icon.ico")


class Motor:
    def __init__(self, burn_time, thrust, totalMass, propellantMass):
        self.burn_time = burn_time
        self.thrust = thrust
        self.totalMass = totalMass
        self.propellantMass = propellantMass


motorList = {"Name": [], "Motor": []}


def defineMotor(sender, data, user_data):
    motorList["Name"].append(dpg.get_value(user_data[0]))
    motorList["Motor"].append(
        Motor(
            dpg.get_value(user_data[1]),
            dpg.get_value(user_data[2]),
            dpg.get_value(user_data[3]),
            dpg.get_value(user_data[4]),
        )
    )
    dpg.configure_item(motor, items=motorList["Name"])


def select_motor(sender, data):
    index = motorList["Name"].index(data)
    motor = motorList["Motor"][index]

    print("Data: ", data)
    print(motor.burn_time, motor.thrust, motor.totalMass)


def print_motor(sender, data, user_data):
    name = dpg.get_value(user_data)
    print(name)
    # index = motorList["Name"].index(name)
    # motor = motorList["Motor"][index]

    # print("Data: ", data)
    # print(motor.burn_time, motor.thrust, motor.totalMass)


dpg.create_context()
dpg.create_viewport(title="Main", width=500, height=600, large_icon=icon)

with dpg.window(
    label="Define Motor", height=200, width=500, no_close=True, no_move=True
):
    name = dpg.add_input_text(label="Name")
    burn_time = dpg.add_input_int(label="Burn Time")
    thrust = dpg.add_input_float(label="Thrust")
    totalMass = dpg.add_input_float(label="Total Mass")
    propellantMass = dpg.add_input_float(label="Propellant Mass")
    dpg.add_button(
        label="Save",
        callback=defineMotor,
        user_data=[name, burn_time, thrust, totalMass, propellantMass],
    )


with dpg.window(
    label="Motors", height=200, width=300, pos=[0, 200], no_close=True, no_move=True
):
    motor = dpg.add_listbox(
        items=motorList["Name"], label="Motors", callback=select_motor
    )
    dpg.add_button(
        label="Print",
        callback=print_motor,
        user_data=motor,
    )

dpg.setup_dearpygui()
dpg.show_viewport()

dpg.start_dearpygui()
dpg.destroy_context()
