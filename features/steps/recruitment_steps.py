from behave import given, when, then
from screenplay.tasks.menu import Menu
from screenplay.tasks.addCandidate import addCandidate
from screenplay.tasks.ListVacancy import listVacancy
from screenplay.tasks.uploadFile import UploadFile
from screenplay.tasks.InfoCandidate import InfoCandidate
from screenplay.tasks.keepdata import keepData
from screenplay.tasks.handleForm import HandleApplicationStage, HandleShortlistCandidate, HandleScheduledStage
from screenplay.tasks.infoInterview import InfoInterview


@given(u'create a contract')
def step_impl(context):
      contract = context.table[0]
      context.actor.attempts_to(Menu())
      context.actor.attempts_to(addCandidate())
      context.actor.attempts_to(listVacancy())
      context.actor.attempts_to(InfoCandidate(contract['firstName'],contract['middleName'],contract['lastName'],contract['email'],contract['phone'],contract['Keywords'],contract['notes'] ))
      context.actor.attempts_to(UploadFile('TEXT.txt'))
      context.actor.attempts_to(keepData())
      context.actor.attempts_to(HandleApplicationStage())
      context.actor.attempts_to(HandleShortlistCandidate())
      context.actor.attempts_to(HandleScheduledStage())

@when(u'create an interview')
def step_impl(context):
    interview = context.table[0]
    context.actor.attempts_to(InfoInterview(
        interview['name'],
        interview['interviewer_field'],
        interview['date_field']
    ))

# @then("the interview is schedule Successful") 
# def step_impl(context):

# @then("offers a job")
# def step_impl(context):
     
# @then("hired the user")
# def step_impl(context):