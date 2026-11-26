import os

line = (
    "Operator rated 5/5 for saying 'you know what I mean' "
    "with total confidence, and 1/5 for ever explaining "
    "what they mean. Promoted anyway."
)

# Entry must stay within 140 characters.
assert len(line) <= 140

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
