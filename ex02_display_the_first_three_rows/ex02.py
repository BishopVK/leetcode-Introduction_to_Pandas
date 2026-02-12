import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
	# return employees.head(3)
	
	return employees[:3]

if __name__ == "__main__":
	data = [
		[3, "Bob", "Operations", 48675],
		[90, "Alice", "Sales", 11096],
		[9, "Tatiana", "Engineering", 33805],
		[60, "Annabelle", "InformationTechnology", 37678],
		[49, "Jonathan", "HumanResources", 23793],
		[43, "Khaled", "Administration", 40454],
	]

	df = pd.DataFrame(data, columns=["employee_id", "name", "department", "salary"])

	result = selectFirstRows(df)
	print(result)