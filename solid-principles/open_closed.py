"""
Open/Closed Principle (OCP)
===========================

The Open/Closed Principle states that classes should be:
- OPEN for extension (you can add new functionality)
- CLOSED for modification (don't change existing working code)

Simple Example: Discount Calculator
"""

# ==========================================
# WRONG WAY - Violating OCP
# ==========================================

class DiscountCalculator:
    """
    BAD EXAMPLE: This violates OCP because every time we add a new discount type,
    we have to modify this existing class by adding new if-elif conditions.
    
    Problems:
    - Risk of breaking existing discount calculations
    - Class grows bigger with each new discount type
    - Hard to test individual discount types
    """
    
    def calculate_discount(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.0  # 0% discount
        elif customer_type == "premium":
            return amount * 0.1  # 10% discount
        elif customer_type == "vip":
            return amount * 0.2  # 20% discount
        # What if we want to add "student" discount? We'd have to modify this method!
        else:
            return 0


# ==========================================
# RIGHT WAY - Following OCP
# ==========================================

class Discount:
    """Base class for all discount types"""
    
    def calculate(self, amount):
        """Calculate discount amount"""
        raise NotImplementedError("Must implement calculate method")


class RegularCustomerDiscount(Discount):
    """Regular customers get no discount"""
    
    def calculate(self, amount):
        return amount * 0.0  # 0% discount


class PremiumCustomerDiscount(Discount):
    """Premium customers get 10% discount"""
    
    def calculate(self, amount):
        return amount * 0.1  # 10% discount


class VIPCustomerDiscount(Discount):
    """VIP customers get 20% discount"""
    
    def calculate(self, amount):
        return amount * 0.2  # 20% discount


# NEW DISCOUNT TYPES - Added without modifying existing code!
class StudentDiscount(Discount):
    """Students get 15% discount"""
    
    def calculate(self, amount):
        return amount * 0.15  # 15% discount


class SeniorCitizenDiscount(Discount):
    """Senior citizens get 25% discount"""
    
    def calculate(self, amount):
        return amount * 0.25  # 25% discount


class PriceCalculator:
    """
    GOOD EXAMPLE: This class works with any discount type
    without knowing the specific implementation details.
    
    Benefits:
    - Never needs to be changed when new discounts are added
    - Works with any discount that follows the Discount interface
    - Easy to test and maintain
    """
    
    def calculate_final_price(self, amount, discount):
        discount_amount = discount.calculate(amount)
        final_price = amount - discount_amount
        return final_price, discount_amount


# ==========================================
# USAGE EXAMPLES
# ==========================================

def demonstrate_ocp_violation():
    """Show the problematic approach"""
    print("=== VIOLATING OCP (BAD WAY) ===")
    calculator = DiscountCalculator()
    
    amount = 100
    customers = ["regular", "premium", "vip"]
    
    for customer_type in customers:
        discount = calculator.calculate_discount(customer_type, amount)
        final_price = amount - discount
        print(f"{customer_type.capitalize()}: ${amount} -> ${final_price} (saved ${discount})")
    
    print("Problem: To add 'student' discount, we must modify DiscountCalculator!")
    print()


def demonstrate_ocp_compliance():
    """Show the correct approach"""
    print("=== FOLLOWING OCP (GOOD WAY) ===")
    price_calculator = PriceCalculator()
    
    amount = 100
    discounts = {
        "Regular": RegularCustomerDiscount(),
        "Premium": PremiumCustomerDiscount(),
        "VIP": VIPCustomerDiscount(),
        "Student": StudentDiscount(),          # New discount added!
        "Senior": SeniorCitizenDiscount()     # Another new discount added!
    }
    
    for customer_type, discount in discounts.items():
        final_price, discount_amount = price_calculator.calculate_final_price(amount, discount)
        print(f"{customer_type}: ${amount} -> ${final_price} (saved ${discount_amount})")
    
    print("Benefit: New discounts added without changing existing code!")
    print()


if __name__ == "__main__":
    demonstrate_ocp_violation()
    demonstrate_ocp_compliance()