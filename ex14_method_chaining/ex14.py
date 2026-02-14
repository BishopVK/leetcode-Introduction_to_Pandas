import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
	# return animals[ animals["weight"] > 100 ].sort_values(by="weight", ascending=False).drop(columns=["species", "age", "weight"])
	return animals[
		animals["weight"] > 100
	].sort_values(
		by="weight",
		ascending=False
	)[["name"]]

if __name__ == "__main__":
	df = pd.DataFrame(
		{
			"name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
			"species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
			"age": [98, 50, 6, 45, 100, 26],
			"weight": [464, 41, 328, 463, 50, 349],
		}
	)

	result = findHeavyAnimals(df)
	print(result)