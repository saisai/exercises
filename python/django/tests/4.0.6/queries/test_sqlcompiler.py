
from django.db import DEFAULT_DB_ALIAS, connection
from django.db.models.sql import Query
from django.test import SimpleTestCase

from .models import Item

class SQLCompilerTest(SimpleTestCase):
    def test_repr(self):
        query = Query(Item)
        print(query)
        compiler = query.get_compiler(DEFAULT_DB_ALIAS, connection)
        #print(dir(compiler))
        self.assertEqual(
            repr(compiler),
            f"<SQLCompiler model=Item connection="
            f"<DatabaseWrapper vendor={connection.vendor!r} alias='default'> "
            f"using='default'>",
        )
        
        def show_dir():                
            for obj in [f for f in dir(compiler) if not f.startswith("_")]:
                print(obj, "=>",  getattr(compiler, obj))


