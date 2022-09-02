import pytest
import sys
sys.path.append("../../../web3.py/")

from cns import (
    CNS,
    AsyncCNS,
)
from web3.middleware import (
    async_validation_middleware,
    pythonic_middleware,
)


def test_fromWeb3_inherits_web3_middlewares(w3):
    test_middleware = pythonic_middleware
    w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = CNS.fromWeb3(w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware


# -- async -- #


@pytest.mark.asyncio
async def test_async_fromWeb3_inherits_web3_middlewares(async_w3):
    test_middleware = async_validation_middleware
    async_w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = AsyncCNS.fromWeb3(async_w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware
