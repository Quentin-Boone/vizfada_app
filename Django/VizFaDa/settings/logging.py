LOGGING = {
    # Define the logging version
    'version': 1,
    # Enable the existing loggers
    'disable_existing_loggers': False,

    # Define the handlers
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },

        'console': {
            'class': 'logging.StreamHandler',
        },
    },
   # Define the loggers
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
