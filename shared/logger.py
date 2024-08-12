import logging.config
import os 
import logging

LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
        'simple': {
            'format': "%(asctime)s : %(levelname)s : %(message)s", # '%(asctime)s - %(lineno)-4d - %(name)-10s - %(levelname)-8s - %(message)s ',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': '',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename':os.getenv('LOG_FILE', 'app.log'),   
            'level': 'DEBUG',
            'formatter': 'simple',
        }
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'AGRI_DUMP': {  
            'handlers': ['file'],
            'level': 'INFO',  
            'propagate': False,
        }
    },

}
def setup_logging():
    logging.config.dictConfig(LOGGING)

