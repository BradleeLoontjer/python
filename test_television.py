# test_television.py
import pytest
from television import Television


def test_init():
    tv = Television()
    assert tv._status is False
    assert tv._muted is False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL


def test_power():
    tv = Television()
    tv.power()
    assert tv._status is True
    tv.power()
    assert tv._status is False


def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._muted is True
    tv.mute()
    assert tv._muted is False


def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._channel == 1
    tv.channel_up()
    assert tv._channel == 2
    tv.channel_up()
    assert tv._channel == 3
    tv.channel_up()  # Should wrap around to MIN_CHANNEL
    assert tv._channel == Television.MIN_CHANNEL


def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()  # Should wrap around to MAX_CHANNEL
    assert tv._channel == Television.MAX_CHANNEL
    tv.channel_down()
    assert tv._channel == 2
    tv.channel_down()
    assert tv._channel == 1


def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._volume == 1
    tv.volume_up()
    assert tv._volume == 2
    tv.volume_up()  # Should not go beyond MAX_VOLUME
    assert tv._volume == Television.MAX_VOLUME


def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME
    tv.volume_down()  # Should not go below MIN_VOLUME
    assert tv._volume == Television.MIN_VOLUME


def test_volume_down_muted():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_down()  # Unmute and decrease volume
    assert tv._muted is False
    assert tv._volume == Television.MIN_VOLUME


if __name__ == '__main__':
    pytest.main()
