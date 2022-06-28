# AUTHOR: Yoni Asulin
 
import re
import os
os.system('color')
 
SUCCESS_COLOR = '\033[32m'
FAILURE_COLOR = '\033[31m'
END = '\033[0m'
 
totalTestCount = 0
failureCount = 0
 
def assert_equal(val, func, args):
    global totalTestCount
    global failureCount
    totalTestCount += 1
 
    result = func(*args)
    if result == val:
        print(SUCCESS_COLOR + "success" + END)
    else:
        failureCount += 1
        print(FAILURE_COLOR + "failure" + END)
        print(f'{func.__name__}({",".join(n for n in args)})')
        print(f'Expected: {val}')
        print(f'Got: {result}')

 
def print_test_suite_summary():
    print()
    print(f'Total number of assertions: {totalTestCount}')
    print(f'Passed tests: {totalTestCount - failureCount}/{totalTestCount}')
 
#------------------------------------------------------------------------------------------------------------
 
def is_complex_question(str):
    return bool(re.match(".*\[\].*\[\]*", str))
 
def has_word_quota(str):
    return bool(re.match("\[\d{1,3}\]", str))


#------------------------------------------------------------------------------------------------------------
 
str = "hello world"
assert_equal(False, is_complex_question, [str])
 
str = "hello [] world"
assert_equal(False, is_complex_question, [str])
 
str = ""
assert_equal(False, is_complex_question, [str])
 
str = "   [] "
assert_equal(False, is_complex_question, [str])
 
str = "hello [] world []"
assert_equal(True, is_complex_question, [str])
 
str = "hello [] wonderful []    world []"
assert_equal(True, is_complex_question, [str])
 
str = " "
assert_equal(False, has_word_quota, [str])
 
str = "[]"
assert_equal(False, has_word_quota, [str])
 
str = "[עד    מילים]"
assert_equal(False, has_word_quota, [str])
 
str = "[עד  150  מילים]"
assert_equal(True, has_word_quota, [str])
 
str = "עד  150  מילים]"
assert_equal(False, has_word_quota, [str])
 
str = "עד  150  מילים"
assert_equal(False, has_word_quota, [str])
 
str = "[עד  265845  מילים]"
assert_equal(False, has_word_quota, [str])
 
#------------------------------------------------------------------------------------------------------------
 
print_test_suite_summary()