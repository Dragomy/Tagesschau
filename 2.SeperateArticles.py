import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('news.json', 'r') as json_file:
    raw_data = json_file.read()

# Fix !hopefully! all errors 
transformed_data = (
    raw_data
    .replace('False', 'false')
    .replace('True', 'true')
    .replace('"', '!')
    .replace("'", '"')
    .replace('\\xa0', ' ') 
)

# Load a valid Json
data = json.loads(transformed_data)

#Regioncount
counts = [0] * 16

for item in data["news"]:
    regionId = item.get("regionId")
    
    if regionId is not None and 1 <= regionId <= 16:
        counts[regionId - 1] += 1

sorted_counts = sorted(enumerate(counts, start=1), key=lambda x: x[1])

for num, count in sorted_counts:
    if count > 0:
        print(f"RegionId {num} occurs {count} times.")


# Matplotlib visualisation as a bar graph   
labels = [str(i) for i in range(1, 17)]

plt.bar(labels, counts)
plt.title('Number Counts')
plt.xlabel('Number')
plt.ylabel('Count')

plt.show()