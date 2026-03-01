import os
import socket
import re
from collections import Counter


def process_file(filepath, split_contractions=False):
    if not os.path.exists(filepath):
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read().lower()

        # Split contractions for the second file
        if split_contractions:
            text = text.replace("'", " ")

        # Treat em-dash (—) and hyphen (-) as separators to catch "and"
        # in "pitch-and-toss" and "And—which"
        text = text.replace("—", " ").replace("-", " ")

        # Clean up remaining standard punctuation
        text = re.sub(r'[.,!?;:()"]', " ", text)

        # Split by whitespace
        words = text.split()
        return words


# File Paths
data_dir = "/home/data"
output_path = os.path.join(data_dir, "output/result.txt")
file1 = os.path.join(data_dir, "IF.txt")
file2 = os.path.join(data_dir, "AlwaysRememberUsThisWay.txt")

os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Process Files
words1 = process_file(file1, split_contractions=False)
words2 = process_file(file2, split_contractions=True)

# Math
count1 = len(words1)
count2 = len(words2)
grand_total = count1 + count2
top3_if = Counter(words1).most_common(3)
top3_always = Counter(words2).most_common(3)
ip_address = socket.gethostbyname(socket.gethostname())

# Build Result String
result = (
    f"Word count in IF.txt: {count1}\n"
    f"Word count in AlwaysRememberUsThisWay.txt: {count2}\n"
    f"Grand total: {grand_total}\n\n"
    f"Top 3 words in IF.txt: {top3_if}\n"
    f"Top 3 words in AlwaysRememberUsThisWay.txt (splitting contractions): {top3_always}\n\n"
    f"Container IP Address: {ip_address}\n"
)

# Write to file and print to console
with open(output_path, "w") as f:
    f.write(result)
print(result)
