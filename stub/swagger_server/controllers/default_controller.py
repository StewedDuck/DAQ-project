import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from swagger_server.models.data_record import DataRecord  # noqa: E501
from swagger_server.models.prediction import Prediction  # noqa: E501
from swagger_server import util


def controller_get_predictions():  # noqa: E501
    """Dust &amp; temperature predictions

     # noqa: E501


    :rtype: Union[Prediction, Tuple[Prediction, int], Tuple[Prediction, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_primary_data(place_type=None, start=None, end=None, limit=None, offset=None):  # noqa: E501
    """All KidBright (primary) readings, with optional filtering &amp; pagination

     # noqa: E501

    :param place_type: 
    :type place_type: str
    :param start: ISO8601 start timestamp (inclusive)
    :type start: str
    :param end: ISO8601 end timestamp (inclusive)
    :type end: str
    :param limit: Max number of records to return
    :type limit: int
    :param offset: Number of records to skip
    :type offset: int

    :rtype: Union[List[DataRecord], Tuple[List[DataRecord], int], Tuple[List[DataRecord], int, Dict[str, str]]
    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return 'do some magic!'


def controller_get_secondary_data(place_type=None, start=None, end=None, limit=None, offset=None):  # noqa: E501
    """All TMD (secondary) readings, with optional filtering &amp; pagination

     # noqa: E501

    :param place_type: 
    :type place_type: str
    :param start: ISO8601 start timestamp (inclusive)
    :type start: str
    :param end: ISO8601 end timestamp (inclusive)
    :type end: str
    :param limit: Max number of records to return
    :type limit: int
    :param offset: Number of records to skip
    :type offset: int

    :rtype: Union[List[DataRecord], Tuple[List[DataRecord], int], Tuple[List[DataRecord], int, Dict[str, str]]
    """
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)
    return 'do some magic!'
