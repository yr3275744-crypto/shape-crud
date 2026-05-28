import logging
def creat_manage_shape_logger():
    """docstring"""
    logger = logging.getLogger(__name__)
    logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s | %(levelname)s | %(message)s", filename = "manage_shapes.log")
    return logger



if __name__ == "__main__":
    manage_shapes_logger = creat_manage_shape_logger()
    print(manage_shapes_logger)
    manage_shapes_logger.info("The logger is working.")