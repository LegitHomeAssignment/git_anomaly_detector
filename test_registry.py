from event_handlers import BaseEventHandler
from registry import Registry

class FakeEventHandler(BaseEventHandler):
    pass


def test_registry():
    registry = Registry()
    event_type = 'test'
    registry.register(event_type, FakeEventHandler)
    handlers = registry.get_handlers(event_type)
    assert len(handlers), 1
    registry.register(event_type, FakeEventHandler)
    assert len(handlers), 1
    registry.deregister(event_type, FakeEventHandler)
    handlers = registry.get_handlers(event_type)
    assert len(handlers) == 0, 'handlers list is not empty'
