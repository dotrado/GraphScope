import networkx.algorithms.tests.test_triads
import pytest

from graphscope.experimental.nx.utils.compat import import_as_graphscope_nx

import_as_graphscope_nx(networkx.algorithms.tests.test_triads,
                        decorators=pytest.mark.usefixtures("graphscope_session"))
