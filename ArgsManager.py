#import argparse
class ArgsManager:
    def __init__(self,parser):
        self.args = self.manag(parser)
        self._input_file = self.args['input_file']
        self._output_file = self.args['output_file']
        self._what_to_do = self.args['do']
        self.code = self.args['code']
    @property
    def input_file(self):
        return self._input_file
    @property
    def output_file(self):
        return self._output_file
    @property
    def what_to_do(self):
        return self._what_to_do
    def manag(self,parser):
        #parser = argparse.ArgumentParser
        parser.add_argument('-i','--input',help='the input csv file name')
        parser.add_argument('-o','--output',help='the output csv file name')
        parser.add_argument('-d','--do',choices = ['e','d'],default='e',help='\'e\' for encryption \n \'d\' for decryption encryption is the defult')
        parser.add_argument('-c','--code',help='encryption code')
        args = parser.parse_args()
        return {
        'input_file' : args.input,
        'output_file' : args.output if args.output is not None else 'output_file.csv',
        'do' : args.do ,
        'code' : args.code
        }
