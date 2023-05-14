from random import choice

from models import User, Session


def main():
    session = Session()
    users = session.query(User).all()

    victim = choice(users)
    print(f"The victim is {victim}")

    session.delete(victim)
    session.commit()

    result = session.query(User).get(victim.id)
    assert result is None, "The user was not deleted"


if __name__ == '__main__':
    main()
