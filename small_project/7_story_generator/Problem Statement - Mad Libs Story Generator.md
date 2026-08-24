Write a program that reads a story template from a file (`story.txt`), identifies placeholder words enclosed in angle brackets (e.g., `<noun>`, `<verb>`), prompts the user to replace each unique placeholder with a custom word, substitutes those words back into the story, and prints the final completed story.

#### Requirements:

1. **Read Input**: Open and read the entire contents of `story.txt`.
    
2. **Extract Placeholders**: Scan through the story and find all words wrapped in `<` and `>`. Each placeholder should be collected **once** (unique values only), even if it appears multiple times in the story.
    
3. **Collect Answers**: For each unique placeholder found, prompt the user with:  
    `Enter a word for <placeholder>:`  
    Store the user's input in a dictionary mapping each placeholder to its replacement.
    
4. **Substitute & Output**: Replace every occurrence of each placeholder in the original story with the corresponding user-provided word, then print the final story.