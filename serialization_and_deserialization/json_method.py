import json

def process_json(data: dict, filename: str) -> dict:
	#serializaiton
	json_string = json.dumps(data)
	
	#writing to file
	with open(filename, "w") as file:
		saved_data = json.dump(data, file)
	
	#deserialization
	dict_data = json.loads(json_string)
	
	#loading from file
	with open(filename, "r") as file:
		loaded_data = json.load(file)

	#loading from file
	print(loaded_data)
	return f"Deserialized Data: {dict_data}"


sample_dict = {'name': 'femi', 'age': 30, 'gender':'male', 'status': 'full-time'}
process_json(sample_dict, "employee-details.json")
