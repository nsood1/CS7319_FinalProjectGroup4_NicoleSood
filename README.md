# TherapyBot - Nicole Sood, CS7314

**NOTES:** The readMe below provides a brief desciption on how to compile the project, differences between architectures as well as the rationel of my selection. Please refer to the word doc in the repo if you would like a more detailed write up about the different architectures I explored, as well as the pro's and con's for each. 

<h2> Compilation & Implementation: </h2>

I implemented this project using Python, with PyCharm 2023.2.1 (Professional Edition) as my IDE. This IDE can be downloaded from JetBrains. The system I am running is: MacOS Catalina Version 10.15.7 (which is out of date in terms of MacOS). 

To install my application, simply clone my GitHub repo onto your local machine. 

Necessary Packages/imports: 
-	Sqlite3
-	nltk.chat.util
-	socket
-	select
-	sys
-	_thread_

To compile & execute the system:
1.	Set up the database. 
- For this step, navigate to the file directory and run the command 		```python databasesetup.py```
  
2.	Initiate the server: 
-	The server is set up to run locally. To get it running, you will need to provide an ip address as well as a port number. You will run the command: 			python server.py [ip address] [port number] 
Example: ```python server.py 127.0.0.1 8081```
- Please note: When you intialise the server, it will take roughly a minute to load and then it will ask you if you would like to maintain the database. Client's can only connect after you have inputed a yes or a no. 

3.	Connect the client: 
-	Using a different terminal, navigate to the directory and then run the client.py file, then run the following command: 
python client.py [ip address] [port number]
-	Example: ```python client.py 127.0.0.1 8081```
-	Multiple clients can connect to the same server. Each will have their own thread and can hold their own conversation. 

<h2> Rational of Architecture Choice and Differences in Design Styles: </h2>

Overall, some of the main differences of the architecture styles include:
1.	Resource Distribution:
a.	A client server provides a clear distinction between a client and a server, meaning clearer access controls
b.	A P2P considers all nodes equal therefore they all have access to the same data.

2.	Centralisation: 
a.	A Client server uses a centralised model meaning that one server is responsible for allocating resources
b.	A P2P is decentralised - meaning that all peers have the same controls and access to data.

3.	Scalability:
a.	A client server will require more hardware to deal with more demand. 
b.	A P2P can scale as large as needed.  

<h2> Rational of Architecture Selection: </h2>

Overall, I settled on a client server architecture for my project. This is because I deemed it the most appropriate for my needs.

Firstly, I wanted my chatbot to be scalable without the need to individually add users to the system. This was a property that came with a client server. Additionally, I wanted a centralised system. This is because I did not want a client to have direct access to my database. The centralization with a server allows for clients to connect, and the server will manage any requests.

Secondly, although denial of service is something which is a risk for both architecture styles. For this project, I deemed it as less of a risk with the client server because of the added centralision attribute. Within a P2P network, if a virus is introduced it can easily spread across the whole system causing a denial of service. In a client server on the other hand, denial of service can present itself differently such as slow response times. If the system were to go down, it would also be easier to restart the server. 

Lastly, many industry chatbots such as chatGPT or Discord run off a client server architecture style. As a result, I thought it would be better in terms of an industry standard practice to follow what is currently established. 
