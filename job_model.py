from DOEDummyApp.extensions import db
from sqlalchemy.sql import func


class Jobdetails(db.Model):
    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, nullable=False)
    job_name = db.Column(db.String(60), nullable=False)
    location = db.Column(db.String(60), nullable=False)
    # job_count = db.Column(db.Integer, nullable=False)
    job_status = db.Column(db.Integer, nullable=False, default=1)
    creationdatetime = db.Column(
        db.DateTime, nullable=False, server_default=func.now())
    updationdatetime = db.Column(
        db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    createdby = db.Column(db.String(20))
    modifiedby = db.Column(db.String(20))

    def __init__(self, customer_id, job_name, location, job_status, createdby):
        self.customer_id = customer_id
        self.job_name = job_name
        self.location = location
        # self.job_count = job_count
        self.job_status = job_status
        self.createdby = createdby

    def __repr__(self):
        return '<Jobdetails %r>' % self.job_id
