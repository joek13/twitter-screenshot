import os

ENV = os.environ["ENV"] if "ENV" in os.environ else "prod"

if ENV not in ["dev", "prod"]:
    raise ValueError(f"Invalid value for ENV: '{ENV}'")