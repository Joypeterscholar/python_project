class TV:
    def __init__(self, tv_is_on: bool, channels):
        self.channels = channels
        self.volume = 0
        self.tv_is_on = tv_is_on

    def increase_vol(self):
        if self.tv_is_on:
            if 0 <= self.volume < 101:
                self.volume += 1
                return f"Volume {self.volume}"
        else:
            return "Tv is off"
    def decrease_vol(self):
        if self.tv_is_on:
            if 0 <= self.volume < 101:
                self.volume -= 1
                return f"Volume {self.volume}"
        else:
            return "Tv is off"

    def switch_channels(self):
        if self.tv_is_on == True:
            return f"Channel {self.channels}"
        else:
            return "Tv is off"

    def __str__(self):
        return f"{self.volume} {self.channels}"


tv = TV(True, 4)
tv.increase_vol()
tv.increase_vol()
tv.increase_vol()
tv.decrease_vol()

print(tv.switch_channels())
print(tv.increase_vol())
