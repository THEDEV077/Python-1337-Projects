import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print("Testing create_air:", alchemy.create_air())
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    print(alchemy.create_earth())
except Exception as e:
    print("Testing the hidden create_earth:", e)
