from models import User, Session


def main():
    session = Session()

    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@gmail.com"
    )

    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
