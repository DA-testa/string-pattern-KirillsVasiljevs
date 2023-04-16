# Kirills Vasiljevs 221RDB427

def read_input():
    text = input()

    if "I" in text[:1]:
        text1 = input()
        text2 = input()
    else:
        with open("./tests/06", "r") as f:
            text1 = f.readline()
            text2 = f.readline()
    return text1.rstrip(), text2.rstrip()

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    result = []
    hash_pattern = hash(pattern)
    # Find the match
    # Calculate hash value for pattern and text
    for i in range(len(text) - len(pattern) + 1):
        hash_text = hash(text[i:i + len(pattern)])
        if hash_text == hash_pattern:
            if text[i:i + len(pattern)] == pattern:
                result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))