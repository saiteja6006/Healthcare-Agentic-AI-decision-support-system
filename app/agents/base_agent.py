class BaseAgent:
    def __init__(self,
                 name:str):
        self.name = name

    def execute(
            self,
            data
    ):
        raise NotImplementedError(
            "Agent must implement execute method"
        )    
        