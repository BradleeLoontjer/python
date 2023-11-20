# television.py

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize default instance variables."""
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        """Toggle the power status."""
        self._status = not self._status

    def mute(self):
        """Toggle the mute status."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        """Increase the channel by 1, considering the maximum channel."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        """Decrease the channel by 1, considering the minimum channel."""
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        """Increase the volume by 1, considering the maximum volume."""
        if self._status:
            self._muted = False
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        """Decrease the volume by 1, considering the minimum volume."""
        if self._status:
            self._muted = False
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def __str__(self):
        """Return the string representation of the Television object."""
        return f"Power--[{self._status}], Channel--[{self._channel}], Volume--[{self._volume}]"
