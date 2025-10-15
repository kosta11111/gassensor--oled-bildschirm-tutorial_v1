OLED.init(128, 64)
smartfeldSensoren.gas_init()
smartfeldSensoren.set_gas_calibration()

def on_every_interval():
    OLED.clear()
    OLED.write_string_new_line("Der CO2-Gehalt beträgt: ")
    OLED.write_num_new_line(smartfeldSensoren.read_gas_co_2eq())
    if smartfeldSensoren.read_gas_co_2eq() < 1000:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
loops.every_interval(5000, on_every_interval)
