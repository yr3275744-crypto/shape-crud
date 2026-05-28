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


# def create_circle_dict():
#     radius = float(input("Enter the radius: "))


def main():
    pass