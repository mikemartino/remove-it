#!/usr/bin/python3 -i

import json
import logging

from TrafficFile import TrafficFile

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_traffic_files():
    result = []
    with open("./files.txt") as f:
        for cnt, type_file in enumerate(f):
            filetype, filename = str(type_file).split(',')
            result.append(TrafficFile(filename.strip(), filetype.strip()))
            logging.info(result[-1])

    return result


def __main__():
    logger.info("Starting remove-it...")
    traffic_files = load_traffic_files()

    with open("backup.log") as f:
        for cnt, line in enumerate(f):
            backup_data = json.loads(line)

            for traffic_file in traffic_files:
                backup_files = backup_data.get("item", {}).get("files", [])
                delete_me = {'type': traffic_file.filetype, 'name': traffic_file.filename}

                logger.debug("Found the following files in {}".format("backup.log"))
                logger.debug(json.dumps(backup_files, indent=2))

                if delete_me in backup_files:
                    logger.info("Found and deleting file 'name' : '{}' from files".format(delete_me.get('name')))
                    del backup_files[backup_files.index(delete_me)]

        logger.info("Writing updated info to new file")
        logger.debug(json.dumps(backup_data, indent=2))
        output_filename = "backup.log" + ".updated"
        with open(output_filename, 'w') as output_file:
            json.dump(backup_data, output_file, indent=2)

        logging.info("Finished writing {}".format(output_filename))

    logger.info("Exiting...")


if __name__ == '__main__':
    __main__()