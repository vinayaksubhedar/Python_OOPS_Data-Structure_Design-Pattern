class TreeType:
    """Flyweight class representing different types of trees"""
    _tree_types = {}

    def __new__(cls, name, color, texture):
        if name not in cls._tree_types:
            cls._tree_types[name] = super().__new__(cls)
            cls._tree_types[name].name = name
            cls._tree_types[name].color = color
            cls._tree_types[name].texture = texture
        return cls._tree_types[name]

    def display(self, x, y):
        """Display tree with its unique position (extrinsic state)"""
        print(f"Tree: {self.name}, Color: {self.color}, Texture: {self.texture}, Position: ({x}, {y})")

# Usage
oak1 = TreeType("Oak", "Green", "Rough")
oak2 = TreeType("Oak", "Green", "Rough")  # Reuses existing Oak object
pine1 = TreeType("Pine", "Dark Green", "Smooth")
pine2 = TreeType("Pine", "Dark Green", "Smooth")

print(pine1 is pine2)  # Output: True (Same shared object)
