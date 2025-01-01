"""This example is to illustrate use of Nested loop. Ideally, this is not correct way to code adhering to Solid Principle"""
class Survey:
    def __init__(self, SurveyId, SurveyTitle,SurveyType,SurveyTemplate,SurveyQuestions):
        self.SurveyId = SurveyId
        self.SurveyTitle = SurveyTitle
        self.SurveyType = SurveyType
        self.SurveyTemplate = SurveyTemplate
        self.questions = []
        for SurveyQuestion in SurveyQuestions:
            question = self.Question(
                SurveyQuestion["QuestionId"],
                SurveyQuestion["QuestionText"],
                SurveyQuestion["QuestionTitle"],
                SurveyQuestion["QuestionResponses"]
                        )   
            self.questions.append(question)
    class Question:
        def __init__(self,QuestionId, QuestionText,QuestionTitle,QuestionResponses):
            self.QuestionId = QuestionId
            self.QuestionText = QuestionText
            self.QuestionTitle = QuestionTitle
            self.QuestionResponses = QuestionResponses
            self.responses = []

            for QuestionResponse in QuestionResponses:
                response = self.Response(
                QuestionResponse["ResponseId"],
                QuestionResponse["ResponseText"]
                        )   
                self.responses.append(response)


        class Response:
            def __init__(self,ResponseId,ResponseText):
                self.ResponseId = ResponseId
                self.ResponseText = ResponseText

        def getResponse(self):
            return self.responses


    def getQuestions(self):
        return self.questions


if __name__ == "__main__":
    SurveyQuestions = [
        {
            "QuestionId" : "Q1",
            "QuestionText": "What is your Gender",
            "QuestionTitle" : "Gender",
            "QuestionResponses" : [
                {
                    "ResponseId":"R1",
                    "ResponseText":"Response 1 - Male"
                },
                {
                    "ResponseId":"R2",
                    "ResponseText":"Response 2 - Female"
                },
                {
                    "ResponseId":"R3",
                    "ResponseText":"Response 3 - Trans Gender"
                }
            ]
        },
        {
            "QuestionId" : "Q2",
            "QuestionText": "What is your Ethnicity",
            "QuestionTitle" : "Ethnicity",
            "QuestionResponses" : [
                {
                    "ResponseId":"R1",
                    "ResponseText":"Response 1 - Ethnicity 1"
                },
                {
                    "ResponseId":"R2",
                    "ResponseText":"Response 2 - Ethnicity 2"
                },
                {
                    "ResponseId":"R3",
                    "ResponseText":"Response 3 - Ethnicity 3"
                }
            ]
        }
    ]

S001 = Survey("S001", "S001 - Title","S001 - Type","S001 - Template",SurveyQuestions)
S001Questions = S001.getQuestions()
for question in S001Questions:
    print(question.QuestionId)
    print(question.QuestionText)
    print(question.QuestionTitle)
    responses = question.getResponse()
    for response in responses:
        print(response.ResponseId)
        print(response.ResponseText)