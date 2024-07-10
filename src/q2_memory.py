from collections import Counter
from typing import List, Tuple
import json
import emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if 'content' in data:
                # Use a generator expression for memory efficiency
                emojis = (value.chars for value in emoji.analyze(data['content']))
                emoji_counter.update(emojis)
    top_10_emojis = emoji_counter.most_common(10)
    return top_10_emojis