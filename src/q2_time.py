from collections import Counter
from typing import List, Tuple
import emoji
import json

def q2_time(file_path: str) -> List[Tuple[str, int]]:
  data = []
  with open(file_path, 'r') as file_data:
    for line in file_data:
      try:
        # Attempt to parse each line as JSON and extract the "content"
        content = json.loads(line)["content"]
        data.append(content)
      except json.JSONDecodeError:
        print("Warning: Skipping a line that is not valid JSON.")
      except KeyError:
        print("Warning: Skipping a line missing the 'content' key.")

  # Guarda todos los emojis distintos.
  different_emojis = []
  for text in data:
    try:
      # Attempt to analyze the text for emojis
      emojis_in_text = [value.chars for value in emoji.analyze(text)]
      different_emojis.extend(emojis_in_text)
    except Exception as e:
      print(f"Warning: An error occurred while analyzing text for emojis: {e}")

  # Este apartado contara todos los emojis differentes
  emoji_counter = Counter(different_emojis)
  # Top 10 emojis mas usados
  top_10_emojis = emoji_counter.most_common(10)
  # Convertir el resultado a una lista de tuplas
  emojis = [(emoji, count) for emoji, count in top_10_emojis]
  return emojis