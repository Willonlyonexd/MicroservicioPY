# app/repositories/inventory_repository.py

from app import db
from app.models.inventory_item import InventoryItem

class InventoryRepository:

    def get_all(self):
        return InventoryItem.query.all()

    def get_by_id(self, item_id: int):
        return InventoryItem.query.get(item_id)

    def create(self, data: dict):
        item = InventoryItem(**data)
        db.session.add(item)
        db.session.commit()
        return item

    def update(self, item: InventoryItem, data: dict):
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    def delete(self, item: InventoryItem):
        db.session.delete(item)
        db.session.commit()
