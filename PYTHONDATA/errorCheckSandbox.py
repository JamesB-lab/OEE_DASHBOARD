



from numpy import NaN


possible = 0

actual = 0

# try:

#     performance = actual/possible

# except ZeroDivisionError:
#     performance = 0

performance = actual/possible

if performance == NaN:
    performance = 0


print(performance)

# uptime = 0

# utilization = 0

# availability = utilization/uptime

# print(availability)

# pickup = 0

# placed = 0

# quality = placed/pickup

# print(quality)