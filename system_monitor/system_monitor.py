from jtop import jtop
import qwiic_micro_oled
import time

PAGE_TIME = 5

OLED = qwiic_micro_oled.QwiicMicroOled()
if not OLED.is_connected():
    exit()

OLED.begin()
OLED.display()
OLED.set_font_type(0)

WIDTH = OLED.get_lcd_width()
CHAR_WIDTH = OLED.get_font_width() + 1

with jtop() as jetson:
    def header(title):
        OLED.line_h(0, 3, WIDTH)
        OLED.set_cursor((WIDTH - len(title)*CHAR_WIDTH)/2, 0)
        OLED.print(title)

    def usage1():
        header("USAGE")
        OLED.set_cursor(2, 8)
        OLED.print(f"GPU:{jetson.gpu['val']:5.0f}%")
        OLED.set_cursor(2, 16)
        OLED.print(f"CPU 1:{jetson.cpu['CPU1']['val']:3.0f}%")
        OLED.set_cursor(2, 24)
        OLED.print(f"CPU 2:{jetson.cpu['CPU2']['val']:3.0f}%")
        OLED.set_cursor(2, 32)
        OLED.print(f"CPU 3:{jetson.cpu['CPU3']['val']:3.0f}%")
        OLED.set_cursor(2, 40)
        OLED.print(f"CPU 4:{jetson.cpu['CPU4']['val']:3.0f}%")

    def usage2():
        header("USAGE")
        OLED.set_cursor(2, 12)
        OLED.print(f"RAM:{jetson.ram['use']/jetson.ram['tot']:6.1%}")
        OLED.set_cursor(2, 20)
        OLED.print(f"{jetson.ram['use']/1e6:4.1f}/{jetson.ram['tot']/1e6:3.1f}GB")
        OLED.set_cursor(2, 32)
        OLED.print(f"mem:{jetson.disk['used']/jetson.disk['total']:6.1%}")
        OLED.set_cursor(2, 40)
        OLED.print(f"{jetson.disk['used']:5.1f}/{jetson.disk['total']:2.0f}GB")

    def power():
        header("POWER")
        OLED.set_cursor(2, 12)
        OLED.print(f"GPU:{jetson.power[1]['5V GPU']['cur']:4.0f}mW")
        OLED.set_cursor(2, 24)
        OLED.print(f"CPU:{jetson.power[1]['5V CPU']['cur']:4.0f}mW")
        OLED.set_cursor(2, 36)
        OLED.print(f"tot:{jetson.power[0]['cur']:4.0f}mW")

    def thermal():
        header("THERMAL")
        OLED.set_cursor(2, 10)
        OLED.print(f"GPU:{jetson.temperature['GPU']:5.1f}C")
        OLED.set_cursor(2, 20)
        OLED.print(f"CPU:{jetson.temperature['CPU']:5.1f}C")
        OLED.set_cursor(2, 30)
        OLED.print(f"PLL:{jetson.temperature['PLL']:5.1f}C")
        OLED.set_cursor(2, 40)
        OLED.print(f"AO:{jetson.temperature['AO']:6.1f}C")

    def network():
        header("NETWORK")
        OLED.set_cursor(0, 12)
        OLED.print(f"eth0: {jetson.local_interfaces['interfaces']['eth0'] if 'eth0' in jetson.local_interfaces['interfaces'].keys() else 'N/A'}")
        OLED.set_cursor(0, 32)
        OLED.print(f"wlan0: {jetson.local_interfaces['interfaces']['wlan0'] if 'wlan0' in jetson.local_interfaces['interfaces'].keys() else 'N/A'}")

    while jetson.ok():
        for page_gen in [usage1, usage2, power, thermal, network]:
            OLED.clear(OLED.PAGE)
            OLED.clear(OLED.ALL)
            page_gen()
            OLED.display()
            time.sleep(PAGE_TIME)
