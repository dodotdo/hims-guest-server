# -*- coding: utf-8 -*-

from hims_guest import app, db

if __name__ == '__main__':
    db.create_all(app=app)
    app.run(host="0.0.0.0", port=8082, debug=True, threaded=True)
