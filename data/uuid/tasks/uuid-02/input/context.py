import uuid

result1 = uuid.uuid1()

namespace = uuid.NAMESPACE_DNS
name = "example.com"
result2 = uuid.uuid3(namespace, name)

result3 = uuid.uuid5(namespace, name)

try:
    from uuid import uuid6 as uuid6_std
    result4 = uuid6_std()
except (ImportError, AttributeError):
    try:
        from uuid6 import uuid6 as uuid6_pkg
        result4 = uuid6_pkg()
    except ImportError:
        result4 = None

result5 = uuid.getnode()
