class Employee:
    """ Base class for both individual employees and managers/directors. """
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        """ Method to display employee details. Overridden by subclasses. """
        raise NotImplementedError("Subclass must implement show_details()")

class IndividualEmployee(Employee):
    """ Leaf class: Represents a single employee with no subordinates. """
    def show_details(self):
        return f"{self.position}: {self.name}"

class Manager(Employee):
    """ Composite class: Can manage multiple employees (Leaf or Composite). """
    def __init__(self, name, position):
        super().__init__(name, position)
        self.subordinates = []

    def add_subordinate(self, employee):
        """ Adds an employee or another manager under this manager. """
        self.subordinates.append(employee)

    def show_details(self):
        """ Displays the manager and their subordinates. """
        details = f"{self.position}: {self.name}\n"
        for emp in self.subordinates:
            details += f"  └── {emp.show_details()}\n"
        return details
    

if __name__ == "__main__":
    # Create individual employees (Leaf)
    emp1 = IndividualEmployee("Alice", "Software Engineer")
    emp2 = IndividualEmployee("Bob", "Software Engineer")
    emp3 = IndividualEmployee("Charlie", "Data Scientist")

    # Create managers (Composite)
    manager1 = Manager("David", "Engineering Manager")
    manager1.add_subordinate(emp1)
    manager1.add_subordinate(emp2)

    manager2 = Manager("Eve", "Data Science Manager")
    manager2.add_subordinate(emp3)

    # Create a director (Composite)
    director = Manager("Frank", "Director of Technology")
    director.add_subordinate(manager1)
    director.add_subordinate(manager2)

    # Create the CEO (Composite)
    ceo = Manager("Grace", "CEO")
    ceo.add_subordinate(director)

    # Display the company hierarchy
    print(ceo.show_details())