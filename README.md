# Snowfakery Representation

Fake data to support representative names, topics, etc.

## Installation

Install with pip

`pip install faker-representation`

## Faker Use

```python
from faker import Faker
import faker_representation

fake = Faker()
fake.add_provider(faker_representation.Provider)

for _ in range(10):
    print(fake.nonbinary_name())
```

## Snowfakery Use

For now you will need to clone the repository and then follow the example in the [sample recipe](snowfakery_rep_example.recipe.yml).
