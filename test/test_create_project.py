from model import project
from model.project import Project


def test_create_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.mc_projects_get_user_accessible("administrator", "root")
    app.project.create(project)
    new_projects = app.soap.mc_projects_get_user_accessible("administrator", "root")
    assert len(old_projects)+1==len(new_projects)
