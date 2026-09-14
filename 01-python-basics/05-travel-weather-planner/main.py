# Define variables with placeholder values (Change these to test different cases)
distance_mi = 5.0
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

# Use conditional statements evaluated in ascending order with boolean operators
if not distance_mi:
    #  If distance_mi is a falsy value (like 0 or None)
    print(False)

elif distance_mi <= 1:
    #  Distance is less than or equal to 1 mile
    if not is_raining:
        print(True)
    else:
        print(False)

elif distance_mi <= 6:
    #  Distance is greater than 1 mile and less than or equal to 6 miles
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

else:
    #  Distance is greater than 6 miles
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
