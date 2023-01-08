from app import add, init_celery
import logging
import time

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    handlers=[logging.StreamHandler()])

def main():
    logging.info("add")
    res = add.delay(1,2)
    logging.info(f"res={res.get()} {res.status}")
    
if __name__ == "__main__":
    #init_celery()
    
    main()
