from behave import given, when, then
from features.steps.step_impl_handle import *


global_list_variables = []

@given(u'User navigates to "{base_URL}"')
def step_impl(context , base_URL):
    #print("=== Running === -> " + base_URL)

    obj_handle_impl.perform_initial_setup(global_list_variables)
    obj_handle_impl.landingPageNavigate(global_list_variables, base_URL)



@when(u'He enters "{Fund_Number}"')
def step_impl(context , Fund_Number):
    #print("=== Running === -> " + Fund_Number)
    obj_handle_impl.searchForFund(global_list_variables ,Fund_Number)



@then(u'System should return "{Return_Page}"')
def step_impl(context , Return_Page):
    #print("=== Running === -> " + Return_Page)
    obj_handle_impl.WaitForOverviewPage(global_list_variables, Return_Page)

@then(u'He verifies fund name is "{Fund_Name}"')
def step_impl(context , Fund_Name):
    #print("=== Running === -> " + Fund_Name)
    obj_handle_impl.verifyFundName(global_list_variables , Fund_Name)

@then(u'He verifies expense ratio is "{Expense_Ratio}"')
def step_impl(context , Expense_Ratio):
    obj_handle_impl.verifyExpenseRatio(global_list_variables, Expense_Ratio)

@then(u'All actions should be successful')
def step_impl(context,):
    obj_handle_impl.final_verification(global_list_variables)
