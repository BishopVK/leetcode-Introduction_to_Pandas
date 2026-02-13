import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
	return students.dropna()

if __name__ == "__main__":
	df = pd.DataFrame(
		{
			"student_id": [32, 217, 779, 849],
			"name": ["Piper", None, "Georgia", "Willow"],
			"age": [5, 19, 20, 14],
		}
	)

	result = dropMissingData(df)
	print(result)