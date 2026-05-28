import shape_manager

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


def get_user_coice() -> int:
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
    try:
        radius = float(input("Enter the radius: "))
        return {"type": "circle", "radius":radius}
    
    except ValueError:
        raise ValueError("The radius value is invalid.")


def create_square_dict() -> dict:
    try:
        side = float(input("Enter the side value: "))
        return {"type": "square", "side":side}
    
    except ValueError:
        raise ValueError("The side value is invalid.")
    

def create_rectangle_dict() -> dict:
    try:
        length_side = float(input("Enter the length side value: "))
        width_side =  float(input("Enter the width side value: "))
        return {"type": "square", "length_side":length_side, "width_side":width_side}
    
    except ValueError:
        raise ValueError("The side value is invalid.")



def main():
    pass