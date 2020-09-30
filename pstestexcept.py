from pscustomexception import check_4_limit, RangeError

try:
    check_4_limit(.15)
except RangeError as err:
    print(err)