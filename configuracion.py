"""Configuración central de conexión a SQLite y sesiones SQLAlchemy."""
from pathlib import Path
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'clinicas_veterinarias.db'}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)

# SQLite no aplica claves foráneas si no se habilitan explícitamente.
@event.listens_for(engine, "connect")
def activar_claves_foraneas(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

def obtener_sesion():
    """Entrega una sesión nueva; quien la use debe cerrarla."""
    return SessionLocal()
