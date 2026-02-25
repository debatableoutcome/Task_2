class ApiErrors:
    # users
    USER_ALREADY_EXISTS = 'User already exists'
    REQUIRED_FIELDS = 'Email, password and name are required fields'
    INVALID_CREDENTIALS = 'email or password are incorrect'
    UNAUTHORIZED = 'You should be authorised'

    # orders
    NO_INGREDIENTS = 'Ingredient ids must be provided'
    INVALID_INGREDIENTS = 'One or more ids provided are incorrect'
    INTERNAL_SERVER_ERROR = 'Internal Server Error'