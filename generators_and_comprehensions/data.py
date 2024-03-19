# Named Tuples are described in the documentation
# https://docs.python.org/3/library/collections.html#collections.namedtuple

from collections import namedtuple

people = [
    ("John Cleese", "cleese@gmail.com"),
    ("Terry Gilliam", "gilliam@gmail.com"),
    ("Eric Idle", ""),
    ("Terry Jones", "jones@gmail.com"),
    ("Graham Chapman", "chapman@gmail.com"),
    ("Michael Palin", "")
]

plant = namedtuple('Plant', ['name', 'scientific_name', 'lifecycle', 'plant_type'])
plantdetails = namedtuple('PlantDetails', ['scientific_name', 'lifecycle', 'plant_type'])

basic_plants_list = [
    ("Andromeda", "Pieris japonica", "Evergreen", "Shrub"),
    ("Bellflower", "Campanula", "perennial", "Flower"),
    ("China Pink", "Dianthus", "Perennial", "Flower"),
    ("Daffodil", "Narcissus", "Perennial", "Flower"),
    ("Evening Primrose", "Oenothera", "Biennial", "Flower"),
    ("French Marigold", "Tagetes patula", "Annual", "Flower"),
    ("Golden Hakone Grass", "Hakonechloa macra", "Perennial", "Grass"),
    ("Hydrangea", "Hydrangea", "evergreen", "Shrub"),
    ("Iris", "Iris", "Perennial", "Flower"),
    ("Japanese Camellia", "Camellia japonica", "Evergreen", "Shrub"),
    ("Lavender", "Lavendula", "Perennial", "Plant/shrub"),
    ("Lilac", "Syringa vulgaris", "Deciduous", "Shrub"),
    ("Magnolia", "Magnolia", "Deciduous, evergreen", "Shrub"),
    ("Peony", "Paeonia", "Perennial", "Shrub"),
    ("Queen Anne's Lace", "Daucus carota", "Biennial", "Flower"),
    ("Red Hot Poker", "Kniphofia", "Perennial", "Flower"),
    ("Snapdragon", "Antirrhinum majus", "Annual", "Flower"),
    ("Sunflower", "Helianthus", "Annual", "Flower"),
    ("Tiger Lily", "Lilinium tigrinium", "Perennial", "Flower"),
    ("Witch Hazel", "Hamamelis", "Deciduous", "Shrubs"),
]

plants_list = [
    plant("Andromeda", "Pieris japonica", "Evergreen", "Shrub"),
    plant("Bellflower", "Campanula", "perennial", "Flower"),
    plant("China Pink", "Dianthus", "Perennial", "Flower"),
    plant("Daffodil", "Narcissus", "Perennial", "Flower"),
    plant("Evening Primrose", "Oenothera", "Biennial", "Flower"),
    plant("French Marigold", "Tagetes patula", "Annual", "Flower"),
    plant("Golden Hakone Grass", "Hakonechloa macra", "Perennial", "Grass"),
    plant("Hydrangea", "Hydrangea", "evergreen", "Shrub"),
    plant("Iris", "Iris", "Perennial", "Flower"),
    plant("Japanese Camellia", "Camellia japonica", "Evergreen", "Shrub"),
    plant("Lavender", "Lavendula", "Perennial", "Shrub"),
    plant("Lilac", "Syringa vulgaris", "Deciduous", "Shrub"),
    plant("Magnolia", "Magnolia", "Deciduous, evergreen", "Shrub"),
    plant("Peony", "Paeonia", "Perennial", "Shrub"),
    plant("Queen Anne's Lace", "Daucus carota", "Biennial", "Flower"),
    plant("Red Hot Poker", "Kniphofia", "Perennial", "Flower"),
    plant("Snapdragon", "Antirrhinum majus", "Annual", "Flower"),
    plant("Sunflower", "Helianthus", "Annual", "Flower"),
    plant("Tiger Lily", "Lilinium tigrinium", "Perennial", "Flower"),
    plant("Witch Hazel", "Hamamelis", "Deciduous", "Shrub"),
]

plants_dict = {
    "Andromeda": plantdetails("Pieris japonica", "Evergreen", "Shrub"),
    "Bellflower": plantdetails("Campanula", "Annual, biennial, perennial", "Flower"),
    "China Pink": plantdetails("Dianthus", "Perennial", "Flower"),
    "Daffodil": plantdetails("Narcissus", "Perennial", "Flower"),
    "Evening Primrose": plantdetails("Oenothera", "Biennial", "Flower"),
    "French Marigold": plantdetails("Tagetes patula", "Annual", "Flower"),
    "Golden Hakone Grass": plantdetails("Hakonechloa macra", "Perennial", "Grass"),
    "Hydrangea": plantdetails("Hydrangea", "Deciduous, evergreen", "Shrub"),
    "Iris": plantdetails("Iris", "Perennial", "Flower"),
    "Japanese Camellia": plantdetails("Camellia japonica", "Evergreen", "Shrub"),
    "Lavender": plantdetails("Lavendula", "Perennial", "Shrub"),
    "Lilac": plantdetails("Syringa vulgaris", "Deciduous", "Shrub"),
    "Magnolia": plantdetails("Magnolia", "Deciduous, evergreen", "Shrub"),
    "Peony": plantdetails("Paeonia", "Perennial", "Shrub"),
    "Queen Anne's Lace": plantdetails("Daucus carota", "Biennial", "Flower"),
    "Red Hot Poker": plantdetails("Kniphofia", "Perennial", "Flower"),
    "Snapdragon": plantdetails("Antirrhinum majus", "Annual", "Flower"),
    "Sunflower": plantdetails("Helianthus", "Annual", "Flower"),
    "Tiger Lily": plantdetails("Lilinium tigrinium", "Perennial", "Flower"),
    "Witch Hazel": plantdetails("Hamamelis", "Deciduous", "Shrub"),
}
