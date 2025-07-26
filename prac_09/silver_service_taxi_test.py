"""

"""
from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    """Test fare and string output of SilverServiceTaxi."""

    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()

    print(f"Expected fare: $48.78 (before rounding)")
    print(f"Actual fare: ${fare:.2f}")
    assert abs(fare - 48.78) < 0.05, "Fare should be close to $48.78"

    print("\nTaxi __str__:")
    print(taxi)

if __name__ == "__main__":
    test_silver_service_taxi()
