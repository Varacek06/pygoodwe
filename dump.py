""" dumps the raw JSON response from the API """
import json

from config import args
from pygoodwe import API


def main() -> None:
    """dumps the raw data"""
    goodwe = API(
        system_id=args.get("gw_station_id", "1"),
        account=args.get("gw_account", "thiswillnotwork"),
        password=args.get("gw_password", "thiswillnotwork"),
    )
    # goodwe.getCurrentReadings()
    # print(json.dumps(goodwe.data, indent=4))
    # with open('/Users/macbook/programovanicko/pygoodwe/data.json', 'w') as file:
    #     file.truncate(0)  # Delete all text in the file
    #     file.write(json.dumps(goodwe.data, indent=4))
    #     print("Data dumped to data.json")
    #     file.close()

    print(goodwe.get_batteries_soc(), goodwe.are_batteries_full())

if __name__ == "__main__":
    main()
