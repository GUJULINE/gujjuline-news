#!/bin/bash

# Auto-generate fixed article page with preset content
TITLE="Nifty Crosses 25,000"
IMAGE="https://source.unsplash.com/600x400/?nifty,stocks"
PARA1="Nifty 50 crosses 25,000 for the first time in history."
PARA2="Today’s rally added 300+ points as global cues remain positive."

# Output file
FILENAME="stock-market.html"

# Use template and replace placeholders
cat article/template.html \
  | sed "s|{{TITLE}}|$TITLE|g" \
  | sed "s|{{IMAGE}}|$IMAGE|g" \
  | sed "s|{{PARA1}}|$PARA1|g" \
  | sed "s|{{PARA2}}|$PARA2|g" \
  > article/$FILENAME

echo "✅ Article created at: article/$FILENAME"
