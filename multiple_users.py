from faker import Faker
from models import Session, User


def create_fake_users(count=10):
    fake = Faker()
    return [
        User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            salary=fake.pyfloat(
                positive=True,
                min_value=4000,
                max_value=10_000
            ),
        )
        for _ in range(count)
    ]


def main():
    session = Session()
    users = create_fake_users()
    session.add_all(users)
    session.commit()


if __name__ == '__main__':
    main()
