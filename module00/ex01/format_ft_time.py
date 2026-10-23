import datetime
import time

# Get the current time in seconds since 01/01/1970
# Unix epoch is the standard time origin used by computers
# https://docs.python.org/3/library/time.html
current = time.time()
print(f"Seconds since January 1, 1970: {current:,.4f} or \
{current:.2e} in scientific notation")

# Get the current local date and time
# strftime is a datetime object method for formatting date objects into strings
# https://www.w3schools.com/python/python_datetime.asp
today = datetime.datetime.now()
print(today.strftime("%b %d %Y"))
