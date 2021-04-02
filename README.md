# internet-technology-proj2

## 1. Briefly discuss how you implemented the LS functionality of tracking which TS responded to the query and timing out if neither TS responded.
We opened a connection betweeen the client and the LS and then the LS and the two TS. We first have the client send a query to the LS and then the LS forwards that to both of the TS. Each TS uses a loop to itereate through its local DNS table and responds with a response. If one server responds, the LS will close its connection with the other TS and forward the response back to the client. If there is no response from either server, then the LS will timeout.
## 2. Are there known issues or functions that aren't working currently in your attached code? If so, explain.
There are no known issues
## 3. What problems did you face developing code for this project?
We had to consider how the LS would be able to recieve a response from one TS and handle the other TS. Also we had to figure out how much time is needed before a timeout.
## 4. What did you learn by working on this project?
