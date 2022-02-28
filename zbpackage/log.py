import logging

def set_logger():
    # Create a custom logger
    global logger
    logger = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.setLevel(logging.INFO)
    return  logger



if __name__=="__main__":
    logger=set_logger()
    logger.info("test info")
    logger.warning("test warn")
