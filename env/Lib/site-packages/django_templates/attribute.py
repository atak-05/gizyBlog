class AttributeTemplate:
    def __init__(self, **kwargs):
        self.data = {}

        for attribute in kwargs.keys():
            self.data[attribute] = kwargs[attribute]

    def get_field(self, field_name):
        if field_name in self.data.keys():
            return self.data[field_name]
        else:
            raise Exception(
                'Class {} has no field {}'.format(self.__name__, field_name))

    def get_permission_error(self, accepted_rule, action):
        return 'You must be {} to {}.'.format(
            accepted_rule, action
            )
