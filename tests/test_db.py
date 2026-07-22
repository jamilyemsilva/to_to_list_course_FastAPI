from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='jami1', password='password', email='jami1@example.com'
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'jami1@example.com')
    )

    assert result.id == 1
