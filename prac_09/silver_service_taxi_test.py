"""
function test_silver_service_taxi():
    description: test the fare calculation and string output of a SilverServiceTaxi

    create silver_service_taxi named "Hummer" with 200 fuel and fanciness 2
    start fare calculation
    drive taxi for 18 kilometers
    get the fare

    print expected fare message
    print actual fare formatted to 2 decimals
    assert that fare is approximately 48.78 within a margin of 0.05

    print label for taxi string output
    print taxi's string representation

if running as main program:
    call test_silver_service_taxi()
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