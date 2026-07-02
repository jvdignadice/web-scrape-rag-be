import sys
from pathlib import Path

# Add the src directory to the path
src_path = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(src_path))

from sqlalchemy import text
from app.db.database_helpers.database import engine, Base
from app.db.model_to_db.models import User, Role

print("Connecting to database...")
try:
    with engine.connect() as connection:
        print(f"✓ Connected successfully to: {engine.url}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
    sys.exit(1)

# Drop all existing tables
print("\nDropping existing tables...")
Base.metadata.drop_all(engine)
print("✓ Tables dropped")

# Recreate tables with new schema
print("\nCreating tables with updated schema...")
Base.metadata.create_all(engine)
print("✓ Tables created")

# Verify tables were created
print("\nVerifying tables...")
with engine.connect() as connection:
    result = connection.execute(text("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public'
    """))
    tables = [row[0] for row in result]
    print(f"✓ Tables in database: {tables}")

print("\n✓ Migration completed successfully!")


