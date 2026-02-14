import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
	return students.astype({"grade": int})

if __name__ == "__main__":
	df = pd.DataFrame(
		{
			"student_id": [1, 2],
			"name": ["Ava", "Kate"],
			"age": [6, 15],
			"grade": [73.0, 87.0],
		}
	)

	result = changeDatatype(df)
	print(result)