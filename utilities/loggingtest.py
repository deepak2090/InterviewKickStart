import logging.config
import importcheck
logger = logging.getLogger("my_app")



def main():
    #logging.config.dictConfig(config=logging_config)
    
    logging.info("info message")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("exception message")
def sum():
    print("sum")

if __name__ == "__main__":
    main()
    