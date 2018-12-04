#!/usr/bin/env python3

import random
from faker import Faker

fake = Faker()
with open("scores.txt", "w") as f:
    for _ in range(25):
        name = fake.name()
        score = random.randint(78, 101)
        print(f"{name}\t{score}", file=f)
