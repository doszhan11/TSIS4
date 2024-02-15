from datetime import datetime

current_d = datetime.now()

datetime_w = current_d.replace(microsecond=0)


print("Original datetime:", current_d)
print("Datetime without microseconds:", datetime_w)
