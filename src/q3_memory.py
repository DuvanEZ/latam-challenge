from collections import Counter
from typing import List, Tuple
import re
import json

def extract_usernames(file_path: str):
  """Generator function to extract usernames from each line of the file."""
  with open(file_path, 'r') as file:
    for line in file:
      try:
        data = json.loads(line.strip())
        if 'content' in data:
          content = data['content']
          # Use regex to find usernames
          for username in re.findall(r'@(\w+)', content):
            yield username
      except json.JSONDecodeError:
        continue  # Skip lines that can't be decoded

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
  username_counts = Counter()
  # Use the generator to update the Counter for each username
  username_counts.update(extract_usernames(file_path))
  # Get the top 10 usernames
  top_10_usernames = username_counts.most_common(10)

  return top_10_usernames