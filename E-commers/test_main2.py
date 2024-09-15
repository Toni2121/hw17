import sqlite3
import sqlite_lib2
import pytest


@pytest.fixture
def before_after_operations_db():
    # BEFORE
    sqlite_lib2.connect('E-commerce Customer Behavior - Sheet1.db')

    yield  # test_get_years

    # AFTER
    sqlite_lib2.close()


def test_gold(before_after_operations_db):
    # BEFORE
    # sqlite_lib.connect('hw.db')

    # Act
    result = sqlite_lib2.run_query_select('''
        SELECT count(*)
            FROM ecomm e
        WHERE "membership type" LIKE "gold"
    ''')

    # Assert
    assert result[0][0] == 117

    # AFTER
    # sqlite_lib.close()


def test_silver(before_after_operations_db):
    # BEFORE
    # sqlite_lib.connect('hw.db')

    # Act
    result = sqlite_lib2.run_query_select('''
        SELECT count(*)
            FROM ecomm e
        WHERE "membership type" LIKE "silver"
    ''')

    # Assert
    assert result[0][0] == 117

    # AFTER
    # sqlite_lib.close()


def test_bronze(before_after_operations_db):
    # BEFORE
    # sqlite_lib.connect('hw.db')

    # Act
    result = sqlite_lib2.run_query_select('''
        SELECT count(*)
            FROM ecomm e
        WHERE "membership type" LIKE "bronze"
    ''')

    # Assert
    assert result[0][0] == 116

    # AFTER
    # sqlite_lib.close()


