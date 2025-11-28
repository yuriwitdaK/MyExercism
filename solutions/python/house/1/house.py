def recite(start, end):
    poem_elements = [
        "the malt that lay in",
        "the rat that ate",
        "the cat that killed",
        "the dog that worried",
        "the cow with the crumpled horn that tossed",
        "the maiden all forlorn that milked",
        "the man all tattered and torn that kissed",
        "the priest all shaven and shorn that married",
        "the rooster that crowed in the morn that woke",
        "the farmer sowing his corn that kept",
        "the horse and the hound and the horn that belonged to"
    ]

    all_lines = []

    for verse_num in range(1, 13):
        line_parts = ["This is"]
        if verse_num > 1:
            # Wichtig: die letzten verse_num-1 Elemente **rückwärts**
            line_parts += poem_elements[verse_num-2::-1]
        line_parts.append("the house that Jack built.")
        all_lines.append(" ".join(line_parts))

    return all_lines[start-1:end]
