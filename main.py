import models.utils
from models.Brewery import Brawery
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Give me a city")
    parser.add_argument("--city", type=str)
    args = parser.parse_args()
    city = args.city
    breweries_info = models.utils.get_breweries(city=city)
    breweries_classes = []
    for brewery in breweries_info:
        breweries_classes.append(
            Brawery(
                brewery["id"],
                brewery["name"],
                brewery["brewery_type"],
                brewery["street"],
                brewery["address_2"],
                brewery["address_3"],
                brewery["city"],
                brewery["state"],
                brewery["county_province"],
                brewery["postal_code"],
                brewery["country"],
                brewery["longitude"],
                brewery["latitude"],
                brewery["phone"],
                brewery["website_url"],
                brewery["updated_at"],
                brewery["created_at"]
            )
        )
    for brew in breweries_classes:
        print(brew)
