class PersistentLayer:
    def __init__(self):
        self.users = set()
        self.listings = {}
        self.categories = {}
        self.listing_id_counter = 100000
    
    def save_user(self, username):
        self.users.add(username)
    
    def user_exists(self, username):
        return username in self.users
    
    def generate_listing_id(self):
        self.listing_id_counter += 1
        return self.listing_id_counter
    
    def save_listing(self, listing_id, title, description, price, category, username, created_at):
        self.listings[listing_id] = {
            "title": title, "description": description, "price": price,
            "category": category, "username": username, "created_at": created_at
        }
        
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append((listing_id, created_at))
    
    def delete_listing(self, listing_id):
        if listing_id in self.listings:
            listing = self.listings.pop(listing_id)
            self.categories[listing["category"]].remove((listing_id, listing["created_at"]))
    
    def listing_exists(self, listing_id):
        return listing_id in self.listings
    
    def get_listing_owner(self, listing_id):
        return self.listings[listing_id]["username"]
    
    def get_listing(self, listing_id):
        if listing_id in self.listings:
            listing = self.listings[listing_id]
            return "|".join(map(str, [listing["title"], listing["description"], listing["price"], listing["created_at"], listing["category"], listing["username"]]))
        return None
    
    def get_listings_by_category(self, category):
        if category not in self.categories or not self.categories[category]:
            return []
        
        sorted_listings = sorted(self.categories[category], key=lambda x: x[1], reverse=True)
        return [self.get_listing(listing_id) for listing_id, _ in sorted_listings]
    
    def get_top_category(self):
    
        return max(self.categories.keys(), key=lambda c: (len(self.categories[c]), c), default=None)