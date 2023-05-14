from models import Session, User


def main():
    session = Session()
    query = session.query(User).filter(
        User.salary.between(5000, 6000)
    ).order_by(User.salary.desc())
    for user in query.limit(3):
        print(user.first_name, user.last_name, user.email)

    print('------------------')
    # one, scalar, first, get
    result = session.query(User).filter(
        User.salary > 5_000_000
    ).scalar()
    print(result)

    print('------------------')
    # all
    result = session.query(User).filter(
        User.first_name.like("A%")
    ).all()
    print(result)

    print('------------------')
    query = session.query(
        User.id, User.email, User.creation_date
    ).filter(
        User.salary.between(5000, 6000),
        User.first_name.like("J%")
    ).order_by(
        User.salary.desc(),
        User.creation_date.asc()

    )
    for row in query:
        print(row.id, row.email, row.creation_date)


if __name__ == '__main__':
    main()


