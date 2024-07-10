from collections import Counter
from typing import List, Tuple
import re
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
  # Compile the regex pattern outside of the loop for efficiency
  username_pattern = re.compile(r'@(\w+)')
  usernames = []

  with open(file_path, 'r') as file:
    for line in file:
      try:
        data = json.loads(line.strip())
        if 'content' in data:
          content = data['content']
          # Use the pre-compiled regex to extract usernames
          usernames_in_content = username_pattern.findall(content)
          usernames.extend(usernames_in_content)
      except json.JSONDecodeError:
        # Handle lines that are not valid JSON
        print("Warning: Skipping invalid JSON line.")
      except KeyError:
        # Handle lines missing the 'content' key
        print("Warning: Skipping line missing 'content' key.")

  # Count the number of times each username appears
  username_counts = Counter(usernames)
  # Get the top 10 usernames
  top_10_usernames = username_counts.most_common(10)

  return top_10_usernames