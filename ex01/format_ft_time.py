from datetime import datetime
from time import time

now = datetime.now()

def format_time(time: float) -> str:
	try:
		if (time <= 0):
			raise ValueError
		time, dec = (str(time)).split('.')
		table_time = list(time)
		for i in range(len(time) - 3, 0, -3):
			table_time.insert(i, ',')
		return f"{''.join(table_time)}.{dec}"
	except ValueError:
		return 'Invalid Value!'


def scientific_notation(time: float) -> str:
	try:
		if (time <= 100):
			raise ValueError
		time = str(time)
		# No rounding 
		return time[0] + '.' + time[1:3] + 'e+' + str(len(time[1:].split('.')[0])).zfill(2)
	except ValueError:
		return 'Invalid Value!'

scientific_notation(time())
print(f"Seconds since January 1, 1970: {format_time(time())} or {scientific_notation(time())} in scientific notation")
print(now.strftime("%b %d %Y"))

