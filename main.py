#TODO:add logs to all files. add checks to load_from_json methods in shape_manager

from shape_manager import ShapeManager

def print_menu() -> None:
    """docstring"""
    print("""Welcome to the shape-manager!
          Choose an option:
          1.Add shape
          2.Update shape
          3.Remove shape
          4.Show all shapes
          5.Exit""")
    return None


def get_user_choice() -> int:
    """docstring"""
    try:
        user_choice = int(input("Enter your choice: "))
        if 1 <= user_choice <= 5:
            return user_choice
        else:
            raise ValueError("You must enter a number between 1 and 5.")
    
    except ValueError as e:
        raise e("You must enter a number between 1 and 5.")

    



def main(json_file_path:str) -> None:
    """docstring"""
    
    shape_manager = ShapeManager(json_file_path)
    user_choice = None

    while user_choice != 5:
        print_menu()
        
        try:
            user_choice = get_user_choice()        
            
            match user_choice:
                case 1:
                    add_shape_handle(shape_manager, json_file_path, create_dict_functions)
                
                case 2:
                    update_shape_handle(shape_manager, json_file_path, create_dict_functions)
                    
        except (KeyError, ValueError) as e:
            print(e)
            continue
            



if __name__ == "__main__":
    main("shapes.json")