import json

# Reading JSON from a file
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return None

# Writing JSON to a file
def write_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("JSON written successfully.")
    except Exception as e:
        print(f"Error writing JSON: {e}")

# Example usage
if __name__ == "__main__":
    sample_data = {
        "name": "Hari",
        "age": 30,
        "skills": ["Python", "SQL", "Data Engineering"]
    }

    write_json("sample.json", sample_data)

    read_data = read_json("sample.json")
    print("Read Data:", read_data)
