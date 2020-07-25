from django.db import models
from django.contrib.auth.models import User


# Model for individual whisk(e)y reviews
class Dram(models.Model):

    # Define different categories of whisk(e)y
    CATEGORIES = (
        ("SM", "Single Malt Scotch"),
        ("BS", "Blended Scotch"),
        ("BMS", "Blended Malt Scotch"),
        ("IB", "Irish Blend"),
        ("SPS", "Single Pot Still Irish"),
        ("B", "Bourbon"),
        ("CW", "Canadian Whisky"),
        ("RW", "Rye Whiskey"),
        ("JW", "Japanese Whisky"),
        ("WW", "World/Misc Whisk(e)y"),
    )

    REGIONS = (
        ("SP", "Speyside"),
        ("HL", "Highlands/Other Islands"),
        ("IS", "Islay"),
        ("LL", "Lowlands"),
        ("CT", "Campbelltown"),
        ("KT", "Kentucky"),
        ("TN", "Tennessee"),
        ("OS", "Other U.S. State"),
        ("N", "N/A"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dram = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    category = models.CharField(max_length=30, choices=CATEGORIES, default="WW")
    # What region or state the whisk(e)y is from
    region = models.CharField(max_length=30, choices=REGIONS, default="N")
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    nosing = models.TextField(default="Add nosing notes here.")
    tasting = models.TextField(default="Add tasting notes here.")