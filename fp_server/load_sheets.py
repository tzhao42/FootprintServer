import xlrd
import sqlite3
from fp_client.models import Cars

def main():
	book = xlrd.open_workbook('emissions-tables.xlsx')
	exec_sum = book.sheet_by_index(0)

	makes_array = exec_sum.col_values(0)[5:16]
	emissions_array = exec_sum.col_values(8)[5:16]

	#print(makes_array)
	#print(emissions_array)

	for i in range(len(makes_array)):
		c = Cars(name = makes_array[i], emissions = emissions_array[i])
		c.save()
	print(Cars.objects.all())

if __name__ == "__main__":
	main()
	