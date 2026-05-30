#TODO:add logs to all files. add checks to load_from_json methods in shape_manager

from shape_manager import ShapeManager
import logger_setup

def print_menu() -> None:
    """docstring"""
    print("""== Welcome to the shape-manager! ==
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
        raise ValueError("You must enter a number between 1 and 5.")


def main(json_file_path:str) -> None:
    """docstring"""
    logger = logger_setup.create_manage_shape_logger()
    shape_manager = ShapeManager(json_file_path)
    user_choice = None

    while user_choice != 5:
        print_menu()
        
        try:
            user_choice = get_user_choice()        
            
            match user_choice:
                case 1:
                    shape_manager.add_shape_handle()
                
                case 2:
                    shape_manager.update_shape_handle()
                case 3:
                    shape_manager.remove_shape_handle()
                
                case 4:
                    shape_manager.show_all_shapes()
                
                    
        except (KeyError, ValueError) as e:
            print(e)
            continue
        
    return None



if __name__ == "__main__":
    main("shapes.json")