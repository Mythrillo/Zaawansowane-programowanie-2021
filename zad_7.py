import requests


class Brawery:

    def __init__(
        self,
        id: int,
        name: str,
        brewery_type: str,
        street: str,
        address_2: str,
        address_3: str,
        city: str,
        state: str,
        county_province: str,
        postal_code: str,
        country: str,
        longitude: str,
        latitude: str,
        phone: str,
        website_url: str,
        updated_at: str,
        created_at: str
    ) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self) -> str:
        tmp = ""
        for attr, value in self.__dict__.items():
            if not attr.startswith("__"):
                tmp += f"{attr}: {value} "
        return tmp


def get_breweries() -> list:
    url = "https://api.openbrewerydb.org/breweries"
    response = requests.get(
        url=url,
        )
    if response.status_code == 200:
        return response.json()
    else:
        return []


if __name__ == "__main__":
    breweries_info = get_breweries(n=1)
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
