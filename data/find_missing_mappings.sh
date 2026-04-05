#!/bin/bash
# Find missing icon mappings
echo "Checking missing icons..."
for cat in Swords Axes Hammers "Body Armor" Helms Shields "Paladin Shields" Staves Katars Polearms "Missile Weapons" Wands Daggers Scepters; do
  echo "=== $cat ==="
  items=$(jq -r ".[\"$cat\"][] | .name_en" base_items.json 2>/dev/null)
  for name in $items; do
    slug=$(echo "$name" | tr '[:upper:]' '[:lower:]' | sed "s/ /_/g" | sed "s/'/_/g")
    if [ ! -f "../assets/items/base/${slug}.jpg" ]; then
      echo "MISSING: $name -> $slug"
      # Try to find similar
      similar=$(ls ../assets/items/base/ | grep -i "${slug:0:4}" | head -3)
      if [ -n "$similar" ]; then
        echo "  Similar: $similar"
      fi
    fi
  done
done
