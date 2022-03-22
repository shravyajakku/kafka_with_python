from faker import Faker

fake = Faker()

def get_registered_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "Year of birth": fake.year()
    }

if __name__ == "__main__":
    print(get_registered_user())