from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app=app

    def can_login(self, username, password):
        client=Client("http://localhost/mantis/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc.login(username, password)
            return True
        except WebFault:
            return False

    def mc_projects_get_user_accessible(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            projects = []
            full_project_list = client.service.mc_projects_get_user_accessible(username, password)
            for i in range(len(full_project_list)):
                projects.append(Project(id=full_project_list[i].id, name=full_project_list[i].name))
            return projects
        except WebFault:
            return False