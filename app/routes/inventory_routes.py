# app/routes/inventory_routes.py

from flask import Blueprint, request, jsonify
from app.services.inventory_service import InventoryService

inventory_bp = Blueprint("inventory", __name__)
service = InventoryService()

@inventory_bp.get("/")
def listar_items():
    items = service.listar_items()
    return jsonify([item.to_dict() for item in items]), 200

@inventory_bp.get("/<int:item_id>")
def obtener_item(item_id):
    item = service.obtener_item(item_id)
    if not item:
        return jsonify({"error": "Item no encontrado"}), 404
    return jsonify(item.to_dict()), 200

@inventory_bp.post("/")
def crear_item():
    data = request.get_json() or {}
    try:
        item = service.crear_item(data)
        return jsonify(item.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@inventory_bp.put("/<int:item_id>")
def actualizar_item(item_id):
    data = request.get_json() or {}
    try:
        item = service.actualizar_item(item_id, data)
        if not item:
            return jsonify({"error": "Item no encontrado"}), 404
        return jsonify(item.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@inventory_bp.delete("/<int:item_id>")
def eliminar_item(item_id):
    ok = service.eliminar_item(item_id)
    if not ok:
        return jsonify({"error": "Item no encontrado"}), 404
    return jsonify({"message": "Item eliminado"}), 200
