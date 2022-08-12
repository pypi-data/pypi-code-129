class english:

    # Pass string as an argument
    # Returns True or False based on if string is simile

    def isSimile(string):
        if " as " in string or " like " in string:
            return True
        return False
    
    # Pass text as an argument
    # Returns the grade level of writing

    def analyze(text):
        useforletters = [",", ";", ".", "!", "?", '"', ":", "'", " "]
        useforsentences = [".", "?", "!"]

        letters = 0
        words = 1
        sentences = 0

        # Get number of letters

        for x in text:
            if x in useforletters:
                pass
            else:
                letters += 1
        
        # Get number of words

        for y in text:
            if y == " ":
                words += 1
            else:
                pass

        # Get number of sentences

        for z in text:
            if z in useforsentences:
                sentences += 1
            else:
                pass

        L = letters / words * 100
        S = sentences / words * 100

        index = 0.0588 * L - 0.296 * S - 15.8

        index = round(index)

        # Print Grade Level

        if index < 1:
           return("Before Grade 1")
        elif index > 1 and index < 16:
            return(f"Grade {index}")
        else:
            return("Grade 16+")

    # Pass text as an argument
    # Returns word count

    def word_count(text):
        useforletters = [",", ";", ".", "!", "?", '"', ":", "'", " "]

        letters = 0

        for x in text:
            if x in useforletters:
                pass
            else:
                letters += 1