import json
import os
from uuid import uuid4
from hbnb.persistence.i_persistence_manager import IPersistenceManager
"""
    Classe qui impléménte les opérations 
    de persistance des données CRUD
"""


class DataManager(IPersistenceManager):
    def __init__(self, storage_file='data.json'):
        self.storage_file = storage_file
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump({}, f)

    def _load_data(self):
        with open(self.storage_file, 'r') as f:
            return json.load(f)

    def _save_data(self, data):
        with open(self.storage_file, 'w') as f:
            json.dump(data, f, indent=4)

    def save(self, entity):
        data = self._load_data()
        entity_id = str(uuid4())
        entity['id'] = entity_id
        entity_type = entity['type']
        if entity_type not in data:
            data[entity_type] = {}
        data[entity_type][entity_id] = entity
        self._save_data(data)
        return entity_id

    def get(self, entity_id, entity_type):
        data = self._load_data()
        return data.get(entity_type, {}).get(entity_id, None)

    def update(self, entity):
        data = self._load_data()
        entity_id = entity['id']
        entity_type = entity['type']
        if not entity_id or not entity_type:
            raise ValueError("Entity must have 'id' and 'type' attribrutes.")
        if entity_type in data and entity_id in data[entity_type]:
            data[entity_type][entity_id] = entity
            self._save_data(data)
            return True
        else:
            raise KeyError(f"Entity with id '{entity_id}' and type '{entity_type}' not found.")

    def delete(self, entity_id, entity_type):
        data = self._load_data()
        if entity_type in data and entity_id in data[entity_type]:
            del data[entity_type][entity_id]
            self._save_data(data)
            return True
        return False

