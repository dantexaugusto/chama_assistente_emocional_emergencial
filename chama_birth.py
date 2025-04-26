from dotenv import load_dotenv
import os
from openai import OpenAI
import json

def model_response(conversation_history):

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
   
    response = client.responses.create(
        model="gpt-4.1-nano",
        input= conversation_history
    )

    return response.output_text

def frontEnd_usrMessage_receiver(usrID, usrMessage):

    with open("behaviour_prompt_I.txt", "r") as bPrompt:
        behaviour_prompt = bPrompt.read()

    conversation_start = [
        {
            "role": "developer",
            "content": behaviour_prompt
        },
        {
            "role": "user",
            "content": "se apresente, diga quem é você e o que você faz."
        }
    ]

    try:
        with open("usrids_conversation_state.json", "r", encoding="utf-8") as idsConvJson:
            usrIDs_convDict = json.load(idsConvJson)
        
        print("users conversation history json file exists", "\n")
            
        if usrID in usrIDs_convDict.keys():
            print("User history already stored")
            conversation_history = usrIDs_convDict[usrID]
            assistant_response = model_response(conversation_history)
            conversation_history.append({"role":"assistant","content":assistant_response})
            usrIDs_convDict[usrID] = conversation_history 
            with open("usrids_conversation_state.json", "w", encoding="utf-8") as idsConvjson:
                json.dump(usrIDs_convDict, idsConvjson, indent=4, ensure_ascii=False)
    
            return assistant_response
            
        else:
            print("New user with no conversation history")
            conversation_history = conversation_start
            assistant_response = model_response(conversation_history)
            conversation_history.append({"role":"assistant","content":assistant_response})
            usrIDs_convDict[usrID] = conversation_history
            with open("usrids_conversation_state.json", "w", encoding="utf-8") as idsConvjson:
                json.dump(usrIDs_convDict, idsConvjson, indent=4, ensure_ascii=False)
    
            return assistant_response
            
    except Exception as e:
        print("Conversation history json file no found", "\n", f"{e}")
        conversation_history = conversation_start
        assistant_response = model_response(conversation_history)
        conversation_history.append({"role":"assistant", "content":assistant_response})
        usrIDs_convDict = {usrID:conversation_history}
        with open("usrids_conversation_state.json", "w", encoding="utf-8") as idsiConvjson:
            json.dump(usrIDs_convDict, idsConvjson, indent=4, ensure_ascii=False)


def main():

    print("Este é um loop infinito de conversação, para sair digite: quit", "\n")
    print("Para começar digite seu ID de usuário único.", "\n") 
    userID = input()    

    while True:

        most_recent_user_prompt = input("User: ")

        if most_recent_user_prompt == "quit":

            break
    
        frontEnd_usrMessage_receiver(usrID, most_recent_user_prompt)   

if __name__ == "__main__":
    main()

