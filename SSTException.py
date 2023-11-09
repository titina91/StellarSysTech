class NotYesOrNoError(Exception):

    def __init__(self, input, message="Input are incorrect!"):
        self.input = input
        self.message = message
        super().__init__(self.message)

