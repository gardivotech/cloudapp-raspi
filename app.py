from fileinput import filename
import logging, time

logging.basicConfig(filename='./logs/' + str(time.asctime()) + '.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

if __name__ == '__main__':
        logging.debug('DroneApp has started!')