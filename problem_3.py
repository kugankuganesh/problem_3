def count_words_in_file(filename: str) -> int:
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            return word_count, text  
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return -1, '' 

filename = r'c:\Users\akhla\OneDrive\Desktop\python Assestment\sample.txt'
word_count, file_text = count_words_in_file(filename)

if word_count != -1:
    print(f"Number of words in '{filename}': {word_count}")
    print(f"File contents:\n{file_text}")
