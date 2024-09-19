modules.button1.onEvent(jacdac.ButtonEvent.Down, function () {
    basic.showString("Guten Tag SPN")
})
modules.button2.onEvent(jacdac.ButtonEvent.Up, function () {
    Richtung = 1
})
modules.button2.onEvent(jacdac.ButtonEvent.Down, function () {
    Richtung = 2
})
modules.lightLevel1.onLightLevelChangedBy(20, function () {
    basic.setLedColors(0xffffff, 0xffffff, 0xffffff)
    basic.pause(5000)
    basic.turnRgbLedOff()
})
let Richtung = 0
basic.setLedColors(0x000000, 0x000000, 0x000000)
Richtung = 1
modules.led1.setBrightness(10)
modules.led1.setPixelColor(0, 0xff0000)
modules.led1.setPixelColor(1, 0x000000)
modules.led1.setPixelColor(2, 0x000000)
modules.led1.setPixelColor(3, 0x000000)
modules.led1.setPixelColor(4, 0x00ff00)
modules.led1.setPixelColor(5, 0x000000)
modules.led1.setPixelColor(6, 0x000000)
modules.led1.setPixelColor(7, 0x000000)
basic.forever(function () {
    if (Richtung == 1) {
        modules.led1.rotate(1)
        basic.pause(500)
    } else if (Richtung == 2) {
        modules.led1.rotate(-1)
        basic.pause(500)
    }
})
