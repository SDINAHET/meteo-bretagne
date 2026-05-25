# from datetime import datetime

# from sqlalchemy import Column, DateTime, Float, Integer, String

# from .database import Base


# class MeteoHistorique(Base):
#     __tablename__ = "meteo_historique"

#     id = Column(Integer, primary_key=True, index=True)
#     ville = Column(String, index=True, nullable=False)
#     lat = Column(Float, nullable=False)
#     lon = Column(Float, nullable=False)
#     temperature = Column(Float)
#     pluie_mm = Column(Float)
#     rafales_kmh = Column(Float)
#     code_meteo = Column(Integer)
#     risque = Column(String)
#     created_at = Column(DateTime, default=datetime.utcnow, index=True)


from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, Integer, String

from .database import Base


class MeteoHistorique(Base):
    __tablename__ = "meteo_historique"

    id = Column(Integer, primary_key=True, index=True)
    ville = Column(String, index=True, nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    temperature = Column(Float)
    pluie_mm = Column(Float)
    rafales_kmh = Column(Float)
    code_meteo = Column(Integer)
    risque = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        index=True
    )
