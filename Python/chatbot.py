from chatterbot import ChatBot

bot = ChatBot(
    "Math & Time Bot",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
        ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
    )

response =bot.get_response("what is 4+9?")
print (response)

reponse =bot.get_response("time is ")
print (response)
