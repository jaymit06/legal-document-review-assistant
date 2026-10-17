from datasets import load_dataset

print("Downloading CUAD dataset (free, no login needed)...")
dataset = load_dataset("theatticusproject/cuad-qa", revision="refs/convert/parquet")
print("Done. Train examples:", len(dataset["train"]))
print("Test examples:", len(dataset["test"]))

dataset["train"].to_json("data/raw/cuad_train.json")
dataset["test"].to_json("data/raw/cuad_test.json")
print("Saved to data/raw/")