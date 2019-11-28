# In[0]:
import requests
import json

def invoke_service(ml_service_key, ml_service_scoring_endpoint, ml_service_input):
    headers   = {"Authorization": "Bearer " + ml_service_key,
                 "Content-Type": "application/json"}
    response  = requests.post(ml_service_scoring_endpoint, headers=headers, data=ml_service_input)
    result = response.json()
    return result



# In[1]: Create example document
example_document = """On november 9th 1989, as the Berlin Wall tumbled, 
Hans-Joachim Binder was on night shift at the potash mine in Bischofferode, 
a village in the communist-ruled German Democratic Republic. 
Mr Binder, a maintenance worker who had toiled in the mine for 17 years, had no idea of the momentous events unfolding 240km (150 miles) to the east. 
The first sign something was up was when most of his colleagues disappeared to investigate what was happening at the border with West Germany, 
just ten minutes’ drive away. Only three returned to complete their shift. Less than a year later Germany was reunited, 
capping one of the most extraordinary stories in modern history. 
Not only had a communist dictatorship collapsed, releasing 16m people from the fear of the Stasi (secret police) and the stultification of censorship. 
Unlike any other country ever freed from tyranny, the entire population of East Germany was given citizenship of a big, 
rich democracy. As a grand, if ill-fated, gesture of welcome the West German chancellor, 
Helmut Kohl, converted some of their worthless savings into hard currency at the preposterously generous exchange rate of one Deutschmark to one Ostmark."""

example_document1 = """I was driving down El Camino and stopped at a red light.
It was about 3pm in the afternoon. The sun was bright and shining just behind the stoplight.
This made it hard to see the lights. There was a car on my left in the left turn lane.
A few moments later another car, a black sedan pulled up behind me. 
When the left turn light changed green, the black sedan hit me thinking 
that the light had changed for us, but I had not moved because the light 
was still red. After hitting my car, the black sedan backed up and then sped past me.
I did manage to catch its license plate. The license plate of the black sedan was ABC123. 
"""

# In[4]: Test service response
summarizer_service_key = "" #leave this value empty if the service does not have authentication enabled
summarizer_service_scoring_endpoint = ''
summarizer_service_input = json.dumps({"text" : example_document, "count" : "None", "ratio" : "1"})


# In[2]
summarizer_result = invoke_service(summarizer_service_key, summarizer_service_scoring_endpoint, 
                                   summarizer_service_input)
serviceoutput = ' '.join(summarizer_result)
formatted_result =  serviceoutput.replace("\\n", " ").strip() #if len(summarizer_result) > 0 else "N/A"
print(formatted_result)