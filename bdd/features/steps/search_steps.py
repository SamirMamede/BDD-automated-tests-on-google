from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'we access the google website')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.google.com/')
    

@given(u'We fill in the search entry')
def step_impl(context):
    context.element = context.driver.find_element(By.NAME, 'q')
    context.element.click()
    

@when(u'we click the search button')
def step_impl(context):
    context.element.send_keys('google')
    context.element.submit()
    

@then(u'We should visualize the result')
def step_impl(context):
    assert context.driver.title == "google - Pesquisa Google"