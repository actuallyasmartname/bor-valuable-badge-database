import connexion
from threading import Thread

from borValBadgeDbServer import encoder
from borValBadgeDbServer.db.db import loadDatabase
from borValBadgeDbServer.db.checker import missingReportWorker


def main():
    loadDatabase()

    Thread(target=missingReportWorker, daemon=True).start()

    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'BoR Valuable Badge Database'},
                pythonic_params=True)

    app.run(host="0.0.0.0", port=8080)


if __name__ == '__main__':
    main()
