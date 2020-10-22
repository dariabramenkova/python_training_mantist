from model import project
from model.project import Project


def test_create_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.create(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects)+1==len(new_projects)
