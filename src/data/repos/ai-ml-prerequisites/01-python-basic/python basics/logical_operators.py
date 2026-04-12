# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)

temp = 20
is_raining = False

if temp >= 45 or temp <= 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is not cancelled")


is_sunny = False

if temp >= 28 and is_sunny:
    print("It's Hot outside🥵")
    print("It is Sunny☀️")
elif temp <=0 and is_sunny:
    print("It's Cold outside🥶")
    print("It is Sunny☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm outside😊")
    print("It is Sunny☀️")


if temp >= 28 and not is_sunny:
    print("It's Hot outside🥵")
    print("It is Cloudy☁️")
elif temp <=0 and not is_sunny:
    print("It's Cold outside🥶")
    print("It is Cloudy☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm outside😊")
    print("It is Cloudy☁️")