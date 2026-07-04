# two strings are anagram, if they contain the same letters, but not neccessarily in the same order (case does not matter)

# example: car and arc

# the key to determine this is to sort them, if the sorted strings are the same, then they are anagrams

def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.replace(' ', '').lower() # Removing spaces and converting to lowercase
    s2 = s2.replace(' ', '').lower()
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    

def main() -> None:
    s1 = 'Emperor Octavian'
    s2 = 'Captain over Rome'
    print(is_anagram(s1,s2))
    

if __name__ == "__main__":
    main()
    
    
# this function relies on python's built-in sorted function, so the runtime is O(n log n)

