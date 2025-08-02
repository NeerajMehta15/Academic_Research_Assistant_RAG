import os
import json

def get_project_structure(root_dir):
    def recurse(directory):
        structure = {}
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                structure[item] = recurse(item_path)
            else:
                structure[item] = "file"
        return structure

    return {os.path.basename(root_dir): recurse(root_dir)}

# Set your root project directory here
root_directory = "/Users/neeraj/Documents/Python/Academic_Research_Assistant_RAG"

structure = get_project_structure(root_directory)

# Save to JSON
with open("project_structure.json", "w") as f:
    json.dump(structure, f, indent=4)

print("Project structure saved to project_structure.json")
