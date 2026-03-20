

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-3eef122e5d104b7aa4d898379811a8aa-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NjY1OTUxNTcsInAiOnsicm9hIjp7Im5zIjpbIjFiZDhlNDgwLTc3YTktNDMzYi04N2M2LTdmNzBkOTZjOTQwMiJdfSwicnciOnsibnMiOlsiMWJkOGU0ODAtNzdhOS00MzNiLTg3YzYtN2Y3MGQ5NmM5NDAyIl19fSwicmlkIjoiZjBiYzIyODEtMTk4NC00NzhkLTg2ZmItMDJlNTk0MTRmZDU5In0.5cigbs3kr7JQ7F88JhyahJ8ZEzKNhzt9Nl9UVIX1oP6slrZj61jpQPHVXnvXGLty3OwLcZpfkwpG6j6uwbIEBQ",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

