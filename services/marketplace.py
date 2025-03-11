from repositories.storage import PersistentLayer
from datetime import datetime

class MarketPlace:
    def __init__(self):
        self.storage = PersistentLayer()
    
    def register_user(self, username):
        username = username.lower()
        if self.storage.user_exists(username):
            print("Error - user already existing")
        else:
            self.storage.save_user(username)
            print("Success")
    
    def create_listing(self, username, title, description, price, category):
        username = username.lower()
        if not self.storage.user_exists(username):
            print("Error - unknown user")
            return
        
        listing_id = self.storage.generate_listing_id()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.storage.save_listing(listing_id, title, description, price, category, username, created_at)
        print(listing_id)
    
    def delete_listing(self, username, listing_id):
        username = username.lower()
        if not self.storage.listing_exists(listing_id):
            print("Error - listing does not exist")
            return
        
        if self.storage.get_listing_owner(listing_id) != username:
            print("Error - listing owner mismatch")
            return
        
        self.storage.delete_listing(listing_id)
        print("Success")
    
    def get_listing(self, username, listing_id):
        username = username.lower()
        if not self.storage.user_exists(username):
            print("Error - unknown user")
            return
        
        listing = self.storage.get_listing(listing_id)
        if not listing:
            print("Error - not found")
            return
        
        print(listing)
    
    def get_category(self, username, category):
        username = username.lower()
        if not self.storage.user_exists(username):
            print("Error - unknown user")
            return
        
        listings = self.storage.get_listings_by_category(category)
        if not listings:
            print("Error - category not found")
            return
        
        for listing in listings:
            print(listing)
    
    def get_top_category(self, username):
        username = username.lower()
        if not self.storage.user_exists(username):
            print("Error - unknown user")
            return
        
        top_category = self.storage.get_top_category()
        if not top_category:
            print("Error - no categories found")
            return
        
        print(top_category)