#
# This class will create the environment for parallele State.
#


class ParalleState:
    def __init__(self, dictData):
        self.data = dictData
# s = $({ $(states[i]) :"SM_"+ $(states.key()[i]) for i in range(0, len($(states.keys())) )})
#{set i = iter($states.keys()}
