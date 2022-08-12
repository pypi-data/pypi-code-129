"""Main class to generate random names."""
import random
from typing import Dict, List, Optional, Tuple

import yaml

import marko_namo.utils as ut
from marko_namo.go_daddy import GoDaddy


class MarkoNamo:
    """General class to generate random names using a markov-chain approach."""

    def __init__(
        self,
        name_length: Optional[int] = None,
        number_of_names: Optional[int] = None,
        training_words: Optional[List[str]] = None,
        n_grams: Optional[List[int]] = [1, 2, 3],
        godaddy_key: Optional[str] = None,
        godaddy_secret: Optional[str] = None,
        godaddy_env: Optional[str] = None,
        domain_extensions: Optional[List[str]] = None,
        config_file: Optional[str] = None,
    ) -> None:
        """Initialise the class.

        Provide either the arugment inputs OR the path to a config yml with the required keys

        Args:
            name_length (int): Maximum word length for the generated name
            number_of_names (int): How many names to attempt to create
            training_words (List[str]): The words to learn from for the generation process
            n_grams (List[int], optional): Word parts to use in the learning phase
                Defaults to [1, 2, 3].
            godaddy_key (Optional[str], optional): API Key for GoDaddy. Defaults to None.
            godaddy_secret (Optional[str], optional): API Secret for GoDaddy.
                Defaults to None.
            godaddy_env (Optional[str], optional): Which GoDaddy environment to use; OTE or PROD.
                Defaults to None.
            domain_extensions (List[str]): Desired web domain extensions to examine, eg .com, etc
            config_file (Optional[str], optional): Path to the config file. Defaults to None.
        """
        self.name_length = name_length
        self.number_of_names = number_of_names
        self.n_grams = n_grams
        self.domain_extensions = domain_extensions
        self.training_words = training_words
        self.godaddy_key = godaddy_key
        self.godaddy_secret = godaddy_secret
        self.godaddy_env = godaddy_env

        if config_file:
            config = yaml.safe_load(open(config_file))
            self.name_length = config["parameters"]["maximum_name_length"]
            self.number_of_names = config["parameters"]["number_of_names"]
            self.training_words = config["training_words"]
            self.n_grams = config["parameters"]["n_grams"]
            self.domain_extensions = config.get("extensions", None)

            if "godaddy" in config:
                self.godaddy_key = config["godaddy"]["key"]
                self.godaddy_secret = config["godaddy"]["secret"]
                self.godaddy_env = config["godaddy"]["env"]

        # Check if GoDaddy credentials were provided & create a connection if so
        self.godaddy = None
        if all([self.godaddy_key, self.godaddy_secret, self.godaddy_env]):
            self.instantiate_godaddy

    def instantiate_godaddy(self) -> None:
        """Instantiates a GoDady class."""
        assert self.godaddy_key is not None
        assert self.godaddy_secret is not None
        assert self.godaddy_env is not None

        self.godaddy = GoDaddy(  # type: ignore
            key=self.godaddy_key,
            secret=self.godaddy_secret,
            env=self.godaddy_env,
        )

    def create_random_names(self) -> Tuple[list, Optional[list]]:
        """Main method to generate random names.

        Returns:
            Tuple[list, list]:
                - Created Names
                - If goDaddy credentials provided, price & availability info for each available name
        """
        # Ensure minimum required items are present
        assert self.training_words is not None
        assert self.name_length is not None
        assert self.number_of_names is not None

        random_words = [
            self.create_random_word(self.training_words, self.name_length)
            for x in range(0, self.number_of_names)
        ]
        random_words = list(set(random_words))

        created_names = []
        available_domain_names: List[str] = []

        # If no goDaddy info is provided simply return the randomly created words
        if self.godaddy is None:
            created_names = random_words
        else:
            available_domains = [
                x
                for x in self.godaddy.check_domain_availability(
                    random_words, self.domain_extensions
                )["domains"]
            ]

            # Check if all domains are available
            for rw in random_words:
                all_available_extensions = [
                    x
                    for x in available_domains
                    if x["domain"].split(".")[0] == rw and x["available"]
                ]
                if len(all_available_extensions) == len(self.domain_extensions):
                    for x in all_available_extensions:
                        x.update({"price": x["price"] / 1000000})
                    available_domain_names.extend(all_available_extensions)
                    created_names.append(rw)

        print("Generated Names:")
        [print(x) for x in created_names]
        print("")
        if len(available_domain_names) == 0:
            print("Did not check for domain name availability or no domains available")
        else:
            [print(x) for x in available_domain_names]

        return (
            created_names,
            available_domain_names if len(available_domain_names) > 0 else None,
        )

    def word_letter_frequency(self, word: str) -> dict:
        """For a given word, build a frequency (markov) table for the proceeding characters.

        It will examine n-grams both as the reference point and the characters following.
        Eg, with a sample word of "abcd"
            - n-gram of 1:
                {
                    "a": ["b"],
                    "b": ["c"],
                    "c": ["d"],
                    "d": [None],
                }
            - n-gram of 2:
                {
                    "ab": ["cd"],
                    "bc": ["d"],
                    "cd": [None]
                }
            - etc

        Args:
            word (str): The word to build a frequency table for

        Returns:
            dict:
                - Keys correspond to the n-gram/s charaters
                - Values are lists of the proceeding n-gram/s characters

        """
        frequency_table: Dict[str, List[Optional[str]]] = {}
        assert self.n_grams is not None
        for i in range(0, len(word)):
            for j in self.n_grams:
                if len(word) >= i + j:
                    if word[i : i + j] not in frequency_table:
                        frequency_table[word[i : i + j]] = []

                    for gram_size in self.n_grams:
                        next_letters = (
                            None
                            if i + j + gram_size > len(word)
                            else word[i + j : i + j + gram_size]
                        )
                        frequency_table[word[i : i + j]].append(next_letters)

        return frequency_table

    def create_random_word(
        self, reference_words: List[str], maximum_word_length: int = 100
    ) -> str:
        """Builds a random word of length N based on the learnt frequency table.

        Args:
            reference_words (list): Words to learn from
            maximum_word_length (int, optional): How long the word is allowed to be. Note:
                - Word can be longer than max if the next random addition is an n-gram exceeding
                  the delta between the current word length and the max value
                - Defaults to 100.

        Returns:
            str: Randomly generated word
        """
        term_frequencies: Dict[str, List[str]] = {}
        for word in reference_words:
            tmp = self.word_letter_frequency(word)
            term_frequencies = ut.merge_dictionaries(term_frequencies, tmp)

        letter = random.choice(list(term_frequencies))
        word = letter

        while letter is not None and len(word) < maximum_word_length:
            letter = random.choice(term_frequencies[letter])
            word = f"{word}{letter if letter else ''}"

        return word.strip()
