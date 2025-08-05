from mimesis import Generic
from mimesis.locales import Locale
import pandas as pd


def generate_fake_names(count=1_000_000, locale=Locale.AR_EG, output_file='fake_egyptian_names.csv'):
    faker = Generic(locale=locale)
    dummy_names = [faker.person.full_name() for _ in range(count)]

    df = pd.DataFrame({'Name': dummy_names})

    df.to_csv(output_file, index=False, encoding='utf-8-sig')

    print(f"CSV created with {len(dummy_names)} fake names.")

generate_fake_names()
