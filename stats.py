def get_num_words(text):
    #defines a function called words that takes a string text as an argument
    return len(text.split())
    #splits the text into words using whitespace as the delimiter and returns the count of words
def get_character(text):
    counts = {}
    for ch in text.lower():
        if 'a' <= ch <= 'z':
            counts[ch] = counts.get(ch, 0) + 1
    return counts

   # return new_list
def sorted_list(character_counts):
    def sort_by_count(item):
        return item["num"]

    new_list = []
    for k, v in character_counts.items():
        new_list.append({"char": k, "num": v})
    new_list.sort(reverse=True, key=sort_by_count)
    return new_list

    


    
