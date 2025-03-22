from datetime import datetime

class ListRepository:
    def __init__(self, user_repository, category_repository):
        self._listings = {}
        self._id_counter = 100000
        self._user_repository = user_repository
        self._category_repository = category_repository
    
    def generate_id(self):
        self._id_counter += 1
        return self._id_counter

    def save(self, title, description, price, category, username):
        listing_id = self.generate_id()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self._listings[listing_id] = {
            "title": title,
            "description": description,
            "price": price,
            "category": category,
            "username": username,
            "created_at": created_at
        }
        
        self._category_repository.save(category)
        self._category_repository.add_listing(category, listing_id, created_at)
        
        return listing_id
    
    def delete(self, listing_id):
        if listing_id in self._listings:
            listing = self._listings.pop(listing_id)
            self._category_repository.remove_listing(listing["category"], listing_id)
            return True
        return False
    
    def exists(self, listing_id):
        return listing_id in self._listings
    
    def get_by_id(self, listing_id):
        if listing_id in self._listings:
            return self._listings[listing_id]
        return None
    
    def get_formatted(self, listing_id):
        if listing_id in self._listings:
            listing = self._listings[listing_id]
            return "|".join(map(str, [
                listing["title"],
                listing["description"],
                listing["price"],
                listing["created_at"],
                listing["category"],
                listing["username"]
            ]))
        return None
    
    def get_by_category(self, category_name):
        listings = self._category_repository.get_listings_by_category(category_name)
        if not listings:
            return []
        
        sorted_listings = sorted(listings, key=lambda x: x[1], reverse=True)
        return [self.get_formatted(listing_id) for listing_id, _ in sorted_listings]