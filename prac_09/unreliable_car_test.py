from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test UnreliableCar behavior over multiple drives to account for randomness."""

    reliable_car = UnreliableCar("Reliable", 100, 100)  # Should always drive
    unreliable_car = UnreliableCar("Unreliable", 100, 0)  # Should never drive
    semi_reliable_car = UnreliableCar("Semi", 100, 50)  # Should drive ~50% of the time

    # 1. Always drives
    total_distance = 0
    for _ in range(10):
        total_distance += reliable_car.drive(10)
    print("Reliable car drove:", total_distance)
    assert total_distance == 100, "Reliable car should always drive"

    # 2. Never drives
    total_distance = 0
    for _ in range(10):
        total_distance += unreliable_car.drive(10)
    print("Unreliable car drove:", total_distance)
    assert total_distance == 0, "Unreliable car should never drive"

    # 3. Semi-reliable: should drive some of the time
    drive_attempts = 100
    distance_each_attempt = 1
    total_distance = 0
    semi_reliable_car = UnreliableCar("Semi", 100, 30)  # 30% reliable
    for _ in range(drive_attempts):
        total_distance += semi_reliable_car.drive(distance_each_attempt)

    print("Semi-reliable car drove:", total_distance)
    assert 15 < total_distance < 45, "Semi-reliable car should drive approximately 30% of the time"

if __name__ == "__main__":
    test_unreliable_car()
