# Bringing Finn to Life

### Prototype Overview
This prototype just showcases what Finn should be able to do. As the user asks it questions, Finn answers with whatever information is most relevant to the question. This is a basic version where Finn is able to answer basic questions based on the knowledge base information.

### How to Run the Prototype
After opening a codespace or cloning the repo, run the file mock_finn.py. In the terminal it will say "Ask Finn a question (or type 'quit'):" here you can ask any question you would like or type 'quit'. 

If the question can be answered (meaning it has a keyword in the json file) then Finn will give a suggestion to your health needs. If not Finn will just say "I don’t have that information yet." 

### Architecture of the Prototype
The way the code process is it first takes the input from the user, then fills the parameters in mock_finn.py. Next we go to knowledge_base.json to find any keywords and if they are found the answer is outputted from mock_finn.py but if the else statement of "I don’t have that information yet." is returned.

### mock_finn.py
This file just acts as a bridge between the user and the data (json). It determines how Finn will answer whatever question is inputted. 

### knowledge_base.py
This json has all the manual data filled with keywords and their corresponding answers. This makes it so Finn knows what to say based on what question is asked.

#### Things I noted
There are so many possible things a user can ask Finn but as this is just a basic prototype I just added keywords that a health AI bot may answer. Keywords such as exercise, workout, and movement all probably have the same advice/answer so I grouped keywords and words similar to give Finn the ability to answer more questions than if there was just one keyword such as just exercise.

Along with that, as Finn is an AI bot, it shouldn't have the ability to give actual medical advice so I used keywords such as pain, hurt, attack, etc to let the user know that Finn cannot answer those type of questions and that emergency services should be contacted instead.

### Example inputs and outputs
Ask Finn a question (or type 'quit'): I want to have a balanced diet.<br>
Finn: Aim for a balanced diet of fruits, vegetables, whole grains, and lean protein.

Ask Finn a question (or type 'quit'): I feel so overwhelmed with work.<br>
Finn: Try deep breathing, meditation, or a short walk to reduce stress.

Ask Finn a question (or type 'quit'): Any advice on being better with exercise?<br>
Finn: Adults should try to get at least 30 minutes of exercise every day.

Ask Finn a question (or type 'quit'): im so sleepy<br>
Finn: Aim for 7–9 hours of sleep each night.

### Future Work
This is very much a simple prototype so using other tools can make Finn more advanced and provide the user with a wider range of responses. 

Firstly, using some sort of API would be amazing as it would provide Finn with more data and it would be able to answer more questions.

Also using LLMs would be great as it would allow Finn to be more flexible with its conversation and make the conversation seem more natural. As of right now if I asked Finn "How much exercise should I do everyday?" and "Should I exercise with or without weights" it gives the same answer because it just sees that the key word of exercise is in both questions so it would answer with "Adults should try to get at least 30 minutes of exercise every day.". Using an LLM can resolve this issue.

This brings up the idea of storing user data to optimize Finn. Maybe if the user previously noted that they have asthma then Finn would give advice around that knowledge. This would bring privacy concerns that would need to be addressed. 
