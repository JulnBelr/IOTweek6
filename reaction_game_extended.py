"""
ReactionGame with Lockout Rules (R7, R8)

New Rules / Behavior Requirements:
- R7 (False Start Limit): Track consecutive or total false starts. 3 false starts trigger Lockout.
- R8 (Lockout Period): During Lockout, flash LED for 10 seconds, ignore presses, reset false start counter, then resume play.
"""

from gpiozero import LED, Button
from time import monotonic, sleep
from random import uniform
from reactionlog import ReactionLog


class ReactionGame:
    def __init__(self, led_pin, button_pin, player):
        self.led = LED(led_pin)
        self.button = Button(button_pin, bounce_time=0.05)
        self.log = ReactionLog(player)
        
        # New state attributes for Lockout feature
        self.false_starts = 0
        self.locked = False

    def trigger_lockout(self):
        """R8: 10-second lockout period with flashing LED while ignoring button presses."""
        print("\n*** LOCKOUT TRIGGERED: 3 False Starts! ***")
        print("System locked for 10 seconds. Please wait...")
        self.locked = True
        
        # Flash LED for 10 seconds (20 iterations * 0.5s = 10s)
        end_time = monotonic() + 10.0
        while monotonic() < end_time:
            self.led.toggle()
            sleep(0.25)
            
        self.led.off()
        self.false_starts = 0
        self.locked = False
        print("*** LOCKOUT EXPIRED: Resuming game ***\n")

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
        """One round. Handles false start counting and triggers lockout if needed."""
        if self.locked:
            return None

        self.led.off()
        print("Get ready...")
        
        if self.wait_delay():
            self.false_starts += 1
            print(f"FALSE START! (Count: {self.false_starts}/3)")
            self.button.wait_for_release()
            
            # Check R7 / R8 Lockout condition
            if self.false_starts >= 3:
                self.trigger_lockout()
            return None

        # Successful start
        self.led.on()
        t0 = monotonic()
        self.button.wait_for_press()
        ms = (monotonic() - t0) * 1000
        self.led.off()
        
        print(f"Reaction: {ms:.0f} ms")
        self.button.wait_for_release()
        
        # Reset consecutive false start counter on a successful round
        self.false_starts = 0
        self.log.add(ms)
        return ms

    def play(self, rounds):
        """Play until target valid rounds are recorded."""
        while self.log.count() < rounds:
            self.play_round()
        print("\n=== GAME OVER ===")
        print(self.log.summary())


if __name__ == "__main__":
    game = ReactionGame(led_pin=17, button_pin=27, player="Sam")
    game.play(5)
