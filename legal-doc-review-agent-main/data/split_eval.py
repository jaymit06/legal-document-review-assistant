import json, random
random.seed(42)
with open("data/processed/filtered_contracts.json") as f:
    data = json.load(f)
    random.shuffle(data)
eval_set = data[:20] 
train_set = data[20:]
with open("data/processed/eval_set.json", "w") as f:
    json.dump(eval_set, f, indent=2)
with open("data/processed/dev_set.json", "w") as f:
    json.dump(train_set, f, indent=2)
print(f"Eval set: {len(eval_set)} | Dev set: {len(train_set)}")