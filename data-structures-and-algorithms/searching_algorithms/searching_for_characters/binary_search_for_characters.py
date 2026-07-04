from typing import List


def binary_search(a_list, n):
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


def character_binary_search1(word, n):
    first = 0
    last = len(word) - 1
    for i in word:
        if ord(i) == ord(n):
            return True


# Goddamn it, i forgot to sort the list

def character_binary_search2(a_list, n):
    first = 0
    last = len(a_list) - 1
    a_list = sorted(a_list)
    while last >= first:
        mid = (first + last) // 2
        if ord(a_list[mid]) == ord(n):
            return True
        else:
            if ord(a_list[mid]) > ord(n):
                last = mid - 1
            else:
                first = mid + 1
    return False


def character_binary_search3(word: str, n: str) -> bool:
    first: int = 0
    last: int = len(word) - 1
    a_list: List = sorted(list(word))
    while last >= first:
        mid: int = (first + last) // 2
        if ord(a_list[mid]) == ord(n):
            return True
        else:
            if ord(a_list[mid]) > ord(n):
                last = mid - 1
            else:
                first = mid + 1
    return False


def character_binary_search4(word: str, n: str) -> bool:
    # explicitly converts the haystack to a list of sorted unicode characters
    first: int = 0
    last: int = len(word) - 1
    a_list: List[int] = sorted(list(map(
        lambda i: ord(i),
        word
    )))
    needle: int = ord(n)
    while last >= first:
        mid: int = (first + last) // 2
        if a_list[mid] == needle:
            return True
        else:
            if a_list[mid] > needle:
                last = mid - 1
            else:
                first = mid + 1
    return False


def word_in_list_binary_search(list_of_words: List[str], word: str) -> bool:
    # Performs a binary search on a list of alphabetically sorted words and returns whether it exists in the list
    # case-sensitive
    a_list = sorted(list_of_words)
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == word:
            return True
        else:
            if a_list[mid] > word:
                last = mid - 1
            else:
                first = mid + 1
    return False
    

def main() -> None:
    print("Result: ", character_binary_search4(list("system"), 'e'))  # true
    print("Result: ", character_binary_search4(list("Apartment"), 'g'))  # false
    
    print("Result: ", word_in_list_binary_search(['hi', 'dude', 'Bam'], "dude")) # true
    print("Result: ", word_in_list_binary_search(['Yup', 'Hello', 'pen'], "Pencil")) # false
    print("Result: ", word_in_list_binary_search(['hi', 'dude', 'Bam'], "Dude")) # false


if __name__ == "__main__":
    main()
