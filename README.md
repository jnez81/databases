### Databases Artifact
This artifact is designed to function as a stock market securities information reporting service and utilizes a RESTful API web-based protocol to retrieve specified company data in conjunction with a MongoDB database of company stocks information.  

### Enhancements
The improvements made to this artifact consist of incorporating MongoDB statements that will update user-defined values for existing documents using the company’s business ID.  The original code simply prompted the user to identify which company ticker abbreviation to use in order to update the “volume” value in the document.  Each company document has a large number of values associated with the company’s respective stock market information and prompting the user to identify several specific values to update adds much more functionality and purpose to the program.  The user inputs the business ID into the database and will then prompt the user to select which values to update in the document.
