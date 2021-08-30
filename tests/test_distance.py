from mlproject.distance import haversine
import inspect

def test_type_of_haversine():
    assert type(haversine(5, 4, 8, -5)) == float

def test_len_of_args_haversine():
    assert len(inspect.getfullargspec(haversine).args) == 4