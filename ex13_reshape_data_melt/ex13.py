import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
	return pd.melt(
		report,
		id_vars=["product"],
		value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
		# value_vars=None, ->  Hace lo mismo
		var_name="quarter",
		value_name="sales"
	)

if __name__ == "__main__":
	df = pd.DataFrame(
		{
			"product": ["Umbrella", "SleepingBag"],
			"quarter_1": [417, 800],
			"quarter_2": [224, 936],
			"quarter_3": [379, 93],
			"quarter_4": [611, 875],
		}
	)

	result = meltTable(df)
	print(result)