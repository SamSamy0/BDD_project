"""
Reads the SQL queries
"""


def load_query(path):
    with open(path, "r", encoding="utf-8") as f:
        query = f.read()
    return query
