#!/usr/bin/env bash
allergies=(eggs peanuts shellfish strawberries tomatoes chocolate pollen cats)

score=$1
command=$2
item=$3

# Only keep lowest 8 bits (ignore extra bits)
score=$(( score & 255 ))

allergic_to() {
  local allergen="$1"
  local index=0

  for a in "${allergies[@]}"; do
    if [[ "$a" == "$allergen" ]]; then
      if (( score & (1 << index) )); then
        echo "true"
      else
        echo "false"
      fi
      return
    fi
    ((index++))
  done
}

list_allergies() {
  local output=""
  local index=0

  for a in "${allergies[@]}"; do
    if (( score & (1 << index) )); then
      output+="$a "
    fi
    ((index++))
  done

  if [[ -n "$output" ]]; then
    echo "${output%" "}"
  fi
}

case "$command" in
  allergic_to)
    allergic_to "$item"
    ;;
  list)
    list_allergies
    ;;
  *)
    echo "Invalid command"
    exit 1
    ;;
esac