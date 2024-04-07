import time

# List of names
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]

# Iterate through the list of names
for index, name in enumerate(names):
    # Calculate progress percentage
    progress_percentage = (index + 1) / len(names) * 100

    # Clear the current line and print the new message
    print(f"\rProcessing {index + 1}/{len(names)}: {name} - Progress: {progress_percentage:.2f}%", end="", flush=True)
    # Simulate some processing time
    time.sleep(0.5)

print("\nProcessing complete!")
