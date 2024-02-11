from calculator import characterCounter, calculateTokenCount
from faker import Faker

def test_character_count():
    faker = Faker()
    text  = faker.texts(nb_texts=5)
    assert characterCounter(text) == 5

def test_token_count():
    assert calculateTokenCount(5) == 2
