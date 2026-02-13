import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
	# employees["bonus"] = employees["salary"] * 2 # -> Salary * 2

	# employees["bonus"] = employees["salary"] + 1000 # -> Salary + 1000

	# employees["bonus"] = pow(employees["salary"], 2) # -> Square of Salary

	""" employees["bonus"] = employees["salary"].where(  # -> Bono *2 if Salary > 5000, else 0
		employees["salary"] > 5000,
		0
	) * 2 """

	""" import numpy as np  # -> Bono *2 if Salary > 5000, else 0

	employees["bonus"] = np.where(
		employees["salary"] > 5000,
		employees["salary"] * 2,
		0
	) """

	employees["bonus"] = employees["salary"] * 2  # -> Bono *2 if Salary > 5000, else 0
	employees.loc[employees["salary"] <= 5000, "bonus"] = 0

	return employees

if __name__ == "__main__":
	data = [
		["Piper", 4548],
		["Grace", 28150],
		["Georgia", 1103],
		["Willow", 6593],
		["Finn", 74576],
		["Thomas", 24433],
	]

	df = pd.DataFrame(data, columns=["name", "salary"])

	result = createBonusColumn(df)
	print(result)