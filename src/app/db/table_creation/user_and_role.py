import sys
from pathlib import Path

# Add the src directory to the path so app can be imported
src_path = Path(__file__).parent.parent.parent.parent  # Go up to src/
sys.path.insert(0, str(src_path))

from app.db.database_helpers.database import engine, Base
from app.db.model_to_db.models import User, Role

Base.metadata.create_all(engine)

print("User and Role tables created successfully.")