"""
Liskov Substitution Principle (LSP)
===================================

The Liskov Substitution Principle states that objects of a superclass should be 
replaceable with objects of a subclass without breaking the application.

In simple terms: If you have a parent class, you should be able to use any child 
class in its place without causing problems.

Simple Example: Bird Flying System
"""

# ==========================================
# WRONG WAY - Violating LSP
# ==========================================

class Bird:
    """Base bird class"""
    
    def fly(self):
        """All birds should be able to fly, right? WRONG!"""
        return "Flying high in the sky!"


class Sparrow(Bird):
    """Sparrow can fly - this works fine"""
    
    def fly(self):
        return "Sparrow flying fast!"


class Penguin(Bird):
    """
    BAD EXAMPLE: Penguin violates LSP!
    
    Problem: Penguins can't fly, but they inherit from Bird which has a fly() method.
    This breaks the expectation that all Bird objects can fly.
    """
    
    def fly(self):
        # This violates LSP - penguin can't fly but is forced to implement fly()
        raise Exception("Penguins can't fly!")


def make_bird_fly_bad(bird):
    """
    This function expects any Bird to be able to fly.
    It will break when given a Penguin!
    """
    return bird.fly()


# ==========================================
# RIGHT WAY - Following LSP
# ==========================================

class FlyingBird:
    """Base class for birds that can fly"""
    
    def fly(self):
        return "Flying through the air!"


class FlightlessBird:
    """Base class for birds that cannot fly"""
    
    def walk(self):
        return "Walking on the ground!"


# Now our specific birds inherit from the correct base class
class SparrowGood(FlyingBird):
    """Sparrow inherits from FlyingBird - makes sense!"""
    
    def fly(self):
        return "Sparrow flying quickly!"


class Eagle(FlyingBird):
    """Eagle also inherits from FlyingBird"""
    
    def fly(self):
        return "Eagle soaring majestically!"


class PenguinGood(FlightlessBird):
    """
    GOOD EXAMPLE: Penguin inherits from FlightlessBird
    
    Benefits:
    - No fly() method to break
    - Has walk() method which makes sense for penguins
    - Can be substituted wherever FlightlessBird is expected
    """
    
    def walk(self):
        return "Penguin waddling on ice!"


class Ostrich(FlightlessBird):
    """Ostrich also inherits from FlightlessBird"""
    
    def walk(self):
        return "Ostrich running very fast!"


def make_flying_bird_fly(flying_bird):
    """
    This function works with any FlyingBird.
    LSP is satisfied - any FlyingBird can be substituted here.
    """
    return flying_bird.fly()


def make_flightless_bird_walk(flightless_bird):
    """
    This function works with any FlightlessBird.
    LSP is satisfied - any FlightlessBird can be substituted here.
    """
    return flightless_bird.walk()




# ==========================================
# USAGE EXAMPLES
# ==========================================

def demonstrate_lsp_violation():
    """Show how LSP violation causes problems"""
    print("=== VIOLATING LSP (BAD WAY) ===")
    
    sparrow = Sparrow()
    penguin = Penguin()
    
    birds = [sparrow, penguin]
    
    for bird in birds:
        try:
            result = make_bird_fly_bad(bird)
            print(f"Result: {result}")
        except Exception as e:
            print(f"ERROR: {e}")
    
    print("Problem: Penguin breaks the system because it can't fly!")
    print()


def demonstrate_lsp_compliance():
    """Show how proper LSP implementation works"""
    print("=== FOLLOWING LSP (GOOD WAY) ===")
    
    # Flying birds
    sparrow = SparrowGood()
    eagle = Eagle()
    flying_birds = [sparrow, eagle]
    
    print("Flying birds:")
    for bird in flying_birds:
        result = make_flying_bird_fly(bird)  # LSP satisfied!
        print(f"- {result}")
    
    # Flightless birds
    penguin = PenguinGood()
    ostrich = Ostrich()
    flightless_birds = [penguin, ostrich]
    
    print("\nFlightless birds:")
    for bird in flightless_birds:
        result = make_flightless_bird_walk(bird)  # LSP satisfied!
        print(f"- {result}")
    
    print("\nBenefit: All substitutions work correctly!")
    print()


if __name__ == "__main__":
    demonstrate_lsp_violation()
    demonstrate_lsp_compliance()