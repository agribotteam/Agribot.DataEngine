import logging.config
from fastapi import  Request
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
class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

        self.setup_logging()
        
    def setup_logging(self):
        logging.config.dictConfig(LOGGING)

    async def __call__(self, scope, receive, send):
        assert scope["type"] == "http"
        request = Request(scope, receive=receive)
        
        logging.info(f"Received request: {request.method} {request.url}")
        
        async def send_with_logging(response):
            status_code = response.get("status_code", 200)  # Default to 200 if status_code is not present
            logging.info(f"Sent response: {status_code}")
            await send(response)
        
        response = await self.app(request.scope, receive, send_with_logging)
        
        return response
