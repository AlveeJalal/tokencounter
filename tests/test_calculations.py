from calculator import characterCounter, calculateTokenCount, calculateTokenPriceInput, calculateTokenPriceOutput
from faker import Faker

def test_character_count():
    faker = Faker()
    text  = faker.texts(nb_texts=5)
    assert characterCounter(text) == 5

def test_token_count():
    assert calculateTokenCount(1000) == 250

def test_token_price():
    faker = Faker()
    text  = faker.texts(nb_texts=4000)
    characterCount = characterCounter(text)
    tokenCount = calculateTokenCount(characterCount)
    assert calculateTokenPriceInput(tokenCount) == 0.01
