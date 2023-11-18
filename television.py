# television.py

class Television:
    # class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # instance variables
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        self._status = not self._status
        if not self._status:
            self._muted = False

    def mute(self):
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        if self._status:
            self._muted = False  # Unmute if muted
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        if self._status:
            self._muted = False  # Unmute if muted
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def __str__(self):
        return f"Power--[{self._status}], Channel--[{self._channel}], Volume--[{self._volume}]"
