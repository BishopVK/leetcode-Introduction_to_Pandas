import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
	return employees.mul({"name": 1, "salary": 2})

	""" employees ['salary']*=2
	return employees """

if __name__ == "__main__":
	df = pd.DataFrame(
		{
			"name": ["Jack", "Piper", "Mia", "Ulysses"],
			"salary": [19666, 74754, 62509, 54866],
		}
	)

	result = modifySalaryColumn(df)
	print(result)