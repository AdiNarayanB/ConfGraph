import json

with open("/home/adithya/datavizgraphapp/dataset_100000_2000_2024_Journals.json", "r") as f:
    data = json.load(f)

keyword_conf = {}

# Iterate over each paper in the dataset
for paper in data:
    p_conf = paper['venue']
    p_keywords = paper['enhanced']
    
    # Iterate over each author of the paper
    for p_keyword in p_keywords:
        if p_keyword not in keyword_conf:
            keyword_conf[p_keyword] = {p_conf}  # Use a set to store conferences
        else:
            keyword_conf[p_keyword].add(p_conf)  # Add conference to the set

# Get the first 10,000 keys
keyword_conf_lists = {keyword: list(conferences) for keyword, conferences in keyword_conf.items()}
keyword_conf_lists = dict(list(keyword_conf_lists.items())[:10000])

# Create a dictionary to store keyword and its corresponding list size
keyword_list_size = {keyword: len(conferences) for keyword, conferences in keyword_conf_lists.items()}

# Save keyword_conf_lists to JSON file
with open("keywordGraphMini.json", "w") as f:
    json.dump(keyword_conf_lists, f, indent=2)

# Save keyword_list_size to JSON file
with open("keywordListSize.json", "w") as f:
    json.dump(keyword_list_size, f, indent=2)

