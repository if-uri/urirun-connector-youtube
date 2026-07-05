# GENERATED smoke test — every handler returns a well-formed urirun envelope.
from urirun_connector_youtube import core


def test_bindings_expose_all_routes():
    text = str(core.urirun_bindings())
    assert 'transcript/query/fetch' in text
    assert 'video/query/metadata' in text
    assert 'highlights/query/extract' in text
