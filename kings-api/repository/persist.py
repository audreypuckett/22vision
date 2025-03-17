from data.David import DAVID
from data.Solomon import SOLOMON
from repository.create_db import create_tables
from repository.repo import insert_king, get_all_kings

# david_id = insert_king(DAVID)
#
# # Insert Solomon
# SOLOMON.predecessor_id = david_id
# solomon_id = insert_king(SOLOMON)
#
# print(f"David inserted with ID: {david_id}")
# print(f"Solomon inserted with ID: {solomon_id}")

print(get_all_kings())
