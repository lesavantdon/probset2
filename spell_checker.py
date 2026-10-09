
import re
from collections import defaultdict


class SpellChecker:
    def __init__(self, dictionary):
        self.dictionary = set(
            word.lower() for word in dictionary
        )

    def check_word(self, word):
        word = word.lower()
        return word in self.dictionary

    def suggest_corrections(self, word):
        word = word.lower()
        suggestions = set()

        # Deletions
        for i in range(len(word)):
            suggestions.add(
                word[:i] + word[i+1:]
            )

        # Transpositions
        for i in range(len(word) - 1):
            suggestions.add(
                word[:i] +
                word[i+1] +
                word[i] +
                word[i+2:]
            )

        # Replacements
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                suggestions.add(
                    word[:i] + c + word[i+1:]
                )

        # Insertions
        for i in range(len(word) + 1):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                suggestions.add(
                    word[:i] + c + word[i:]
                )

        return [
            s for s in suggestions
            if s in self.dictionary
        ]

    def check_text(self, text: str):
        words = re.findall(r'\b\w+\b', text.lower())

        misspelled = [
            word for word in words
            if not self.check_word(word)
        ]

        return misspelled

    def spell_check_and_suggest(self, text: str):
        misspelled_words = self.check_text(text)
        results = {}

        for word in misspelled_words:
            results[word] = self.suggest_corrections(word)

        return results


if __name__ == "__main__":
    dictionary = [
        "the", "quick", "brown",
        "fox", "jumps", "over",
        "lazy", "dog"
    ]

    checker = SpellChecker(dictionary)

    print(checker.check_word("quick"))
    print(checker.check_word("quik"))

    print(
        checker.spell_check_and_suggest(
            "the quik brown fox jumpps"
        )
    )
