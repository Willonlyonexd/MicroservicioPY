# run.py

from app import create_app, db
from app.models.inventory_item import InventoryItem  # importa modelos para crear tablas

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # crea las tablas la primera vez
    app.run(host="0.0.0.0", port=5000, debug=True)
