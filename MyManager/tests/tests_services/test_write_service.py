# Тесты для методов сервисов


import pytest

from MyManager.core.entities import StructDataOfTransaction


class TestWriteService:

    class TestFuncAdd:
        def test_add_to_exist_bd(self, write_service_with_bd, read_service_with_bd):

            write_service_with_bd.add(
                new_date="06.10.2026",
                new_amount="50.0",
                new_type_op="expense",
                new_description="Купил булочку с корицей в столовой"
            )

            got = read_service_with_bd.get_all()

            assert got == [
        StructDataOfTransaction(id=1, date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=3, date="02.01.2024", amount=550.0,
                                typeOp="expense", description="Стрижка в парикмахерской"),
        StructDataOfTransaction(id=4, date="06.10.2026", amount=50.0,
                                typeOp="expense", description="Купил булочку с корицей в столовой"),
    ]

        def test_add_to_empty_bd(self, write_service_without_bd, read_service_without_bd):
        
            write_service_without_bd.add(
                new_date="06.10.2026",
                new_amount="50.0",
                new_type_op="expense",
                new_description="Купил булочку с корицей в столовой"
            )

            got = read_service_without_bd.get_all()

            assert got == [
        StructDataOfTransaction(id=1, date="06.10.2026", amount=50.0,
                                typeOp="expense",  description="Купил булочку с корицей в столовой"),
    ]
            
        def test_add_incorrect_data(self, write_service_with_bd):

            with pytest.raises(ValueError):
                write_service_with_bd.add(
                    new_date="06.10.2026",
                    new_amount="пятьдесят рублей",  # Сломает float()
                    new_type_op="expense",
                    new_description="Булочка"
                )

        def test_add_return_data(self, write_service_with_bd):

            got_data_for_checking = write_service_with_bd.add(
                new_date="06.10.2026",
                new_amount="50.0",
                new_type_op="expense",
                new_description="Купил булочку с корицей в столовой"
                )


            assert got_data_for_checking == StructDataOfTransaction(4,
                                                                    "06.10.2026", 
                                                                    50.0,
                                                                    "expense",
                                                                    "Купил булочку с корицей в столовой")


    class TestFuncChangeData:
        @pytest.mark.parametrize(
            ("new_data", "got_bd"),
            [((1, "01.01.2023", 25000.0, "income", "Зарплата"), [
        StructDataOfTransaction(id=1, date="01.01.2023", amount=25000.0,
                                typeOp="income",  description="Зарплата"),
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=3, date="02.01.2024", amount=550.0,
                                typeOp="expense", description="Стрижка в парикмахерской")
    ]),
             ((3, "05.10.2026", 550.0, "expense", "Стрижка"), [
        StructDataOfTransaction(id=1, date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=3, date="05.10.2026", amount=550.0,
                                typeOp="expense", description="Стрижка")
    ])]
        )
        def test_change_data_positive(self, read_service_with_bd, write_service_with_bd, new_data, got_bd):

            write_service_with_bd.change_data(
                find_id=new_data[0],
                changed_date=new_data[1],
                changed_amount=new_data[2],
                changed_type_op=new_data[3],
                changed_description=new_data[4]
            )

            got_changed_bd = read_service_with_bd.get_all()

            assert got_changed_bd == got_bd


    class TestFuncDeleteData:

        @pytest.mark.parametrize(
            ("id_for_deleting", "got_bd"),
            [(1, [
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе"),
        StructDataOfTransaction(id=3, date="02.01.2024", amount=550.0,
                                typeOp="expense", description="Стрижка в парикмахерской")
    ]),
             (3, [
        StructDataOfTransaction(id=1, date="01.01.2024", amount=100.0,
                                typeOp="income",  description="зарплата"),
        StructDataOfTransaction(id=2, date="02.01.2024", amount=50.5,
                                typeOp="expense", description="кофе")
    ])]
        )
        def test_delete_data_positive(self, read_service_with_bd, write_service_with_bd, id_for_deleting, got_bd):

            write_service_with_bd.delete_data(id_for_deleting)

            got_changed_bd = read_service_with_bd.get_all()

            assert got_bd == got_changed_bd    