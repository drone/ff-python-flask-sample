from flask import Blueprint, jsonify, abort
from .error_handler import Unauthorized, BadRequest, ServerError

from featureflags.evaluations.auth_target import Target

from .utils import cf


bp = Blueprint('dashboard', __name__, url_prefix='/api/flags')


@bp.route('/', methods=(['GET']))
def dashboard():
    try:
        target = Target(identifier='harness')
        value = cf.bool_variation('test_key', target, False)
        result = {
            'test_key': value
        }
        return jsonify(result)
    except KeyError as e:
        abort(400, description=e)
    except BadRequest as e:
        abort(400, description=e.description)
    except Unauthorized as e:
        abort(401, description=e.description)
    except ServerError as e:
        abort(500, description=e.description)