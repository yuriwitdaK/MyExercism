def find_anagrams(word, candidates):
    """
    Find all anagrams of 'word' from a list of candidates.
    Supports Unicode characters (including Greek letters).
    Case-insensitive comparison.
    
    Args:
        word (str): The word to find anagrams for
        candidates (list): List of candidate words to check
        
    Returns:
        list: List of words that are anagrams of the input word
    """
    # Handle empty input
    if not word or not candidates:
        return []
    
    # Convert word to lowercase using casefold (better for Unicode)
    word_normalized = word.casefold()
    word_sorted = sorted(word_normalized)
    
    anagrams = []

    # check if its itself


    # Check each candidate
    for candidate in candidates:
        # Skip empty candidates
        if not candidate:
            continue

            
        # Convert candidate to lowercase using casefold
        candidate_normalized = candidate.casefold()

        # Skip if it's an exact match (word can't be anagram of itself)
        if candidate_normalized == word_normalized:
            continue
        
        candidate_sorted = sorted(candidate_normalized)

        
        # If sorted characters match, it's an anagram
        if word_sorted == candidate_sorted:
            anagrams.append(candidate)
    
    return anagrams
