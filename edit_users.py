from random import choice

from models import User, Session


def main():
    session = Session()
    users = session.query(User).all()

    lucky_user = choice(users)
    print(f"The lucky user is {lucky_user} with id {lucky_user.id}")
    print(f"His/her salary is {lucky_user.salary}")

    prev_salary = lucky_user.salary
    lucky_user.salary *= 1.15

    session.add(lucky_user)
    session.commit()

    result = session.query(User).get(lucky_user.id)
    assert result.salary != prev_salary, "Salary was not updated"


if __name__ == '__main__':
    main()