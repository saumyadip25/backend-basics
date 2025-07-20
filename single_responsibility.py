"""
Single Responsibility Principle (SRP)
=====================================

The Single Responsibility Principle states that a class should have only one reason to change,
meaning it should have only one job or responsibility.

Key Benefits:
- Easier to maintain and modify
- Reduced risk of introducing bugs when making changes
- Better code organization and readability
- Improved testability
"""

# ==========================================
# WRONG WAY - Violating SRP
# ==========================================

class UserManager:
    """
    BAD EXAMPLE: This class violates SRP because it has multiple responsibilities:
    1. User authentication
    2. Profile management  
    3. Email notifications
    
    Problems with this approach:
    - If authentication logic changes, this class needs to change
    - If email service changes, this class needs to change
    - If profile management changes, this class needs to change
    - Hard to test individual functionalities
    - Violates the principle of having only one reason to change
    """
    
    def authenticate_user(self, username, password):
        """Handle user authentication"""
        # Authentication logic
        print(f"Authenticating user: {username}")
        # Simulate authentication
        if username and password:
            print("User authenticated successfully")
            return True
        else:
            print("Authentication failed")
            return False

    def update_profile(self, user_id, profile_data):
        """Handle profile updates"""
        # Profile management logic
        print(f"Updating profile for user ID: {user_id}")
        print(f"New profile data: {profile_data}")
        # Simulate profile update
        print("Profile updated successfully")

    def send_welcome_email(self, user_email):
        """Handle email notifications"""
        # Email notification logic
        print(f"Sending welcome email to: {user_email}")
        # Simulate email sending
        print("Welcome email sent successfully")


# ==========================================
# RIGHT WAY - Following SRP
# ==========================================

class UserAuthenticator:
    """
    GOOD EXAMPLE: This class has a single responsibility - user authentication
    
    Benefits:
    - Only changes when authentication logic needs to change
    - Easy to test authentication functionality in isolation
    - Can be reused across different parts of the application
    - Clear and focused purpose
    """
    
    def authenticate_user(self, username, password):
        """Handle user authentication"""
        print(f"Authenticating user: {username}")
        # Simulate authentication logic
        if username and password:
            print("User authenticated successfully")
            return True
        else:
            print("Authentication failed")
            return False


class UserProfileManager:
    """
    GOOD EXAMPLE: This class has a single responsibility - profile management
    
    Benefits:
    - Only changes when profile management logic needs to change
    - Easy to test profile functionality in isolation
    - Can be extended with more profile-related methods without affecting other classes
    - Clear and focused purpose
    """
    
    def update_profile(self, user_id, profile_data):
        """Handle profile updates"""
        print(f"Updating profile for user ID: {user_id}")
        print(f"New profile data: {profile_data}")
        # Simulate profile update logic
        print("Profile updated successfully")
    
    def get_profile(self, user_id):
        """Retrieve user profile"""
        print(f"Retrieving profile for user ID: {user_id}")
        # Simulate profile retrieval
        return {"user_id": user_id, "name": "John Doe", "email": "john@example.com"}


class EmailNotificationService:
    """
    GOOD EXAMPLE: This class has a single responsibility - email notifications
    
    Benefits:
    - Only changes when email notification logic needs to change
    - Easy to test email functionality in isolation
    - Can be replaced with different notification services (SMS, push, etc.)
    - Clear and focused purpose
    """
    
    def send_welcome_email(self, user_email):
        """Send welcome email to new users"""
        print(f"Sending welcome email to: {user_email}")
        # Simulate email sending logic
        print("Welcome email sent successfully")
    
    def send_password_reset_email(self, user_email, reset_token):
        """Send password reset email"""
        print(f"Sending password reset email to: {user_email}")
        print(f"Reset token: {reset_token}")
        # Simulate password reset email logic
        print("Password reset email sent successfully")


# ==========================================
# USAGE EXAMPLES
# ==========================================

def demonstrate_srp_violation():
    """Demonstrate the problematic approach (violating SRP)"""
    print("=== DEMONSTRATING SRP VIOLATION ===")
    user_manager = UserManager()
    
    # All responsibilities handled by one class
    user_manager.authenticate_user("john_doe", "password123")
    user_manager.update_profile(1, {"name": "John Doe", "age": 30})
    user_manager.send_welcome_email("john@example.com")
    print()


def demonstrate_srp_compliance():
    """Demonstrate the correct approach (following SRP)"""
    print("=== DEMONSTRATING SRP COMPLIANCE ===")
    
    # Each class has a single responsibility
    authenticator = UserAuthenticator()
    profile_manager = UserProfileManager()
    email_service = EmailNotificationService()
    
    # Responsibilities are separated
    authenticator.authenticate_user("john_doe", "password123")
    profile_manager.update_profile(1, {"name": "John Doe", "age": 30})
    email_service.send_welcome_email("john@example.com")
    print()


if __name__ == "__main__":
    # Run demonstrations
    demonstrate_srp_violation()
    demonstrate_srp_compliance()
