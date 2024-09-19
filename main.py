def on_button1_button_down():
    basic.show_string("Guten Tag SPN")
modules.button1.on_event(jacdac.ButtonEvent.DOWN, on_button1_button_down)

def on_button2_button_up():
    global Richtung
    Richtung = 1
modules.button2.on_event(jacdac.ButtonEvent.UP, on_button2_button_up)

def on_button2_button_down():
    global Richtung
    Richtung = 2
modules.button2.on_event(jacdac.ButtonEvent.DOWN, on_button2_button_down)

def on_light_level1_level_changed_by():
    basic.set_led_colors(0xffffff, 0xffffff, 0xffffff)
    basic.pause(5000)
    basic.turn_rgb_led_off()
modules.light_level1.on_light_level_changed_by(20, on_light_level1_level_changed_by)

Richtung = 0
basic.set_led_colors(0x000000, 0x000000, 0x000000)
Richtung = 1
modules.led1.set_brightness(10)
modules.led1.set_pixel_color(0, 0xff0000)
modules.led1.set_pixel_color(1, 0x000000)
modules.led1.set_pixel_color(2, 0x000000)
modules.led1.set_pixel_color(3, 0x000000)
modules.led1.set_pixel_color(4, 0x00ff00)
modules.led1.set_pixel_color(5, 0x000000)
modules.led1.set_pixel_color(6, 0x000000)
modules.led1.set_pixel_color(7, 0x000000)

def on_forever():
    if Richtung == 1:
        modules.led1.rotate(1)
        basic.pause(500)
    elif Richtung == 2:
        modules.led1.rotate(-1)
        basic.pause(500)
basic.forever(on_forever)
