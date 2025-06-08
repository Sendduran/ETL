from sqlmodel import Field , SQLModel, BigInteger, Column

class Facts(SQLModel, table=True):
    facts_id : int | int = Field(default=None, sa_column=Column(BigInteger(),primary_key=True)) # int - Id is created in python using timestamp()
    fact : str # This is a must field
    created_date : str # Iso format returns a string
