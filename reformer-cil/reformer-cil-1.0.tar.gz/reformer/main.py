"""Сonversion of Cyrillic into Latin."""

from reform_dictionary import reformCyrillicToLatin


def reform_cyrillic_to_latin():
    print(
        "-------------------------------------\n\n"
        "~ There is reformer program thats can help you "
        "to convers of Cyrillic into Latin."
        "\n\n-------------------------------------\n"
    )

    userCyrillic = str.upper((input("~ Write your message here:\n\n> ")))

    latinResult = str()
    for letterNumber in userCyrillic:
        if letterNumber in reformCyrillicToLatin:
            letterValue = reformCyrillicToLatin[letterNumber]
            latinResult += letterValue
    
    print(f"\n{latinResult}")


if __name__ == "__main__":
    reform_cyrillic_to_latin()