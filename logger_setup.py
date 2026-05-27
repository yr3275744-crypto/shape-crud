import logging
def creat_manage_shape_logger(file_name):
    """docstring"""
    logger = logging.getLogger(__name__)
    logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s | %(levelname)s | %(message)s", filename = file_name)
    return logger

manage_shapes_logger = creat_manage_shape_logger("manage_shapes.log")

if __name__ == "__main__":
    print(manage_shapes_logger)
    manage_shapes_logger.info("The logger is working.")