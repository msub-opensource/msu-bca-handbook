# Question 12: Input hours, minutes and seconds and convert entire time into seconds

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# 1 hour = 60 minutes = 60 * 60 = 3600 seconds
# 1 minute = 60 seconds
total_seconds = hours * 3600 + minutes * 60 + seconds

print(f"Total seconds = {total_seconds}")
