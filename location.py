import json

class Location:
    """Represents a location in the game world."""

    def __init__(self, name, description, exits={}, objects={}, npcs=[], ascii_art="", 
                 hidden_areas={}, requirements=[], special_events=[]):
        self.name = name
        self.description = description
        self.exits = exits  # Dictionary of exits: {"direction": "connected_location_name"}
        self.objects = objects  # Dictionary of objects: {"object_name": Object instance}
        self.npcs = npcs  # List of NPC instances
        self.ascii_art = ascii_art  # ASCII art representation of the location
        self.hidden_areas = hidden_areas  # Dictionary of hidden areas: {"area_name": (requirements, description)}
        self.requirements = requirements  # List of requirements to access this location
        self.special_events = special_events  # List of functions to trigger special events

    @classmethod
    def load_location(cls, location_name):
        """Loads location data from a JSON file."""
        with open("location_data.json", "r") as f:
            location_data = json.load(f)
        return cls(**location_data[location_name])

    def enter(self, player):
        """Handles entering the location, potentially triggering events or encounters."""
        print(self.description)

        # Trigger any special events associated with this location
        for event in self.special_events:
            event(player, self)  # Pass the player and location objects to the event function

        # Check for hidden areas and reveal them if requirements are met
        for area_name, (reqs, desc) in self.hidden_areas.items():
            if player.meets_requirements(reqs):
                print(f"\nYou discover a hidden area: {area_name}")
                print(desc)
                # Optionally, add the hidden area to the location's exits or objects

    def add_object(self, obj):
        """Adds an object to the location."""
        self.objects[obj.name] = obj

    def remove_object(self, obj_name):
        """Removes an object from the location."""
        if obj_name in self.objects:
            del self.objects[obj_name]

    def add_npc(self, npc):
        """Adds an NPC to the location."""
        self.npcs.append(npc)

    def remove_npc(self, npc_name):
        """Removes an NPC from the location."""
        self.npcs = [npc for npc in self.npcs if npc.name != npc_name]

#