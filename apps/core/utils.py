from apps.core.config import settings


def generate_api_prefix(prefix: str):
    prefix = f'/{settings.API_VERSION}{prefix}'
    if prefix.endswith('/'):
        prefix = prefix[:-1]

    return prefix
from typing import Union
def common_parameters(

    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    print('inmm originalsss?')
    return {"q": q, "skip": skip, "limit": limit}
