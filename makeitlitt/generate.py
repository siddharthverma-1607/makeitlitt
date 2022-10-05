def get_myString(value, split_obj, **parameters):
    """
    Gets the value based on the split char passed
    Optional keyword arguments::
    split_obj : [Datatype -> STRING] character to split your string. [Mandatory]
    split_pos_toGet : [Datatype -> INT] string to grab after split, 0 is LEFT [Default] | 1 is RIGHT. 
    split_strlen : 
        [List] with 2 INT values [LEFT_INDEX, RIGHT_INDEX]
        Length of the string to grab from (Left -> Right). [Default - complete string based on split_pos_toGet value for split]
    add_chartostr : [Datatype -> STRING] Add a single character as prefix and suffix for the string. [Default is empty a '' string]
    return_type : [Datatype -> INT] Return type for the extracted string, 0 is List [Default] | 1 is CSV
    """

    default_parameters = {'split_pos_toGet': 0,
                          'split_strlen': [], 'add_chartostr': '', 'return_type': 0}

    # parameter check & update
    for parameter_key in parameters.keys():
        if parameter_key not in ['split_pos_toGet', 'split_strlen', 'add_chartostr', 'return_type']:
            raise TypeError(
                "'{}' is an invalid keyword argument for get_myString() \nFor more details for valid parameters try:\nhelp(get_myString) OR\nget_myString.__doc__", parameter_key)

        else:
            # Updating default parameters value
            if parameter_key == 'split_strlen' and len(parameters[parameter_key]) not in [0, 2]:
                raise ValueError(
                    "Too many or less value passed for 'split_strlen'  keyword argument for get_myString() \nFor more details for valid parameters try:\nhelp(get_myString) OR\nget_myString.__doc__")

            if (parameter_key == 'return_type' or parameter_key == 'split_pos_toGet') and parameters[parameter_key] not in [0, 1]:
                raise ValueError(
                    "Expected 0 or 1 for 'return_type' keyword argument for get_myString() \nFor more details for valid parameters try:\nhelp(get_myString) OR\nget_myString.__doc__")

            # Updating correct values
            default_parameters[parameter_key] = parameters[parameter_key]

    # --------------------------------------------------------------------------------------------
    # Checking based on split_pos_toGet : [Datatype -> INT] string to grab after split, 0 is LEFT [Default] | 1 is RIGHT.
    if default_parameters['split_pos_toGet'] == 1:
        return_value = []
        for i in value.split("\n"):
            if len(i.split(split_obj)) >= 2:
                # Getting value by split_strlen value passed | Rest all will remain same without this argument passed
                if len(default_parameters['split_strlen']) == 0:
                    return_value.append(default_parameters['add_chartostr'] + i.split(split_obj)[
                        default_parameters['split_pos_toGet']] + default_parameters['add_chartostr'])

                elif len(default_parameters['split_strlen']) == 2:
                    return_value.append(default_parameters['add_chartostr'] + i.split(split_obj)[
                        default_parameters['split_pos_toGet']][default_parameters['split_strlen'][0]:default_parameters['split_strlen'][1]] + default_parameters['add_chartostr'])

    else:

        # Getting value by split_strlen value passed | Rest all will remain same without this argument passed
        if len(default_parameters['split_strlen']) == 0:
            return_value = [default_parameters['add_chartostr'] + i.split(split_obj)[
                default_parameters['split_pos_toGet']] + default_parameters['add_chartostr'] for i in value.split("\n")]

        elif len(default_parameters['split_strlen']) == 2:
            return_value = [default_parameters['add_chartostr'] + i.split(split_obj)[
                default_parameters['split_pos_toGet']][default_parameters['split_strlen'][0]:default_parameters['split_strlen'][1]] + default_parameters['add_chartostr'] for i in value.split("\n")]

    # Returning based on return_type
    if default_parameters['return_type'] == 0:
        return return_value
    else:
        return ','.join(return_value)


def creator():
    """Aur Bhai kesa laga. Abh ham hai ek izzatdaar Open Source Developer\n -- Siddharth Verma"""
    print("Aur Bhai kesa laga. Abh ham hai ek izzatdaar Open Source Developer\n -- Siddharth Verma")
