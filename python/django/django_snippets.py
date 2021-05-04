import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

# get all models with app name
def get_all_models():
    from django.apps import apps

    print(apps)
    print(dir(apps))
    print(apps.all_models)
    for key, val in apps.all_models.items():
        #print(key, val)
        print('App Name', key , '-> Models : ')
        for v in val:
            print(v)
        print('\n')

# get table length of django in built.
def get_table_length():
    from django.db import connection
    print(connection.ops.max_name_length())
    print(dir(connection.ops))
    print(dir(connection.queries_log))

# /django/db/backends/postgresql/introspection.py

# get_table_list
def get_table_list():
    from django.db import connection
    with connection.cursor() as cursor:
        print(connection.introspection.get_table_list(cursor))


# get all tables
def get_all_tables():
    from django.db import connection
    #print(connection.introspection.django_table_names())
    for table in connection.introspection.django_table_names():
        print(table)
        yield table



# get key columsn
def get_key_columns():
    from django.db import connection
    for table in get_all_tables():
        with connection.cursor() as cursor:
            print(connection.introspection.get_key_columns(cursor, table))


# get_relations
def get_relations():
    from django.db import connection
    for table in get_all_tables():
        with connection.cursor() as cursor:
            print(connection.introspection.get_relations(cursor, table))


# get_indexes
def get_indexes():
    from django.db import connection
    for table in get_all_tables():
        with connection.cursor() as cursor:
            print(connection.introspection.get_indexes(cursor, table))

# get_constraints
def get_constraints():
    from django.db import connection
    for table in get_all_tables():
        with connection.cursor() as cursor:
            print(connection.introspection.get_constraints(cursor, table))


# get name of database, password, username
def get_connection_dbname():
    from django.db import connection
    print(connection.settings_dict)


if __name__ == '__main__':
    #get_all_models()
    #get_table_length()
    #get_all_tables()
    #get_key_columns()
    #get_relations()
    #get_table_list()
    #get_indexes()
    #get_constraints()
    get_connection_dbname()