"""
Dependency Inversion Principle (DIP)
====================================

The Dependency Inversion Principle states that:
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.

In simple terms: Depend on interfaces/abstractions, not on concrete implementations.

Simple Example: Email Service System
"""

# ==========================================
# WRONG WAY - Violating DIP
# ==========================================

class GmailClient:
    """Concrete email client implementation"""
    
    def send_email(self, message):
        return f"Sending via Gmail: {message}"


class EmailService:
    """
    BAD EXAMPLE: EmailService directly depends on GmailClient (concrete class)
    
    Problems:
    - Hard-coded dependency on Gmail
    - Cannot easily switch to other email providers
    - Difficult to test (can't mock Gmail easily)
    - Violates DIP by depending on concrete implementation
    """
    
    def __init__(self):
        # BAD: Direct dependency on concrete class
        self.gmail_client = GmailClient()
    
    def send_email(self, message):
        # Tightly coupled to Gmail implementation
        return self.gmail_client.send_email(message)


# ==========================================
# RIGHT WAY - Following DIP
# ==========================================

class EmailClient:
    """
    GOOD EXAMPLE: Abstract interface for email clients
    
    Benefits:
    - Defines contract that all email clients must follow
    - Allows EmailService to work with any email provider
    - Enables easy testing with mock implementations
    """
    
    def send_email(self, message):
        """Send email - must be implemented by concrete clients"""
        raise NotImplementedError("Must implement send_email method")


class GmailClientGood(EmailClient):
    """Gmail implementation of EmailClient interface"""
    
    def send_email(self, message):
        return f"Sending via Gmail: {message}"


class OutlookClient(EmailClient):
    """Outlook implementation of EmailClient interface"""
    
    def send_email(self, message):
        return f"Sending via Outlook: {message}"


class YahooClient(EmailClient):
    """Yahoo implementation of EmailClient interface"""
    
    def send_email(self, message):
        return f"Sending via Yahoo: {message}"


class EmailServiceGood:
    """
    GOOD EXAMPLE: EmailService depends on EmailClient interface
    
    Benefits:
    - Works with any EmailClient implementation
    - Easy to switch email providers
    - Easy to test with mock implementations
    - Follows DIP by depending on abstraction
    """
    
    def __init__(self, email_client: EmailClient):
        # GOOD: Depends on interface, not concrete class
        self.email_client = email_client
    
    def send_email(self, message):
        return self.email_client.send_email(message)
    
    def send_welcome_email(self, user_email):
        message = f"Welcome to our service! Sent to: {user_email}"
        return self.send_email(message)


# ==========================================
# USAGE EXAMPLES
# ==========================================

def demonstrate_dip_violation():
    """Show problems with tight coupling"""
    print("=== VIOLATING DIP (BAD WAY) ===")
    
    # EmailService is tightly coupled to Gmail
    email_service = EmailService()
    result = email_service.send_email("Hello World!")
    print(result)
    
    print("Problem: EmailService is stuck with Gmail only!")
    print("What if we want to use Outlook or Yahoo? We'd have to modify EmailService!")
    print()


def demonstrate_dip_compliance():
    """Show benefits of depending on abstractions"""
    print("=== FOLLOWING DIP (GOOD WAY) ===")
    
    # We can use any email client with the same EmailService!
    
    # Using Gmail
    gmail_client = GmailClientGood()
    gmail_service = EmailServiceGood(gmail_client)
    print(gmail_service.send_email("Hello from Gmail!"))
    
    # Using Outlook - same EmailService, different implementation!
    outlook_client = OutlookClient()
    outlook_service = EmailServiceGood(outlook_client)
    print(outlook_service.send_email("Hello from Outlook!"))
    
    # Using Yahoo - again, same EmailService!
    yahoo_client = YahooClient()
    yahoo_service = EmailServiceGood(yahoo_client)
    print(yahoo_service.send_welcome_email("user@example.com"))
    
    print("\nBenefit: EmailService works with any email provider!")
    print()


if __name__ == "__main__":
    demonstrate_dip_violation()
    demonstrate_dip_compliance()