from models import Session, User


def main():
    session = Session()
    query = session.query(User).filter(User.salary > 9000)
    for user in query.order_by(User.salary > 9000):
        print(user.first_name, user.last_name, user.email)


if __name__ == '__main__':
    main()
