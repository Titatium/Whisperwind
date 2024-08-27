class Object:
    """Represents an object in the game world."""

    def __init__(self, name, description, type, hidden_stats=None, value=0, can_pickup=True):
        self.name = name
        self.description = description
        self.type = type  # e.g., "weapon", "armor", "consumable", "misc"
        self.hidden_stats = hidden_stats or {}  # Dictionary of hidden attributes and their values
        self.value = value  # Gold value
        self.can_pickup = can_pickup  # Whether the player can take this object
        self.quantity = 1  # Default quantity is 1

    def get_descriptive_stat(self, stat_name):
        """Returns a descriptive phrase based on the hidden stat value."""
        value = self.hidden_stats.get(stat_name)
        if value is None:
            return "unknown"

        if stat_name == "nutrition":
            if value < 3:
                return "meager sustenance"
            elif value < 6:
                return "moderate nourishment"
            else:
                return "substantial sustenance"
        elif stat_name == "alcohol_content":
            if value < 5:
                return "mildly intoxicating"
            elif value < 8:
                return "moderately intoxicating"
            else:
                return "highly intoxicating"
        elif stat_name == "quenching":
            if value < 3:
                return "barely quenches thirst"
            elif value < 6:
                return "satisfyingly quenches thirst"
            else:
                return "completely quenches thirst"
        elif stat_name == "damage":
            if value < 3:
                return "minimal damage"
            elif value < 6:
                return "moderate damage"
            else:
                return "significant damage"
        elif stat_name == "concealment":
            if value < 5:
                return "easily noticeable"
            elif value < 10:
                return "somewhat concealed"
            else:
                return "well-hidden"
        elif stat_name == "healing":
            if value < 5:
                return "minor healing"
            elif value < 10:
                return "moderate healing"
            else:
                return "substantial healing"
        elif stat_name == "poison_resistance":
            if value < 5:
                return "weak poison resistance"
            elif value < 10:
                return "moderate poison resistance"
            else:
                return "strong poison resistance"
        elif stat_name == "herbalism_knowledge":
            if value < 3:
                return "basic herbalism knowledge"
            elif value < 6:
                return "intermediate herbalism knowledge"
            else:
                return "advanced herbalism knowledge"
        elif stat_name == "luck":
            if value < 3:
                return "a slight bit of luck"
            elif value < 6:
                return "a moderate amount of luck"
            else:
                return "a considerable amount of luck"
        elif stat_name == "divinity":
            if value < 3:
                return "a faint divine presence"
            elif value < 6:
                return "a noticeable divine presence"
            else:
                return "a strong divine presence"
        elif stat_name == "religious_knowledge":
            if value < 3:
                return "basic religious knowledge"
            elif value < 6:
                return "intermediate religious knowledge"
            else:
                return "deep religious knowledge"
        elif stat_name == "light_source":
            if value < 1:
                return "no light"
            elif value < 3:
                return "a dim light"
            else:
                return "a bright light"
        elif stat_name == "fey_energy":
            if value < 3:
                return "a faint fey energy"
            elif value < 6:
                return "a noticeable fey energy"
            else:
                return "a strong fey energy"
        elif stat_name == "growth_potential":
            if value < 1:
                return "little growth potential"
            elif value < 3:
                return "moderate growth potential"
            else:
                return "great growth potential"
        else:
            return "an unknown quality"

    @classmethod
    def from_data(cls, item_data):
        """Creates an Object instance from a dictionary of item data, 
           handling potential errors and data inconsistencies."""

        try:
            # Basic attribute assignment
            name = item_data["name"]
            description = item_data["description"]
            obj_type = item_data["type"]

            # Optional attributes with default values
            hidden_stats = item_data.get("hidden_stats", {})
            value = item_data.get("value", 0)
            can_pickup = item_data.get("can_pickup", True)

            # Data validation and error handling
            if not all([name, description, obj_type]):
                raise ValueError("Missing required attributes for object creation.")

            if obj_type not in ["weapon", "armor", "consumable", "misc"]:
                raise ValueError(f"Invalid object type: {obj_type}")

            # Create and return the Object instance
            return cls(name, description, obj_type, hidden_stats, value, can_pickup)

        except KeyError as e:
            print(f"Error loading object data: Missing key '{e.args[0]}'")
            return None
        except ValueError as e:
            print(f"Error loading object data: {e}")
            return None
