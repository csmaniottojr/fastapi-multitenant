from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable

from models import *

if __name__ == "__main__":
    for table in Base.metadata.tables.values():
        if table.schema != "tenant":
            table_str = str(CreateTable(table).compile(dialect=postgresql.dialect()))
            print(f"{table_str.rstrip()};")

    schemas = ["cia_a", "cia_b"]
    for schema in schemas:
        print(f'create schema "{schema}" authorization pythonsul;\n\n')
        for table in Base.metadata.tables.values():
            if table.schema == "tenant":
                table_str = str(
                    CreateTable(table).compile(dialect=postgresql.dialect())
                )
                table_str = table_str.replace("tenant", f'"{schema}"')
                print(f"{table_str.rstrip()};")
