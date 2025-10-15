OLED.init(128, 64)
smartfeldSensoren.gas_init()
smartfeldSensoren.setGasCalibration()
loops.everyInterval(5000, function () {
    OLED.clear()
    OLED.writeStringNewLine("Der CO2-Gehalt beträgt: ")
    OLED.writeNumNewLine(smartfeldSensoren.readGasCO2eq())
    if (smartfeldSensoren.readGasCO2eq() < 1000) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
