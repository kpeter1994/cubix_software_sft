from peewee import Model, IntegerField, CharField, DecimalField, DateField
from db.db_config import db

class Share(Model):
    portfolio_id = IntegerField()
    share_id = CharField()
    cost_value = DecimalField()
    quantity = IntegerField()
    date = DateField()

    class Meta:
        database = db
        table_name = "share"

    def to_dict(self):
        """Az objektum szótár formátumra alakítása"""
        return {
            "id": self.id,
            "portfolio_id": self.portfolio_id,
            "share_id": self.share_id,
            "cost_value": str(self.cost_value),  # A Decimal típusú mezőt sztringgé alakítjuk
            "quantity": self.quantity,
            "date": self.date.isoformat()  # Dátum formátum ISO 8601 szerint
        }

    @classmethod
    def create_share(cls, portfolio_id, share_id, cost_value, quantity, date):
        """Új részvény hozzáadása a portfólióhoz"""
        try:
            share = cls.create(
                portfolio_id=portfolio_id,
                share_id=share_id,
                cost_value=cost_value,
                quantity=quantity,
                date=date
            )
            return share
        except Exception as e:
            raise Exception(f"Részvény rögzítése sikertelen: {str(e)}")

    @classmethod
    def get_by_portfolio_id(cls, portfolio_id):
        """Részvények lekérése portfólió ID alapján"""
        return cls.select().where(cls.portfolio_id == portfolio_id)

    @staticmethod
    def get_by_portfolio_and_id(portfolio_id, share_id):
        return Share.select().where(
            (Share.portfolio_id == portfolio_id) & (Share.id == share_id)
        ).first()
