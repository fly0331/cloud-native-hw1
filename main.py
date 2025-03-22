import re
from services.marketplace import MarketPlace

def parse_command(command):

    matches = re.findall(r"'([^']*)'|(\S+)", command)
    parsed = [match[0] if match[0] else match[1] for match in matches]

    if not parsed:
        return []
    return parsed

def main():
    cloudShop = MarketPlace()
    
    while True:
        try:
            command = input("# ").strip()
            if not command:
                continue

            parts = parse_command(command)
            if len(parts) == 0:
                print("Error - empty command")
                continue

            action = parts[0]

            if action == "REGISTER":
                if len(parts) != 2:
                    print("Error - invalid REGISTER format")
                    continue
                print(cloudShop.register_user(parts[1]))

            elif action == "CREATE_LISTING":
                if len(parts) != 6:
                    print("Error - invalid CREATE_LISTING format")
                    continue
                username, title, description, price, category = parts[1:]
                print(cloudShop.create_listing(username, title, description, price, category))

            elif action == "DELETE_LISTING":
                if len(parts) != 3:
                    print("Error - invalid DELETE_LISTING format")
                    continue
                username, listing_id = parts[1], int(parts[2])
                print(cloudShop.delete_listing(username, listing_id))

            elif action == "GET_LISTING":
                if len(parts) != 3:
                    print("Error - invalid GET_LISTING format")
                    continue
                username, listing_id = parts[1], int(parts[2])
                print(cloudShop.get_listing(username, listing_id))

            elif action == "GET_CATEGORY":
                if len(parts) != 3:
                    print("Error - invalid GET_CATEGORY format")
                    continue
                username, category = parts[1], parts[2]
                result = cloudShop.get_category(username, category)
                for item in result:
                    print(item)

            elif action == "GET_TOP_CATEGORY":
                if len(parts) != 2:
                    print("Error - invalid GET_TOP_CATEGORY format")
                    continue
                username = parts[1]
                result = cloudShop.get_top_category(username)
                for item in result:
                    print(item)

            elif action == "EXIT":
                break

            else:
                print("Error - invalid command")
                
        except ValueError:
            print("Error - invalid number format")
        except IndexError:
            print("Error - missing arguments")
        except Exception as e:
            print(f"Error - {str(e)}")

if __name__ == "__main__":
    main()
