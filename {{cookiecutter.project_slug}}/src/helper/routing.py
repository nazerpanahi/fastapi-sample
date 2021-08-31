from typing import Optional, Callable, Dict, Tuple

from fastapi.routing import APIRouter
from starlette.datastructures import URLPath
from starlette.routing import Match


def reverse(router: APIRouter, name: str, **path_params: str) -> URLPath:
    return router.url_path_for(name=name, **path_params)


def resolve(router: APIRouter, path: str, method: str) -> Tuple[Match, Optional[Callable], Optional[Dict]]:
    # starlette.routing.Router.__call__
    scope: dict = {
        'type': 'http',
        'method': method,
        'path': path
    }
    match: Match = Match.NONE
    endpoint: Optional[Callable] = None
    path_params: Optional[Dict] = None
    for route in router.routes:
        match, child_scope = route.matches(scope)
        if match == Match.FULL:
            match = Match.FULL
            endpoint = child_scope.get('endpoint')
            path_params = child_scope.get('path_params')
            break
        elif match == Match.PARTIAL:
            match = Match.PARTIAL
            endpoint = child_scope.get('endpoint')
            path_params = child_scope.get('path_params')
        else:
            continue
    return match, endpoint, path_params
