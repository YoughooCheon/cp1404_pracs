"""
import unreliablecar class

function test_unreliable_car():
    create reliable_car with reliability 100
    create unreliable_car with reliability 0
    create semi_reliable_car with reliability 50

    total_distance = 0
    repeat 10 times:
        add reliable_car.drive(10) to total_distance
    print "reliable car drove:", total_distance
    assert total_distance == 100

    total_distance = 0
    repeat 10 times:
        add unreliable_car.drive(10) to total_distance
    print "unreliable car drove:", total_distance
    assert total_distance == 0

    set drive_attempts to 100
    set distance_each_attempt to 1
    total_distance = 0
    create semi_reliable_car with reliability 30
    repeat drive_attempts times:
        add semi_reliable_car.drive(distance_each_attempt) to total_distance
    print "semi-reliable car drove:", total_distance
    assert total_distance is approximately 30% of drive_attempts

if this module is main:
    call test_unreliable_car()
"""
from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test UnreliableCar behavior over multiple drives to account for randomness."""

    reliable_car = UnreliableCar("Reliable", 100, 100)
    unreliable_car = UnreliableCar("Unreliable", 100, 0)
    semi_reliable_car = UnreliableCar("Semi", 100, 50)

    total_distance = 0
    for _ in range(10):
        total_distance += reliable_car.drive(10)
    print("Reliable car drove:", total_distance)
    assert total_distance == 100, "Reliable car should always drive"

    total_distance = 0
    for _ in range(10):
        total_distance += unreliable_car.drive(10)
    print("Unreliable car drove:", total_distance)
    assert total_distance == 0, "Unreliable car should never drive"

    drive_attempts = 100
    distance_each_attempt = 1
    total_distance = 0
    semi_reliable_car = UnreliableCar("Semi", 100, 30)
    for _ in range(drive_attempts):
        total_distance += semi_reliable_car.drive(distance_each_attempt)

    print("Semi-reliable car drove:", total_distance)
    assert 15 < total_distance < 45, "Semi-reliable car should drive approximately 30% of the time"

if __name__ == "__main__":
    test_unreliable_car()
