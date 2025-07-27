"""
import taxi class

create taxi instance named "prius 1" with 100 fuel as my_taxi

call my_taxi.drive(40)

print my_taxi details
print current fare formatted from my_taxi.get_fare()

call my_taxi.start_fare() to reset fare distance

call my_taxi.drive(100)

print my_taxi details
print current fare formatted from my_taxi.get_fare()
"""
from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)

my_taxi.drive(40)

print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

my_taxi.start_fare()
my_taxi.drive(100)

print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")
