# app/services/inventory_service.py

from app.repositories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self, repository: InventoryRepository | None = None):
        self.repository = repository or InventoryRepository()

    def listar_items(self):
        return self.repository.get_all()

    def obtener_item(self, item_id: int):
        return self.repository.get_by_id(item_id)

    def crear_item(self, data: dict):
        # Validaciones básicas
        if data.get("cantidad", 0) < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if data.get("precio_unitario", 0) < 0:
            raise ValueError("El precio unitario no puede ser negativo")
        return self.repository.create(data)

    def actualizar_item(self, item_id: int, data: dict):
        item = self.repository.get_by_id(item_id)
        if not item:
            return None

        if "cantidad" in data and data["cantidad"] < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if "precio_unitario" in data and data["precio_unitario"] < 0:
            raise ValueError("El precio unitario no puede ser negativo")

        return self.repository.update(item, data)

    def eliminar_item(self, item_id: int):
        item = self.repository.get_by_id(item_id)
        if not item:
            return None
        self.repository.delete(item)
        return True
