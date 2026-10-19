"""
NightLight State Machine with DIM Mode
Cycle: OFF -> ON -> DIM -> OFF ...

States:
  0: OFF (LED off)
  1: ON  (LED solid on)
  2: DIM (LED blinking slowly / dimmed)
"""

from gpiozero import LED, Button
from time import sleep


class NightLight:
    def __init__(self, led_pin, button_pin):
        self.led = LED(led_pin)
        self.button = Button(button_pin, bounce_time=0.05)
        # State: 0 = OFF, 1 = ON, 2 = DIM
        self.state = 0
        
        # Attach button press event
        self.button.when_pressed = self.handle_press

    def handle_press(self):
        """State transition logic upon button press."""
        if self.state == 0:
            self.state = 1
            print("[State Change] OFF -> ON")
        elif self.state == 1:
            self.state = 2
            print("[State Change] ON -> DIM")
        elif self.state == 2:
            self.state = 0
            print("[State Change] DIM -> OFF")

    def update_hardware(self):
        """Applies hardware actions matching current state."""
        if self.state == 0:
            self.led.off()
        elif self.state == 1:
            self.led.on()
        elif self.state == 2:
            # DIM mode: slow blinking simulation
            self.led.on()
            sleep(0.1)
            self.led.off()
            sleep(0.1)

    def run(self):
        """Main event loop."""
        print("NightLight running... Press button to cycle (OFF -> ON -> DIM -> OFF).")
        try:
            while True:
                self.update_hardware()
                sleep(0.01)
        except KeyboardInterrupt:
            self.led.off()
            print("\nNightLight shutdown.")


if __name__ == "__main__":
    # Pins matching standard setup (LED=17, Button=27)
    light = NightLight(led_pin=17, button_pin=27)
    light.run()
