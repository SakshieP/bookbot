def get_num_words(text):
    words = text.split()
    return len(words)
def get_char_count(text):
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
def sort_char_counts(char_count_dict):
    sorted_list = []

    for char, count in char_count_dict.items():
        sorted_list.append({"char": char, "count": count})

    def sort_on(item):
        return item["count"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list