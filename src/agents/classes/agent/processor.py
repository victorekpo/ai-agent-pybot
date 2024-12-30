import json

from datetime import datetime


def _try_to_parse(self, obj):
    """Attempt to parse JSON in multiple ways."""
    try:
        return json.loads(obj)
    except Exception:
        pass
    try:
        return json.loads(f"[{obj}]")
    except Exception:
        pass
    return None


def process_information(self, _type, key, raw_value, limit=-1, cache=True):
    value = "\r\n".join(raw_value) if isinstance(raw_value, list) else raw_value
    formatted_value = value  # Optional formatting logic can be added here.

    if value and limit != 0:
        item_exists = any(
            isinstance(entry, dict) and (
                    entry["type"] == _type and entry["key"] == key and entry["value"] == formatted_value
            )
            for entry in self.brain
        )

        if item_exists:
            print("Item already exists in brain.", formatted_value)
            return

        if not item_exists:
            self.brain.append({
                "type": _type,
                "key": key,
                "value": formatted_value,
                "timestamp": datetime.now().isoformat()
            })

        if limit > 0:
            self.brain = self.brain[-limit:]

    self.save_brain()
