from random import randrange
from model.project import Project

def test_delete_project(app):
    app.session.login("administrator", "root")
    old_projects = app.soap.mc_projects_get_user_accessible("administrator", "root")
    app.project.open_projects_page()
    if len(old_projects) == 0:
        project = app.project.generate_project_data()
        app.project.fill_project_form(project)
        old_projects = app.soap.mc_projects_get_user_accessible("administrator", "root")
        app.project.open_projects_page()
    index = randrange(len(old_projects))
    name = old_projects[index].name
    app.project.open(name)
    app.project.delete()
    old_projects[index:index + 1] = []
    new_projects = app.soap.mc_projects_get_user_accessible("administrator", "root")
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)