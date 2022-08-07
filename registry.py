class Registry():
    handlers = {}

    @classmethod
    def get_handlers(cls, event_type):
        return cls.handlers.get(event_type, [])

    @classmethod
    def register(cls, event_type, handler_cls):
        if event_type in cls.handlers:
            event_type_handlers = cls.handlers[event_type]
            if handler_cls not in event_type_handlers:
                event_type_handlers.append(handler_cls)
        else:
            cls.handlers[event_type] = [handler_cls]

    @classmethod
    def deregister(cls, event_type, handler_cls):
        if event_type in cls.handlers and handler_cls in cls.handlers[event_type]:
            handler_index = cls.handlers[event_type].index(handler_cls)
            cls.handlers[event_type].pop(handler_index)
