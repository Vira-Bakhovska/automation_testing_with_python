import pytest
import sqlite3
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    biscuit_qnt = db.select_product_qnt_by_id(4)

    assert biscuit_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "test", "data", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()

    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


@pytest.mark.database
def test_insert_into_not_existent_table():
    db = Database()

    with pytest.raises(sqlite3.OperationalError) as excinfo:
        db.insert_data_into_non_existent_table()
    # print (str(excinfo.value))

    assert f"no such table: non_existen" in str(excinfo.value)


@pytest.mark.database
def test_insert_with_invalide_encoding():
    db = Database()
    db.insert_with_invalid_encoding()
    record = db.select_product_name_by_id(999)

    assert record[0] != "é", "Data integrity not maintained with invalid encoding."


@pytest.mark.database
def test_data_consistency():
    db = Database()
    record = db.get_data_consistency()

    assert len(record) == 0


@pytest.mark.database
def test_product_qnt_datatype():
    db = Database()
    record = db.select_product_qnt()
    for item in record:
        assert isinstance(item[0], int) == True


@pytest.mark.database
def test_postal_code_format():
    db = Database()
    record = db.select_postal_codes()
    for item in record:
        assert len(item[0]) == 4
        assert item[0].isdigit()
