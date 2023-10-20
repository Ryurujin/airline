from django.db.models import *

#plane
class ModelsPlane(Model):
    name = CharField(
        verbose_name="plane: ",
        max_length=15,
    )
    characteristics = TextField(
        speed = "speed: ",
    )
    def __str__(self):
        return f"{self.name}"


#airline
class ModelsAirline(Model):
    name = CharField(
        verbose_name="airline: ",
        max_length=15,
    )
    created_at = DateField(
        auto_now_add=True 
    )
    planes = PositiveIntegerField(
        "quantity: "
    )#

#flight
class ModelsFlight(Model):
    fro_m = CharField(
        name="from: ",
        max_length=15,
    )
    to = CharField(
        name="to: ",
        max_length=15,
    )
    plane = (
        ModelsPlane
    )
    airline = (
        ModelsAirline
    )
    price = PositiveIntegerField(
        price = "price: ",
    )





