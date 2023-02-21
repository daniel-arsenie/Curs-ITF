"""
Un site pentru programari. Sugestii tabele:
clients
employees
appointments
Services
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    appointments = relationship("Appointment", back_populates="client")


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    appointments = relationship("Appointment", back_populates="employee")


class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    appointment_time = Column(String)

    client = relationship("Client", back_populates="appointments")
    employee = relationship("Employee", back_populates="appointments")
    service = relationship("Service")


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    appointments = relationship("Appointment", back_populates="service")


Base.metadata.create_all(engine)
