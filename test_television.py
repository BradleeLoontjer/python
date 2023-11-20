# test_television.py
import pytest
from television import Television

def test_television():
    tv = Television()

    # Test power method
    tv.power()
    assert tv._status is True

    # Test mute method
    tv.mute()
    assert tv._muted is True

    # Test channel_up method
    tv.channel_up()
    assert tv._channel == 1

    # Test channel_down method
    tv.channel_down()
    assert tv._channel == 0

    # Test volume_up method
    tv.volume_up()
    assert tv._volume == 1

    # Test volume_down method
    tv.volume_down()
    assert tv._volume == 0

    # Test __str__ method
    assert str(tv) == "Power--[True], Channel--[0], Volume--[0]"

if __name__ == "__main__":
    pytest.main()
