from repositories.UserRepository import UserRepository
from repositories.CategoryRepository import CategoryRepository
from repositories.ListRepository import ListRepository  


class MarketPlace:
    def __init__(self):
        self.user_storage = UserRepository()
        self.category_storage = CategoryRepository()
        self.list_storage = ListRepository(self.user_storage, self.category_storage)
        
    '''User service'''
    def register_user(self, username):
        username = username.lower()
        if self.user_storage.exists(username):
            return("Error - user already existing")
        else:
            self.user_storage.save(username)
            return("Success")
        
    '''List service'''
    def create_listing(self, username, title, description, price, category):
        username = username.lower()
        if not self.user_storage.exists(username):
            return("Error - unknown user")

        listing_id = self.list_storage.save(title, description, price, category, username)
        return str(listing_id)

    def delete_listing(self, username, listing_id):
        username = username.lower()
        if not self.list_storage.exists(listing_id):
            return "Error - listing does not exist"
            
        listing = self.list_storage.get_by_id(listing_id)
        if listing["username"] != username:
            return "Error - listing owner mismatch"
            
        self.list_storage.delete(listing_id)
        return "Success"
    
    def get_listing(self, username, listing_id):
        username = username.lower()
        if not self.user_storage.exists(username):
            return "Error - unknown user"
            
        listing = self.list_storage.get_formatted(listing_id)
        if not listing:
            return "Error - not found"
            
        return listing
    
    ''' Category service'''
    def get_category(self, username, category):
        username = username.lower()
        if not self.user_storage.exists(username):
            return ["Error - unknown user"]
        
        listings = self.list_storage.get_by_category(category)
        if not listings:
            return ["Error - category not found"]
        
        return listings
    
    def get_top_category(self, username):
        username = username.lower()
        if not self.user_storage.exists(username):  
            return ["Error - unknown user"]
            
        top_categories = self.category_storage.get_top_categories()  
        if not top_categories:
            return ["Error - no categories found"]
            
        return top_categories