from behave import given, when, then
from screenplay.tasks.navigate import NavigateTo
from screenplay.tasks.login import Login
from screenplay.tasks.menu import Menu
from screenplay.tasks.addCandidate import addCandidate
from screenplay.tasks.ListVacancy import listVacancy
from screenplay.tasks.uploadFile import UploadFile
from screenplay.tasks.InfoCandidate import InfoCandidate
from screenplay.tasks.keepdata import keepData
from screenplay.tasks.handleForm import HandleApplicationStage, HandleShortlistCandidate, HandleScheduledStage
from screenplay.tasks.infoInterview import InfoInterview
from screenplay.questions.dashboard import DashboardIsVisible
from screenplay.actor import Actor

@given('{actor} is on the login page')
def step_impl(context, actor):
    context.actor = Actor(actor, context.driver)
    context.actor.attempts_to(NavigateTo("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"))

@when('he enters his credentials')
def step_impl(context):
    credentials = context.table[0]
    context.actor.attempts_to(
        Login(credentials['username'], credentials['password'])
    )

@when('he should see the dashboard')
def step_impl(context):
    assert context.actor.can_see(DashboardIsVisible())

@then(u'create a contract')
def step_impl(context):
      contract = context.table[0]
      context.actor.attempts_to(Menu())
      context.actor.attempts_to(addCandidate())
      context.actor.attempts_to(listVacancy())
      context.actor.attempts_to(InfoCandidate(contract['firstName'],contract['middleName'],contract['lastName'],contract['email'],contract['phone'],contract['Keywords'],contract['notes'] ))
      context.actor.attempts_to(UploadFile('resume.pdf'))
      context.actor.attempts_to(keepData())
      context.actor.attempts_to(HandleApplicationStage())
      context.actor.attempts_to(HandleShortlistCandidate())
      context.actor.attempts_to(HandleScheduledStage())
      context.actor.attempts_to(InfoInterview())