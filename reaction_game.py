from gpiozero import LED, Button
from time import monotonic, sleep
from random import uniform
from reactionlog import ReactionLog       
class ReactionGame:
    def __init__(self, led_pin, button_pin, player):
        self.led = LED(led_pin)                          
        self.button = Button(button_pin, bounce_time=0.05)
        self.log = ReactionLog(player)                   
    def wait_delay(self):
        """The watchful wait. Returns True on a false start."""   
        delay = uniform(2.0, 5.0)
        waited = 0.0
        while waited < delay:
            if self.button.is_pressed:
                return True
            sleep(0.01)
            waited = waited + 0.01
        return False
    def play_round(self):
        """One round. Returns the time in ms, or None on a false start."""
        self.led.off()                                   
        print("Get ready...")
        if self.wait_delay():
            print("FALSE START")                         
            self.button.wait_for_release()
            return None
        self.led.on()                                    
        t0 = monotonic()
        self.button.wait_for_press()                     
        ms = (monotonic() - t0) * 1000
        self.led.off()
        print(f"Reaction: {ms:.0f} ms")
        self.button.wait_for_release()
        self.log.add(ms)
        return ms
    def play(self, rounds):
        """Play until `rounds` valid times are recorded."""       
        while self.log.count() < rounds:
            self.play_round()
        print(self.log.summary())
game = ReactionGame(17, 27, "Sam")
game.play(5)
