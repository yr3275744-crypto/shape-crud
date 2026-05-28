#TODO:add logs to all files. add checks to load_from_json methods in shape_manager

from shape_manager import ShapeManager

def print_menu() -> None:
    """docstring"""
    print("""Welcome to the shape-manager!
          Choose an option:
          1.Add shape
          2.Show all shapes
          3.Update shape
          4.Delete shape
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


def create_circle_dict() -> dict:
    """docstring"""
    radius = float(input("Enter the radius: "))
    return {"type": "circle", "radius":radius}


def create_square_dict() -> dict:
    """docstring"""
    side = float(input("Enter the side value: "))
    return {"type": "square", "side":side}
    

def create_rectangle_dict() -> dict:
    """docstring"""
    length_side = float(input("Enter the length side value: "))
    width_side =  float(input("Enter the width side value: "))
    return {"type": "square", "length_side":length_side, "width_side":width_side}
    



def add_shape_handle(shape_manager:ShapeManager, file_path:str, create_dict_functions:dict) -> None:
    """docstring"""
    try:
        shape_name = input("Enter the sape you want add: ")
        shape_dict = create_dict_functions(shape_name)
    
    except KeyError:
        raise("The shape does not exists.")
    
    except ValueError:
        raise ValueError("The value is invalid.")

    shape_object = shape_manager.create_shape(shape_dict)
    shape_manager.add_shape(shape_object)
    shape_manager.save_to_json(file_path)
    
    return None

def main(json_file_path:str) -> None:
    """docstring"""
    create_dict_functions = {"circle":create_circle_dict, 
                                   "square":create_square_dict, 
                                   "rectangle":create_rectangle_dict}
    
    shape_manager = ShapeManager(json_file_path)
    user_choice = None

    while user_choice != 5:
        print_menu()
        
        try:
            user_choice = get_user_choice()
        
        except ValueError as e:
            print(e)
            continue
        
        match user_choice:
            case 1:
                try:
                    add_shape_handle(shape_manager, json_file_path, create_dict_functions)
                except (KeyError, ValueError) as e:
                    print(e)
                    continue
            
                   



if __name__ == "__main__":
    main("shapes.json")