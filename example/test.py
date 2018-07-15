from bast.bast import Bast
from .route.route import route_

if __name__ == '__main__':
    app = Bast(route_)
    app.run(debug=True)
