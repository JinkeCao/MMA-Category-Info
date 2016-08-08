##>>> import json
##>>> def as_complex(dct):
##...     if '__complex__' in dct:
##...         return complex(dct['real'], dct['imag'])
##...     return dct
##...
##>>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
##...     object_hook=as_complex)
##(1+2j)
##>>> import decimal
##>>> json.loads('1.1', parse_float=decimal.Decimal)
##Decimal('1.1')
import json


with open("sephora20160807.json") as text:
    for eachLine in text:
        dct = json.loads(eachLine)
        with open("mma_sephora.json", "a") as output:
            print(json.dumps({"1st":dct["c1"], "2nd":dct["c2"], "3rd":dct["c3"], "brand":dct["brand"], "info":dct["info"]}, ensure_ascii = False, sort_keys = True), file = output)
