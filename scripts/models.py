from pydantic import BaseModel


class Artist(BaseModel):
    discord: str


class Credit(BaseModel):
    artist: Artist
    artists: list[Artist]


credit_39_51 = Credit(
    artist=Artist(discord="Aegide#8190"),
    artists=[Artist(discord="Bubba-Rottweiler#7322")]
)


json_39_51 = credit_39_51.json()
print(json_39_51)


# {
#     "artist": {
#         "discord": "Aegide#8190"
#     },
#     "artists": [
#         {
#             "discord": "Bubba-Rottweiler#7322"
#         }
#     ]
# }