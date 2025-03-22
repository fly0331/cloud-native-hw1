class CategoryRepository:
    def __init__(self):
        self._categories = {}  
        
    def save(self, category_name):
        if category_name not in self._categories:
            self._categories[category_name] = []
    
    def delete(self, category_name):
        if category_name in self._categories:
            del self._categories[category_name]
    
    def get_all(self):
        return list(self._categories.keys())
    

    def add_listing(self, category_name, listing_id, created_at):
        if category_name not in self._categories:
            self._categories[category_name] = []
        self._categories[category_name].append((listing_id, created_at))

    def remove_listing(self, category_name, listing_id):
        if category_name in self._categories:
   
            for i, (id, _) in enumerate(self._categories[category_name]):
                if id == listing_id:
                    self._categories[category_name].pop(i)
                    break
    
    def get_listings_by_category(self, category_name):
        if category_name not in self._categories:
            return []
        return self._categories[category_name].copy()
    
    def get_top_categories(self):
        if not self._categories:
            return []
        
        max_count = max([len(listings) for listings in self._categories.values()], default=0)
        return [category for category, listings in self._categories.items() 
                if len(listings) == max_count]