def capital_usage_validator(word):
    # Check if the word meets any of the correct capitalization conditions
    return word.isupper() or word.islower() or word.istitle()


# Example Test
print(capital_usage_validator("USA"))  # Output: True
print(capital_usage_validator("Google"))  # Output: True
print(capital_usage_validator("flaG"))  # Output: False
