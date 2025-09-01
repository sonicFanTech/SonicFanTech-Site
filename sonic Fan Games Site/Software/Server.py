import json

# Replace this with the path to your JSON file
file_path = "C:\Users\Sonic Tech\Documents\GitHub\sonic Fan Games Site\Software\software.json"

try:
    with open(file_path, "r") as f:
        data = json.load(f)
    print("✅ JSON is valid!")
except json.JSONDecodeError as e:
    print("❌ JSON is invalid!")
    print("Error:", e)

input("\nPress Enter to exit...")
